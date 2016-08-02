import numpy

class RGISpatialIterable:
  def __init__(self, regionMapper, params={
    'SouthernmostLatitude': -90.0,
    'NorthernmostLatitude': 90.0,
    'WesternmostLongitude': -180.0,
    'EasternmostLongitude': 179.375,
    'LatitudeResolution': 0.5,
    'LongitudeResolution': 0.625,
  }, dependencies={
    'linespace': numpy.linspace
  }):

    self.latitudes = dependencies['linespace'](
      params['SouthernmostLatitude'],
      params['NorthernmostLatitude'],
      (params['NorthernmostLatitude'] - params['SouthernmostLatitude']) / params['LatitudeResolution'] + 1
    )
    self.longitudes = dependencies['linespace'](
      params['WesternmostLongitude'],
      params['EasternmostLongitude'],
      (params['EasternmostLongitude'] - params['WesternmostLongitude']) / params['LongitudeResolution'] + 1
    )
    self._regionMapper = regionMapper


  def _getExpansiveIterator(self):
    for lat in self.latitudes:
      for lon in self.longitudes:
        yield (lat, lon)

  def getIterator(self):
    for p in self._getExpansiveIterator():
      rm = self._regionMapper( p[0], p[1] )

      if rm != 0:
        yield(rm, p)
