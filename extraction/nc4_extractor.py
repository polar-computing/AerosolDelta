import numpy as np
import pandas as pd
import netCDF4, sys
from dateutil.parser import parse

STAT_METHODS = [
  'min',
  'max',
  'median',
  'mean',
  'std',
]

class NC4Extractor:
  def __init__(self,
    merra2FilePath,
    poiData,
    dependencies={
      'Dataset': netCDF4.Dataset,
      'np': np,
      'pd': pd,
      'dateParser': parse
    }):
    self.spatialPointsOfInterest = poiData
    self.__dependencies = dependencies
    self.dataset = self.__dependencies['Dataset'](merra2FilePath, mode='r')

    parsed = self.__dependencies['dateParser'](self.dataset.RangeBeginningDate)
    self.month = parsed.month
    self.year  = parsed.year

    self.time = str(self.year) + "-" + str(self.month)

  def iterativeExtractor(self, fields):
    # NOTE: Time index is hardcoded
    for rg in self.spatialPointsOfInterest:
      for v in fields:
        data = np.array(map(lambda pt: self.dataset.variables[v][0][pt[0]][pt[1]], self.spatialPointsOfInterest[rg]), dtype=np.float64)
        summary = reduce(lambda m, s: m.update({ s :  getattr(np, s)(data) }) or m, STAT_METHODS, { })

        yield(self.time, rg, v, summary)


  def extract(self, fields):
    df = pd.DataFrame(columns=['time', 'region', 'field', 'min','max','median','mean','std'], index=[ ])

    for i, r in enumerate(self.iterativeExtractor(fields)):
      df.loc[i] = [ r[0], r[1], r[2], r[3]['min'], r[3]['max'], r[3]['median'], r[3]['mean'], r[3]['std']]

    return df


  def __exit__(self):
    self.dataset.close()
