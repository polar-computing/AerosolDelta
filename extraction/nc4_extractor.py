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
    filePath,
    geoKeys,
    poiData,
    dependencies={
      'Dataset': netCDF4.Dataset,
      'np': np,
      'pd': pd,
      'dateParser': parse
    }):
    self.spatialPointsOfInterest = poiData
    self.__dependencies = dependencies
    self.dataset = self.__dependencies['Dataset'](filePath, mode='r')

    self.latitude  = self.dataset.variables[geoKeys[0]][:]
    self.longitude = self.dataset.variables[geoKeys[1]][:]

    parsed = self.__dependencies['dateParser'](self.dataset.RangeBeginningDate)
    self.month = parsed.month
    self.year  = parsed.year

    self.time = str(self.year) + "-" + str(self.month)

  def iterativeExtractor(self, fields):
    # NOTE: Time index is hardcoded
    for rg in self.spatialPointsOfInterest:
      geo = { }

      for lt in self.spatialPointsOfInterest[rg]:
        points = len(self.spatialPointsOfInterest[rg][lt])
        lon_bnds = [ self.spatialPointsOfInterest[rg][lt][0][1], self.spatialPointsOfInterest[rg][lt][points - 1][1] + 0.001 ]

        lat_idx  = np.where((self.latitude == lt))[ 0 ] if lt != 0 else np.array([180])
        lon_inds = np.where((self.longitude >= lon_bnds[0]) & (self.longitude < lon_bnds[1]))

        geo[str(lat_idx[0])] = lon_inds[0]

      for v in fields:
        data = reduce(lambda data, lt: np.concatenate([ data, self.dataset.variables[v][0][float(lt)][geo[lt]] ]), geo, np.array([], dtype=np.float64))
        summary = reduce(lambda m, s: m.update({ s :  getattr(np, s)(data) }) or m, STAT_METHODS, { })

        yield(self.time, rg, v, summary)


  def extract(self, fields):
    df = pd.DataFrame(columns=['time', 'region', 'field', 'min','max','median','mean','std'], index=[ ])

    for i, r in enumerate(self.iterativeExtractor(fields)):
      df.loc[i] = [ r[0], r[1], r[2], r[3]['min'], r[3]['max'], r[3]['median'], r[3]['mean'], r[3]['std']]

    return df


  def __exit__(self):
    self.dataset.close()
