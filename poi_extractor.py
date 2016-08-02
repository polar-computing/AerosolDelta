# Extracts points of interest from satellite date
# Points of interest
from spatial.rgi_spatial_iterable import RGISpatialIterable
from spatial.rgi_region_mapper    import RgiSpatial


# Merra2
f = open("./data/merra2-buffer.csv", "w+")
for (region, point) in RGISpatialIterable(RgiSpatial.bufferLandIceRegionMapper).getIterator():
  f.write("{0},{1},{2}\n".format(point[0], point[1], region))

rg = RgiSpatial()
f = open("./data/merra2-strict.csv", "w+")
for (region, point) in RGISpatialIterable(rg.regionsOfInterestMapper).getIterator():
  f.write("{0},{1},{2}\n".format(point[0], point[1], region))
