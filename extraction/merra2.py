import netCDF4
import sys
import pdb

VARIABLES_OF_INTERST = [
  'BCSCATAU','BCSMASS','OCSCATAU','OCSMASS','DUSCATAU','DUSMASS',
  'SSSCATAU','SSSMASS','SUSCATAU','SO4SMASS','SO2SMASS','TOTSCATAU'
]

class Merra2Extractor:
  def __init__(self,
    merra2FilePath,
    poiPath="./data/merra2-strict.csv",
    dependencies={ 'Dataset': netCDF4.Dataset }):

    self.__dependencies = dependencies

    self.dataset = self.__dependencies['Dataset'](merra2FilePath, mode='r')

  def extract(self, fields=VARIABLES_OF_INTERST):
    pdb.set_trace()

  def __exit__(self):
    self.dataset.close()


if __name__ == '__main__':
  IP_FILE_PATH = sys.argv[1]

  extractor = Merra2Extractor(IP_FILE_PATH)
  extractor.extract()

