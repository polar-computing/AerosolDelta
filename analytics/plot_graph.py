# Program to Plot Graphs for Aerosol Delta

from os import mkdir
from os.path import join, isdir
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import argparse
import constants as C

# Use ggplot for Maps
matplotlib.style.use('ggplot')


# Argument Parser
def parse_arguments():
    # Configure
    argparser = argparse.ArgumentParser(description = 'Plot Graphs for Aerosol Delta')
    argparser.add_argument('-i', '--inFile', help='Path to the input file (CSV)', required=True)
    argparser.add_argument('-o', '--outDir', help='Path to the output directory where graphs will be stored', required=True)
    argparser.add_argument('-d', '--data', help='Data: merra2, merra2-catau, merra2-mass, caliop', required=True)
    argparser.add_argument('-op', '--operation', help='Supports - min, max, median, mean, std', required=True)
    argparser.add_argument('-r', '--regions', help='19 regions. Specify range here. 1:19 means all regions', required=True)
    argparser.add_argument('-y', '--years', help='Specify year range. 2002:2016 means from year 2002 to 2016', required=True)
    argparser.add_argument('-gb', '--groupBy', help='y: year, m: month, ym: year and month', required=True)

    # Checking for Syntactical Errors
    args = argparser.parse_args()

    # Checking for Semantic Errors
    if args.operation not in C.OPERATIONS:
        print "Not a valid operation:", args.operation
        exit(1)

    return args


# Get drop columns based on the requested data
def getDropCols(data):
    return {
        'merra2': list(),
        'caliop' : list(),
        'merra2-catau': list(C.MERRA2_MASS_ATTR),
        'merra2-mass' : list(C.MERRA2_CATAU_ATTR)
    }[data]


# Create directory if not exists
def safeMakeDir(path):
  if not isdir(path):
    mkdir(path)


def clip_list(raw, lb, ub):
    clipped = list()
    for item in raw:
        if lb <= int(item) <= ub:
            clipped.append(item)
    return clipped


# Plot Graphs
def plot(args):
    # Initializing variables
    drop_attr = getDropCols(args.data)
    region_limits = args.regions.split(':')
    year_limits = args.years.split(':')
    years = range(int(year_limits[0]), int(year_limits[1]) + 1)

    # Pre-Processing
    df_main = pd.DataFrame.from_csv(args.inFile, index_col=False)
    regions = clip_list(df_main.region.unique().tolist(), int(region_limits[0]), int(region_limits[1]))
    df_main[C.YEAR] = df_main[C.TIME].str.split('-', 1).str.get(0).astype(int)
    df_main[C.MONTH] = df_main[C.TIME].str.split('-', 1).str.get(1).astype(int)
    df_main = df_main[df_main[C.YEAR].isin(years)]
    df_main.drop(list(C.OPERATIONS - {args.operation}), axis=1, inplace=True)

    # Group By
    gb = list()
    df_index = C.YEAR
    if args.groupBy == 'ym':
        gb.append(C.TIME)
        df_main.drop(C.MONTH, axis=1, inplace=True)
        df_main.drop(C.YEAR, axis=1, inplace=True)
        df_index = C.TIME
    elif args.groupBy == 'y':
        gb.append(C.YEAR)
        df_main.drop(C.MONTH, axis=1, inplace=True)
        df_main.drop(C.TIME, axis=1, inplace=True)
    elif args.groupBy == 'm':
        gb.append(C.MONTH)
        df_main.drop(C.YEAR, axis=1, inplace=True)
        df_main.drop(C.TIME, axis=1, inplace=True)
        df_index = C.MONTH
    gb.append(C.FIELD)

    # Iterate over each region to generate a graph
    for region in regions:
        # Filter by Region
        df = df_main.copy(deep=True)
        df = df[df[C.REGION].isin([region])]
        df.drop(C.REGION, axis=1, inplace=True)

        # Group By
        df = df.groupby(gb, as_index=False)[args.operation]
        df = getattr(df, args.operation)()
        df = df.reset_index(df_index)

        # Pivoting data for Plotting the graph
        df = df.pivot(index=df_index, columns=C.FIELD, values=args.operation)

        if drop_attr:
            df.drop(drop_attr, axis=1, inplace=True)

        # Plotting the graph and saving it in a file
        safeMakeDir(join(args.outDir, str(region)))
        plt.figure()
        df[df.columns].plot(kind='bar', stacked=True)
        plt.savefig(join(args.outDir, str(region), args.operation + ".png"), dpi=200)
        plt.close('all')

        print "Graph generated for Region:", region


if __name__ == '__main__':
    args = parse_arguments()
    plot(args)