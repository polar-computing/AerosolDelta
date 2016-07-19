import numpy as np
import pandas as pd

import sys

# Extracted CSV file generated from data extracted from HDFs
PATH = sys.argv[1]

# Aggregated by year
OP_PATH = sys.argv[2]

df = pd.read_csv(PATH, names=[
  'RegionId','Year','Month','Latitude','Longitude','AOD_Mean_Dust',
  'AOD_Mean_Smoke','AOD_Mean_Polluted_Dust','AOD_Mean',
], index_col=False)

df = df.applymap(lambda x: np.nan if x == -9999.0 else x)

g = df[[
  'RegionId', 'Year', 'AOD_Mean_Dust',
  'AOD_Mean_Smoke','AOD_Mean_Polluted_Dust','AOD_Mean'
]].groupby(['RegionId', 'Year'], as_index=False).agg([ np.min, np.max, np.sum, np.mean, np.median ])


# Write aggregate to csv
g.reset_index(inplace=True, level=1, col_level=1)
g.to_csv(OP_PATH, header=True, index=True)
