# encoding: utf-8

# Process data to plot the difference map

import sys
import numpy as np
import pandas as pd

caliop = None

def getMerra2Range(lat, lon):
    latUb = lat + 1
    latLb = lat - 0.9
    lonUb = lon + 2.5
    lonLb = lon - 2.4
    return (latUb, latLb, lonUb, lonLb)


#TODO: Use this later to improve performance
def filterGrp(row):
    global caliop
    #print "Processing row of Merra2"
    try:
        X, Y = row['Latitude'], row['Longitude']
        caliop['DIS'] = (caliop.Latitude - X) * (caliop.Latitude - X) + (caliop.Longitude - Y) * (caliop.Longitude - Y)
        temp = caliop.ix[caliop.DIS.idxmin()]
        return temp['index']  # print temp[2]
    except:
        pass

def processData(merra2File, caliopFile, outputFile):
    global caliop
    positive = []
    negative = []
    gray = []

    print "Loading CALIOP Data..."

    caliop = pd.read_csv(caliopFile, names=[
        'RegionId', 'Year', 'Month', 'Latitude', 'Longitude', 'AOD_Mean_Dust',
        'AOD_Mean_Smoke', 'AOD_Mean_Polluted_Dust', 'AOD_Mean',
    ], index_col=False, dtype={
        'RegionId': np.int64,
        'Year': np.int64,
        'Month': np.str,
        'Latitude': np.float64,
        'Longitude': np.float64,
        'AOD_Mean_Dust': np.float64,
        'AOD_Mean_Smoke': np.float64,
        'AOD_Mean_Polluted_Dust': np.float64,
        'AOD_Mean': np.float64,
    })

    print "CALIOP Data Loaded"

    print "Filtering data based on year and month"
    caliopData = caliop.query('Year == 2010 and Month == "06" and AOD_Mean_Dust != -9999.0')

    # If needed for 5 years
    #caliopData = caliop.query('Year >= 2007 and Year <= 2011 and AOD_Mean_Dust != -9999.0').groupby(['Latitude', 'Longitude'])['AOD_Mean_Dust'].mean()

    print caliopData

    print "Loading MERRA-2 Data..."

    merra2 = pd.read_csv(merra2File, names=[
        'RegionId', 'Year', 'Month', 'Latitude', 'Longitude', 'BCSCATAU',
        'BCSMASS', 'OCSCATAU', 'OCSMASS', 'DUSCATAU', 'DUSMASS', 'SSSCATAU',
        'SSSMASS', 'SUSCATAU', 'SO4SMASS', 'SO2SMASS', 'TOTSCATAU'
    ], index_col=False, dtype={
        'RegionId': np.int64,
        'Year': np.int64,
        'Month': np.str,
        'Latitude': np.float64,
        'Longitude': np.float64,
        'BCSCATAU': np.float64,
        'BCSMASS': np.float64,
        'OCSCATAU': np.float64,
        'OCSMASS': np.float64,
        'DUSCATAU': np.float64,
        'DUSMASS': np.float64,
        'SSSCATAU': np.float64,
        'SSSMASS': np.float64,
        'SUSCATAU': np.float64,
        'SO4SMASS': np.float64,
        'SO2SMASS': np.float64,
        'TOTSCATAU': np.float64,
    })

    print "MERRA-2 Data Loaded"

    print "Filtering data based on year and month"
    merra2Filtered = merra2.query('Year == 2010 and Month == "06" and DUSCATAU != -9999.0')

    # If needed for 5 years
    #merra2Filtered = merra2.query('Year >= 2007 and Year <= 2011 and DUSCATAU != -9999.0').groupby(['Latitude', 'Longitude'])['DUSCATAU'].mean()

    #merra2Data['grpId'] = merra2Data.apply(filterGrp, axis=1)
    #print merra2Data['grpId']
    print "Processed MERRA-2"

    print "Iterating over CALIOP Data and mapping it with MERRA-2 Data"
    for index,row in caliopData.iterrows():

        (latUp, latLb, lonUb, lonLb) = getMerra2Range(row["Latitude"], row["Longitude"])

        print "Query MERRA-2 Data for Latitude - Longitude Range"
        merra2Data = merra2Filtered.query(
            'DUSCATAU != -9999.0 and Latitude <= ' + str(latUp) + ' and Latitude >= ' + str(
                latLb) + ' and Longitude <= ' + str(lonUb) + ' and Longitude >= ' + str(lonLb))

        print "MERRA-2 Query Completed"

        if merra2Data.empty:
            gray.append('[' + str(row["Latitude"]) + ',' + str(row["Longitude"]) + ']')
            continue

        print "Perform Operation(s)"
        merra2DustMean = merra2Data["DUSCATAU"].mean()
        dust = row["AOD_Mean_Dust"] - merra2DustMean

        if row["AOD_Mean_Dust"] == 0.0 or merra2DustMean == 0.0:
            gray.append('[' + str(row["Latitude"]) + ',' + str(row["Longitude"]) + ']')
        elif dust < 0.0:
            negative.append('[' + str(row["Latitude"]) + ',' + str(row["Longitude"]) + ',' + str(dust) + ']')
        else:
            positive.append('[' + str(row["Latitude"]) + ',' + str(row["Longitude"]) + ',' + str(dust) + ']')

        #print row["Latitude"], row["Longitude"]
        #print "Caliop Dust Mean", row["AOD_Mean_Dust"]
        #print "Merra2 Dust Mean", merra2DustMean
        #print row["Latitude"], row["Longitude"], dust

        print "Operation Performed"

    print "Writing Data"
    with open(outputFile, 'a') as out:
        out.write('var positive = [' + ",\n".join(positive) + '];\n')
        out.write('var negative = [' + ",\n".join(negative) + '];\n')
        out.write('var gray = [' + ",\n".join(gray) + '];\n')
    print "Writing Completed"


# This is where all begins. Expects .nc file (netCDF)
def main(args):
    merra2File = args[1]
    caliopFile = args[2]
    outputFile = args[3]

    processData(merra2File, caliopFile, outputFile)



if __name__ == '__main__':
    main(sys.argv)
