import numpy as np
import pandas as pd

import sys

# Extracted CSV file generated from data extracted from HDFs
PATH = sys.argv[1]

# Aggregated by year
OP_PATH = sys.argv[2]

#df = pd.DataFrame.from_csv(PATH, index_col=False, header=0)
df = pd.read_csv(PATH, names=[
  'RegionId', 'Year', 'Month', 'Latitude', 'Longitude', 'BCSCATAU',
  'BCSMASS', 'OCSCATAU', 'OCSMASS', 'DUSCATAU', 'DUSMASS', 'SSSCATAU',
  'SSSMASS', 'SUSCATAU', 'SO4SMASS', 'SO2SMASS','TOTSCATAU'
], index_col=False, dtype = {
  'RegionId' : np.int64,
  'Year' : np.int64,
  'Month' : np.str,
  'Latitude' : np.float64,
  'Longitude' : np.float64,
  'BCSCATAU' : np.float64,
  'BCSMASS' : np.float64,
  'OCSCATAU' : np.float64,
  'OCSMASS' : np.float64,
  'DUSCATAU' : np.float64,
  'DUSMASS' : np.float64,
  'SSSCATAU' : np.float64,
  'SSSMASS' : np.float64,
  'SUSCATAU' : np.float64,
  'SO4SMASS' : np.float64,
  'SO2SMASS' : np.float64,
  'TOTSCATAU' : np.float64,
})

print "LOADED"

df['TOTALSMC'] = df['BCSMASS'] + df['OCSMASS'] + df['DUSMASS'] + df['SSSMASS'] + df['SO4SMASS'] + df['SO2SMASS']

g = df[[
  'RegionId', 'Year', 'BCSCATAU','BCSMASS', 'OCSCATAU',
  'OCSMASS', 'DUSCATAU', 'DUSMASS', 'SSSCATAU', 'SSSMASS',
  'SUSCATAU', 'SO4SMASS', 'SO2SMASS', 'TOTSCATAU','TOTALSMC'
]].groupby(['RegionId', 'Year'], as_index=False).agg([ np.min, np.max, np.sum, np.mean, np.median ])

print "AGGREGATED"

# Write aggregate to csv
g.reset_index(inplace=True, level=1, col_level=1)
g.to_csv(OP_PATH, header=True, index=True)



