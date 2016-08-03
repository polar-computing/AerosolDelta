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

rg = RgiSpatial(
  resolution=[0.5, 0.625],
  rgiPath=os.path.join(DATA_PATH, "rgi-coords.csv"),
  countryBoundryPath=os.path.join(DATA_PATH, "country-boundries.json"))

if __name__ == '__main__':
  DATA_SET_TYPE = sys.argv[1]

  if DATA_SET_TYPE == 'merra2':
    f = open(os.path.join(DATA_PATH, "merra2-buffer.csv"), "w+")
    for (region, point) in RGISpatialIterable(RgiSpatial.bufferLandIceRegionMapper, merra2Params).getIterator():
      f.write("{0},{1},{2}\n".format(point[0], point[1], region))

    f = open(os.path.join(DATA_PATH, "merra2-strict.csv"), "w+")
    for (region, point) in RGISpatialIterable(rg.regionsOfInterestMapper, merra2Params).getIterator():
      f.write("{0},{1},{2}\n".format(point[0], point[1], region))
