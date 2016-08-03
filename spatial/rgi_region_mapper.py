from shapely.geometry import Polygon, Point
from rtree.index import Index
import csv, ast

class RgiSpatial:
  # This function checks if the given spatial coordinate is within the region
  # of interest ( Buffer Zones )

  # A region of interest (1 - 13) has been defined here
  # https://github.com/polar-computing/AerosolDelta/issues/7

  # if the given point doesn't line within a buffer zone it returns 0
  @classmethod
  def bufferLandIceRegionMapper(klass, lat, lon):
    #Alaska / Canadian Rockies
    if (lat >= 45 and lat <= 63 and lon >= -180 and lon <= -110):
      return 1

    #Arctic (Eastern) Canada
    if (lat >= 60 and lon  >= -130 and lat <= 84 and lon <=  -62):
      return 2

    #Greenlan
    if (lat >= 58 and lon  >= -75 and lat <= 85 and lon <=  -25):
      return 3

    #Icelan
    if (lat >= 61 and lon  >= -26 and lat <= 68 and lon <=  -11):
      return 4

    #Arctic
    if (lat >= 70 and lon  >= -180 and lat <= 90 and lon <=  180):
      return 5

    #Scandinavia
    if (lat >= 54 and lon  >= 3 and lat <= 72 and lon <=  35):
      return 6

    #European Alps
    if (lat >= 40 and lon  >= -2 and lat <= 48 and lon <=  20):
      return 7

    #Caucasus / Middle East
    if (lat >= 23 and lon  >= 35 and lat <= 50 and lon <=  63):
      return 8

    #Himalay
    if (lat >= 21 and lon  >= 70 and lat <= 50 and lon <=  99):
      return 9

    #Africa
    if (lat >= -57 and lon >= -85 and lat <= 3 and lon <=  -60):
      return 10

    #South Americ
    if (lat >= -50 and lon >= 160 and lat <= -30 and lon <=  183):
      return 11

    #New Zealand
    if (lat >= -90 and lon >= -180 and lat <= -55 and lon <=  180) :
      return 12

    #Antarctica
    if (lat >= -4 and lon >= 29 and lat <= 2 and lon <=  38):
      return 13

    return 0

  def __init__(self,
    resolution=[0.5, 0.625],
    rgiPath,
    countryBoundryPath,
    dependencies={
    'Point': Point,
    'Polygon': Polygon,
    'Index': Index,
    'csv': csv,
    'ast': ast
  }):

    self.__dependencies = dependencies

    def rgiIceMaskBounds():
      for p in self.__dependencies['csv'].reader(open(rgiPath)):
        pt = (float(p[0]), float(p[1]))
        iceMask = self.__dependencies['Polygon']([
          (pt[0] - resolution[0]/2, pt[1] - resolution[1]/2),
          (pt[0] + resolution[0]/2, pt[1] - resolution[1]/2),
          (pt[0] + resolution[0]/2, pt[1] + resolution[1]/2),
          (pt[0] - resolution[0]/2, pt[1] + resolution[1]/2),
          (pt[0] - resolution[0]/2, pt[1] - resolution[1]/2),
        ])

        yield(float(p[2]), iceMask)

    self._geoIndex = self.__dependencies['Index']()
    self.iceMaskBounds = [ (region, iceMask) for (region, iceMask) in rgiIceMaskBounds() ]

    for pos, (region, iceMask) in enumerate(self.iceMaskBounds):
      self._geoIndex.insert(pos, iceMask.bounds)

    countryBoundries = self.__dependencies['ast'].literal_eval(open(countryBoundryPath).read())
    cBound = lambda d: map(lambda x: (x[1], x[0]), d)

    self.countryBounds = {
      'Antarctica' : (19, self.__dependencies['Polygon'](cBound(countryBoundries['Antarctica']))),
      'Greenland'  : (5,  self.__dependencies['Polygon'](cBound(countryBoundries['Greenland']))),
    }

  # This function checks if the given spatial coordinate is within the 'a strict
  # land ice mask' as defined by RGI
  # It returns 0 if the given point doesn't lie within the strict land ice mask
  # It returns a integer number indicating RGI region

  def scrictLandIceRegionMapper(self, lat, lon):
    pt = self.__dependencies['Point'](lat, lon)

    # iceMaskIndices
    iceMaskIndices = [ _ for _ in self._geoIndex.intersection((pt.coords[0])) if pt.within( self.iceMaskBounds[_][1] ) ]

    if len(iceMaskIndices) > 0:
      (region, iceMask) = self.iceMaskBounds[ iceMaskIndices[0] ]
      return region

    return 0

  # Additionally to the strict region mapping,
  # We further divide RGI 16 into 3 sub regions
  # (a) for South American glaciers
  # (b) for African glaciers
  # (c) for Papua New Guinea glaciers
  # We also ensure that Greenland/Antarctica includes the whole continent/ice sheet
  # It returns a floating point number indicating RGI region
  # ( 1, 2, .. 16.1, 16.2, 16.3 .. 19 )

  def regionsOfInterestMapper(self, lat, lon):
    pt = self.__dependencies['Point'](lat, lon)

    rg = self.scrictLandIceRegionMapper(lat, lon)

    if rg == 16:
      if lon <= -40:
        rg = 16.1
      elif lon <= 70:
        rg = 16.2
      else:
        rg = 16.3

    if rg !=0:
      return rg

    wt = lambda b: lat >= b[0] and lat <= b[2] and lon >= b[1] and lon <= b[3]

    # Country Matches
    if wt(self.countryBounds['Antarctica'][1].bounds) and pt.within( self.countryBounds['Antarctica'][1] ):
      return self.countryBounds['Antarctica'][0]

    elif wt(self.countryBounds['Greenland'][1].bounds) and pt.within( self.countryBounds['Greenland'][1] ):
      return self.countryBounds['Greenland'][0]

    return 0

