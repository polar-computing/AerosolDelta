# Extracts points of interest from satellite date
# Points of interest
from spatial.rgi_spatial_iterable import RGISpatialIterable
from spatial.rgi_region_mapper    import RgiSpatial
import os
import sys

DATA_PATH = os.environ['DATA_PATH']

merra2Params = {
  'SouthernmostLatitude': -90.0,
  'NorthernmostLatitude': 90.0,
  'WesternmostLongitude': -180.0,
  'EasternmostLongitude': 179.375,
  'LatitudeResolution': 0.5,
  'LongitudeResolution': 0.625,
}

caliopParams = {
  'SouthernmostLatitude': -84,
  'NorthernmostLatitude': 84,
  'WesternmostLongitude': -177.5,
  'EasternmostLongitude': 177.5,
  'LatitudeResolution': 1.0,
  'LongitudeResolution': 5.0,
}

if __name__ == '__main__':
  DATA_SET_TYPE = sys.argv[1]

  if DATA_SET_TYPE == 'merra2':
    dParams = merra2Params

  elif DATA_SET_TYPE == 'caliop':
    dParams = caliopParams

  rg = RgiSpatial(
      resolution=[dParams['LatitudeResolution'], dParams['LongitudeResolution']],
      rgiPath=os.path.join(DATA_PATH, "rgi-coords.csv"),
      countryBoundryPath=os.path.join(DATA_PATH, "country-boundries.json"))

  f = open(os.path.join(DATA_PATH, DATA_SET_TYPE + "-buffer.csv"), "w+")
  for (region, point) in RGISpatialIterable(RgiSpatial.bufferLandIceRegionMapper, dParams).getIterator():
    f.write("{0},{1},{2}\n".format(point[0], point[1], region))

  f = open(os.path.join(DATA_PATH, DATA_SET_TYPE + "-strict.csv"), "w+")
  for (region, point) in RGISpatialIterable(rg.regionsOfInterestMapper, dParams).getIterator():
    f.write("{0},{1},{2}\n".format(point[0], point[1], region))
