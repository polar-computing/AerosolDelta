import pyhdf.HDF
import pyhdf.SD
import numpy as np
import pandas as pd

class HDFExtractor:
  def __init__(self,
    filePath,
    geoKeys,
    poiData,
    dependencies={
      'pyhdf.HDF': pyhdf.HDF,
      'pyhdf.SD': pyhdf.SD,
      'np': np,
      'pd': pd,
    }):
    self.spatialPointsOfInterest = poiData
    self.__dependencies = dependencies

    self.dataset = pyhdf.SD.SD(filePath, pyhdf.SD.SDC.READ)

    self.latitude  = self.dataset.select(geoKeys[0])[0]
    self.longitude = self.dataset.select(geoKeys[1])[0]

    # TODO FIX THIS - READ DATES FROM HDF METADATA
    # self.dataset.attributes()['coremetadata']
    self.year  = int(filePath.split("-")[-2][-4:] )
    self.month = int(filePath.split("-")[-1][:2]  )

    self.time = str(self.year) + "-" + str(self.month)

  def iterativeExtractor(self, fields, STAT_METHODS):
    for rg in self.spatialPointsOfInterest:
      geo = { }

      for lt in self.spatialPointsOfInterest[rg]:
        points = len(self.spatialPointsOfInterest[rg][lt])
        lon_bnds = [ self.spatialPointsOfInterest[rg][lt][0][1], self.spatialPointsOfInterest[rg][lt][points - 1][1] + 0.001 ]

        lat_idx  = np.where((self.latitude == lt))[ 0 ] if lt != 0 else np.array([180])
        lon_inds = np.where((self.longitude >= lon_bnds[0]) & (self.longitude < lon_bnds[1]))

        geo[str(lt)] = lon_inds[0]

      for v in fields:
        data = reduce(lambda data, lt: np.concatenate([ data, self.dataset.select(v)[int(float(lt))][geo[lt]] ]), geo, np.array([], dtype=np.float64))
        summary = reduce(lambda m, s: m.update({ s :  getattr(np, s)(data) }) or m, STAT_METHODS, { })

        yield(self.time, rg, v, summary)

  def extract(self, fields, STAT_METHODS):
    df = pd.DataFrame(columns=['time', 'region', 'field', 'min','max','median','mean','std'], index=[ ])

    for i, r in enumerate(self.iterativeExtractor(fields, STAT_METHODS)):
      df.loc[i] = [ r[0], r[1], r[2], r[3]['min'], r[3]['max'], r[3]['median'], r[3]['mean'], r[3]['std']]

    return df

  def __exit__(self):
    self.dataset.close()
