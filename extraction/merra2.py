import numpy as np
import netCDF4, sys, csv

VARIABLES_OF_INTERST = [
  'BCSCATAU','BCSMASS','OCSCATAU','OCSMASS','DUSCATAU','DUSMASS',
  'SSSCATAU','SSSMASS','SUSCATAU','SO4SMASS','SO2SMASS','TOTSCATAU'
]

STAT_METHODS = [
  'min',
  'max',
  'median',
  'mean',
  'std',
]

class Merra2Extractor:
  def __init__(self,
    merra2FilePath,
    poiPath="./data/merra2-strict.csv",
    dependencies={
      'Dataset': netCDF4.Dataset,
      'csv': csv,
      'np': np,
    }):

    self.__dependencies = dependencies

    self.dataset = self.__dependencies['Dataset'](merra2FilePath, mode='r')

    self.spatialPointsOfInterest = { }

    for p in self.__dependencies['csv'].reader(open(poiPath)):
      pt = (float(p[0]), float(p[1]))
      rg = float(p[2])

      if not rg in self.spatialPointsOfInterest:
        self.spatialPointsOfInterest[rg] = [ ]

      self.spatialPointsOfInterest[rg].append(pt)

  def extract(self, fields=VARIABLES_OF_INTERST):
    extracted = { }

    for rg in self.spatialPointsOfInterest:
      extracted[rg] = { }

      for v in VARIABLES_OF_INTERST:
        data = np.array(map(lambda pt: self.dataset.variables[v][0][pt[0]][pt[1]], self.spatialPointsOfInterest[rg]))
        extracted[rg][v] = reduce(lambda m, s: m.update({ s :  getattr(np, s)(data) }) or m, STAT_METHODS, { })

    return extract


  def __exit__(self):
    self.dataset.close()


if __name__ == '__main__':
  IP_FILE_PATH = sys.argv[1]

  extractor = Merra2Extractor(IP_FILE_PATH)
  # Do something with this
  extractor.extract()

