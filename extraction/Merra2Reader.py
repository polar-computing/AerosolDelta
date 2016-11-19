# encoding: utf-8

# Program to read MERRA-2 Monthly Mean netCDF4 files. Currently it
# (a) reads the BCSCATAU data against each latitude and longitude and prints it.
# (b) extracts all Lat-Lon and writes it to CSV.

import netCDF4
import numpy
import sys

# Dataset Handle
dataset = netCDF4.Dataset


# Initialize the Dataset
def init(ncFile):
    global dataset
    dataset = netCDF4.Dataset(ncFile, mode='r')


# Releasing Resources
def close():
    dataset.close()


# Read BCSCATAU Data
def getBcscatauData():
    # Prints all variables in the dataset
    print dataset.variables
    print

    # 3-d array of time, lat, lon. But, the time field always remain 0
    bcscatau_dataset = dataset.variables['BCSCATAU']

    # 1-d array of lat and lon
    latitude_dataset = dataset.variables['lat']
    longitude_dataset = dataset.variables['lon']

    print longitude_dataset[10]

    # Not required here as the dataset is 2-d
    #time_dataset = dataset.variables['time']

    #print bcscatau_dataset
    #print longitude_dataset[0]
    #print latitude_dataset[0]
    #print bcscatau_dataset[0][0][0]

    for lat in xrange(0, numpy.size(bcscatau_dataset, 1)):
        for lon in xrange(0, numpy.size(bcscatau_dataset, 2)):
            if bcscatau_dataset[0][lat][lon] < 0:
                print latitude_dataset[lat], longitude_dataset[lon], bcscatau_dataset[0][lat][lon]
            #exit()


def extractLatLon(outputFile):
    # 1-d array of lat and lon
    latitude_dataset = dataset.variables['lat']
    longitude_dataset = dataset.variables['lon']

    with open(outputFile, 'w') as out:
        for lat in xrange(0, len(latitude_dataset)):
            for lon in xrange(0, len(longitude_dataset)):
                out.write(str(latitude_dataset[lat]) + "," + str(longitude_dataset[lon]) + "," + str(lat) + "," + str(lon))
                out.write("\n")


# This is where all begins. Expects .nc file (netCDF)
def main(args):
    if len(args) != 3:
        print "Wrong number of arguments!!!"
        exit(1)
    ncFile = args[1]
    outputFile = args[2]
    init(ncFile)
    getBcscatauData()
    #extractLatLon(outputFile)
    close()


if __name__ == '__main__':
    main(sys.argv)
