import sys, pdb, csv
import pylab as pl
from os import listdir, mkdir
from os.path import isfile, join, isdir
import itertools
import matplotlib.pyplot as plt

import matplotlib
matplotlib.style.use('ggplot')

# PATH to the filtered CSV
PATH = sys.argv[1]
OP_PATH = sys.argv[2]

reader = csv.reader(open(PATH))

# Skip the first 3 lines [ Find a better way to do this ]
reader.next()
reader.next()
reader.next()


YEARS = map(str, range(2006, 2017))
REGIONS = map(str, range(1, 14))
DATA = { }

# Initializing DICT
for r in REGIONS:
  DATA[r] = { }
  for y in YEARS:
    DATA[r][y] = [ ]

COLUMNS = ['AOD_Mean_Dust','AOD_Mean_Smoke','AOD_Mean_Polluted_Dust','AOD_Mean']
PCOLUMNS = ['AOD_Mean_Dust','AOD_Mean_Smoke','AOD_Mean_Polluted_Dust','AOD_Mean']
OPERATIONS = ['min', 'max', 'sum', 'mean', 'median']

FIELDS = map(lambda c: c[0] + '-' + c[1],itertools.product(COLUMNS, OPERATIONS))

for row in reader:
  DATA[row[0]][row[1]] = {}

  for f in range(len(FIELDS)):
    DATA[row[0]][row[1]][FIELDS[f]] = row[f+2]

def safeMakeDir(path):
  if not isdir(path):
    mkdir(path)

def plotGraph(region, operation):
  getVals = lambda column: map(lambda y: DATA[region][y][column + "-" + operation], DATA[region])
  handles = map(lambda c: plt.plot(map(int, YEARS), getVals(c), label=c), PCOLUMNS)

  plt.legend(PCOLUMNS)
  plt.title("Region : {0} - {1}".format(region, operation))
  plt.plot(handles=handles)
  plt.savefig(join(OP_PATH, region, operation + ".png"), dpi=200)
  plt.close('all')

for r in REGIONS:
  safeMakeDir(join(OP_PATH, r))

  for o in OPERATIONS:
    plotGraph(r, o)








