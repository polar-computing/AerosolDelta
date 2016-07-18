# This python file reads a set of latitude and longitudes from an input CSV file
# and iteratively maps each coordinate to a region of interest

# It writes those spatial coordinates into an output CSV file which belong to
# one of the regions of interest

from shapely import geometry
import csv
from multiprocessing import Pool
from util.region_mapper import regionMapper
import sys

INPUT_FILE = sys.argv[1]
OP_FILE    = sys.argv[2]

reader = csv.reader(open(INPUT_FILE), delimiter=',')
op     = open(OP_FILE, "w+")

for row in reader:
  pt = geometry.Point( float(row[0]), float(row[1]) )
  r = regionMapper(pt)
  if r!=0:
    op.write("{0},{1},{2}\n".format(row[0], row[1], r))
