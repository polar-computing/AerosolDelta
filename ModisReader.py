# encoding: utf-8

# Program to read MODIS MYD09A1 HDF4 files. It expects the files to be in netCDF format.
# Therefore, we have used HDF4 CF CONVERSION TOOLKIT (http://hdfeos.org/software/h4cflib.php) for the
# same.

# Author: Karanjeet Singh (karanjeets)

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


# Takes the Surface Reflectance value and returns the Aerosol Quantity
def getAerosolQty(value):
    binary = format(value, '016b')
    aerosol_qty = binary[6:8]
    if aerosol_qty == "00":
        return "climatology"
    elif aerosol_qty == "01":
        return "low"
    elif aerosol_qty == "10":
        return "average"
    elif aerosol_qty == "11":
        return "high"
    else:
        print "Incorrect value: ", aerosol_qty
        exit(1)


# Read Aerosol Data
def getAerosol():
    aerosol_dataset = dataset.variables['sur_refl_state_500m']
    latitude_dataset = dataset.variables['latitude']
    longitude_dataset = dataset.variables['longitude']
    for row in xrange(0, numpy.size(aerosol_dataset, 0)):
        for col in xrange(0, numpy.size(aerosol_dataset, 1)):
            #print value
            print latitude_dataset[row][col], longitude_dataset[row][col], getAerosolQty(aerosol_dataset[row].data[col])


# This is where all begins. Expects .nc file (netCDF)
def main(args):
    if len(args) != 2:
        print "Wrong number of arguments!!!"
        exit(1)
    ncFile = args[1]
    init(ncFile)
    getAerosol()
    close()


if __name__ == '__main__':
    main(sys.argv)
