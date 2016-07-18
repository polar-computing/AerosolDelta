# encoding: utf-8

# Program to read CALIOP Monthly Mean HDF-4 files. Filter data for only the region specific Lat-Lon
# Writes the data into CSV file

import numpy
import sys
import os
import pyhdf.HDF
import pyhdf.SD


goodGeoPoints = []

# Initialize the Dataset
def init(hdfFile):
    if pyhdf.HDF.ishdf(hdfFile):
        myhdf = pyhdf.SD.SD(hdfFile, pyhdf.SD.SDC.READ)
        return myhdf
    else:
        print "Trying to operate on a non-hdf filetype"


# Releasing Resources
def close(myhdf):
    myhdf.close()


# Read All Data
def getAllData(hdfFile, myhdf, outputFile):
    # Initialize all variables
    # 1-d array of lat and lon
    latitude = myhdf.select("Latitude_Midpoint")
    longitude = myhdf.select("Longitude_Midpoint")

    # Aerosol Values
    aodMean = myhdf.select("AOD_Mean")
    aodMeanDust = myhdf.select("AOD_Mean_Dust")
    aodMeanSmoke = myhdf.select("AOD_Mean_Smoke")
    aodMeanPollutedDust = myhdf.select("AOD_Mean_Polluted_Dust")

    print aodMean[0][0]
    print aodMeanDust[0][0]
    print aodMeanSmoke[0][0]
    print aodMeanPollutedDust[0][0]

    year = hdfFile.split("-")[-2][-4:]
    month = hdfFile.split("-")[-1][:2]

    print "Extracting all data..."
    with open(outputFile, 'a') as out:
        for lats,lons,region in goodGeoPoints:
            lat = int(lats)
            lon = int(lons)
            print lat,lon,region
            dataList = []
            dataList.append(str(region))
            dataList.append(str(year))
            dataList.append(str(month))
            dataList.append(str(latitude[0][lat]))
            dataList.append(str(longitude[0][lon]))
            dataList.append(str(aodMeanDust[lat][lon]))
            dataList.append(str(aodMeanSmoke[lat][lon]))
            dataList.append(str(aodMeanPollutedDust[lat][lon]))
            dataList.append(str(aodMean[lat][lon]))
            print "Adding data:"
            print ','.join(dataList)
            out.write(','.join(dataList))
            out.write("\n")
    exit()


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
        out.write("RegionId,Year,Month,Latitude,Longitude,AOD_Mean_Dust,AOD_Mean_Smoke,AOD_Mean_Polluted_Dust,AOD_Mean")
        out.write("\n")

    for root, dirs, files in os.walk(args[1], topdown=False):
        for name in files:
            if name.endswith(".hdf"):
                hdfFile = os.path.join(root, name)
                print "Processing ", hdfFile
                myhdf = init(hdfFile)
                getAllData(hdfFile, myhdf, outputFile)
                close(myhdf)


if __name__ == '__main__':
    main(sys.argv)

