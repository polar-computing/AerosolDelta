import sys
import os

DATA_PATH = os.environ['DATA_PATH']

from extraction.nc4_extractor import NC4Extractor
from extraction.hdf_extractor import HDFExtractor
from spatial.poi_data_struct  import PoiDataStruct

if __name__ == '__main__':
  DATA_SET_TYPE = sys.argv[1]
  IP_FILE_PATH  = sys.argv[2]

  if DATA_SET_TYPE == 'merra2':
    poiStruct = PoiDataStruct(os.path.join(DATA_PATH, "merra2-strict.csv")).generate()

    fields = [
      'BCSCATAU','BCSMASS','OCSCATAU','OCSMASS','DUSCATAU','DUSMASS',
      'SSSCATAU','SSSMASS','SUSCATAU','SO4SMASS','SO2SMASS','TOTSCATAU'
    ]

    ext = NC4Extractor(IP_FILE_PATH, ["lat", "lon"], poiStruct)

    for r in ext.iterativeExtractor(fields):
      d = [ r[0], r[1], r[2], r[3]['min'], r[3]['max'], r[3]['median'], r[3]['mean'], r[3]['std'] ]
      print ",".join(map(str, d))


  elif DATA_SET_TYPE == 'caliop':
    poiStruct = PoiDataStruct(os.path.join(DATA_PATH, "caliop-strict.csv")).generate()

    fields = [
      'AOD_Mean', 'AOD_Mean_Dust', 'AOD_Mean_Smoke', 'AOD_Mean_Polluted_Dust',
    ]

    ext = HDFExtractor(IP_FILE_PATH, ["Latitude_Midpoint", "Longitude_Midpoint"], poiStruct)

    for r in ext.iterativeExtractor(fields):
      d = [ r[0], r[1], r[2], r[3]['min'], r[3]['max'], r[3]['median'], r[3]['mean'], r[3]['std'] ]
      print ",".join(map(str, d))

