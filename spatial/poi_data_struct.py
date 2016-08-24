import csv

# POI -> points of interest
# Reads extracted poi from file and returns POIs by region in a hash

class PoiDataStruct:
  def __init__(self, poiPath, dependencies={ 'csv': csv }):
    self.poiPath = poiPath
    self.__dependencies = dependencies

  def generate(self):
    poi = { }

    for p in self.__dependencies['csv'].reader(open(self.poiPath)):
      pt = (float(p[0]), float(p[1]))
      rg = float(p[2])

      if not rg in poi:
        poi[rg] = { }

      if not pt[0] in poi[rg]:
        poi[rg][pt[0]] = [ ]

      poi[rg][pt[0]].append(pt)

    for rg in poi:
      for lt in poi[rg]:
        poi[rg][lt] = sorted(poi[rg][lt], key=lambda pt: pt[1])

    return poi
