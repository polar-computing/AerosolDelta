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
  'SSSMASS', 'SUSCATAU', 'SO4SMASS', 'SO2SMASS', 'TOTSCATAU'
], index_col=False)


g = df[[
  'RegionId', 'Year', 'BCSCATAU','BCSMASS', 'OCSCATAU',
  'OCSMASS', 'DUSCATAU', 'DUSMASS', 'SSSCATAU', 'SSSMASS',
  'SUSCATAU', 'SO4SMASS', 'SO2SMASS', 'TOTSCATAU'
]].groupby(['RegionId', 'Year'], as_index=False).agg([ np.min, np.max, np.sum, np.mean, np.median ])

# Write aggregate to csv
g.unstack().to_csv(OP_PATH, header=False, index=False, index_label=False)



