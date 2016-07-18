# encoding: utf-8

# Program to read MERRA-2 Monthly Mean netCDF4 files. Filter data for only the region specific Lat-Lon
# Writes the data into CSV file

# Author: Karanjeet Singh (karanjeets)

import netCDF4
import numpy
import sys
import os

# Dataset Handle
dataset = netCDF4.Dataset

goodGeoPoints = []

# Initialize the Dataset
def init(ncFile):
    global dataset
    dataset = netCDF4.Dataset(ncFile, mode='r')


# Releasing Resources
def close():
    dataset.close()


# Read All Data
def getAllData(ncFile, outputFile):
    # Initialize all variables
    # 1-d array of lat and lon
    latitude = dataset.variables['lat']
    longitude = dataset.variables['lon']

    # Bands
    bcscatau = dataset.variables['BCSCATAU']
    bcsmass = dataset.variables['BCSMASS']
    ocscatau = dataset.variables['OCSCATAU']
    ocsmass = dataset.variables['OCSMASS']
    duscatau = dataset.variables['DUSCATAU']
    dusmass = dataset.variables['DUSMASS']
    ssscatau = dataset.variables['SSSCATAU']
    sssmass = dataset.variables['SSSMASS']
    suscatau = dataset.variables['SUSCATAU']
    so4smass = dataset.variables['SO4SMASS']
    so2smass = dataset.variables['SO2SMASS']
    totscatau = dataset.variables['TOTSCATAU']

    year = ncFile.split(".")[-2][:4]
    month = ncFile.split(".")[-2][4:6]

    print "Extracting all data..."
    with open(outputFile, 'a') as out:
        for lats,lons,region in goodGeoPoints:
            lat = int(lats)
            lon = int(lons)
            #print lat,lon,region
            dataList = []
            dataList.append(str(region))
            dataList.append(str(year))
            dataList.append(str(month))
            dataList.append(str(latitude[lat]))
            dataList.append(str(longitude[lon]))
            dataList.append(str(bcscatau[0][lat][lon].item()))
            dataList.append(str(bcsmass[0][lat][lon].item()))
            dataList.append(str(ocscatau[0][lat][lon].item()))
            dataList.append(str(ocsmass[0][lat][lon].item()))
            dataList.append(str(duscatau[0][lat][lon].item()))
            dataList.append(str(dusmass[0][lat][lon].item()))
            dataList.append(str(ssscatau[0][lat][lon].item()))
            dataList.append(str(sssmass[0][lat][lon].item()))
            dataList.append(str(suscatau[0][lat][lon].item()))
            dataList.append(str(so4smass[0][lat][lon].item()))
            dataList.append(str(so2smass[0][lat][lon].item()))
            dataList.append(str(totscatau[0][lat][lon].item()))
            #print "Adding data:"
            #print ','.join(dataList)
            out.write(','.join(dataList))
            out.write("\n")


# This is where all begins. Expects .nc file (netCDF)
def main(args):
    if len(args) != 4:
        print "Wrong number of arguments!!!"
        exit(1)

    outputFile = args[2]
    maskFile = args[3]

    print "Loading all Region specific Lat-Lon"
    for line in open(maskFile, 'r'):
        csv = line.split(",")
        t = tuple()
        t = (csv[2].strip(), csv[3].strip(), csv[4].strip())
        goodGeoPoints.append(t)

    print "Loaded"

    with open(outputFile, 'w') as out:
        out.write("RegionId,Year,Month,Latitude,Longitude,BCSCATAU,BCSMASS,OCSCATAU,OCSMASS,DUSCATAU,DUSMASS,SSSCATAU,SSSMASS,SUSCATAU,SO4SMASS,SO2SMASS,TOTSCATAU")
        out.write("\n")

    #for root, dirs, files in os.walk(args[1], topdown=False):
    #    for name in files:
    #        if name.endswith(".nc4"):
    #            ncFile = os.path.join(root, name)
    #            print "Processing ", ncFile
    #            init(ncFile)
    #            getAllData(ncFile, outputFile)
    #            close()
    name=args[1]
    if name.endswith(".nc4"):
        ncFile = name
        print "Processing ", ncFile
        init(ncFile)
        getAllData(ncFile, outputFile)
        close()
    print "Process Completed"


if __name__ == '__main__':
    main(sys.argv)
