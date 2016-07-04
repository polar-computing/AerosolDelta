# encoding: utf-8

# Program to parse MERRA-2 M2TMNXAER.5.12.4 files and index it to ElasticSearch instance.

# Author: Karanjeet Singh

import netCDF4
import numpy
import sys
from elasticsearch import Elasticsearch


# Global Constants
ELASTIC_SEARCH_HOST = 'localhost'
ELASTIC_SEARCH_PORT = 9200
ELASTIC_SEARCH_INDEX = 'aerosol'
ELASTIC_SEARCH_INDEX_TYPE = 'merra2'

# Handle
dataset = netCDF4.Dataset
es = Elasticsearch


# Initialize the Dataset
def init(ncFile):
    global dataset, es
    dataset = netCDF4.Dataset(ncFile, mode='r')
    es = Elasticsearch([{'host': ELASTIC_SEARCH_HOST, 'port': ELASTIC_SEARCH_PORT}])


# Releasing Resources
def close():
    dataset.close()


# Parse Dataset and returns JSON data
def parseAndIndex():
    print dataset.variables

    # Output
    out_json = {}
    id = 1

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

    for lat in xrange(0, numpy.size(latitude, 0)):
        for lon in xrange(0, numpy.size(longitude, 0)):
            #print bcscatau[0][lat][lon]
            out_json["latitude"] = latitude[lat]
            out_json["longitude"] = longitude[lon]
            out_json["BCSCATAU"] = bcscatau[0][lat][lon].item()
            out_json["BCSMASS"] = bcsmass[0][lat][lon].item()
            out_json["OCSCATAU"] = ocscatau[0][lat][lon].item()
            out_json["OCSMASS"] = ocsmass[0][lat][lon].item()
            out_json["DUSCATAU"] = duscatau[0][lat][lon].item()
            out_json["DUSMASS"] = dusmass[0][lat][lon].item()
            out_json["SSSCATAU"] = ssscatau[0][lat][lon].item()
            out_json["SSSMASS"] = sssmass[0][lat][lon].item()
            out_json["SUSCATAU"] = suscatau[0][lat][lon].item()
            out_json["SO4SMASS"] = so4smass[0][lat][lon].item()
            out_json["SO2SMASS"] = so2smass[0][lat][lon].item()
            out_json["TOTSCATAU"] = totscatau[0][lat][lon].item()
            print out_json
            es.index(index=ELASTIC_SEARCH_INDEX, doc_type=ELASTIC_SEARCH_INDEX_TYPE, id=id,
                     body=out_json)
            id += 1


# TODO:Add bulk indexing of data in Elastic Search
def index():
    pass


# This is where it all begins
def main(args):
    if len(args) != 2:
        print "Wrong number of arguments!!!"
        exit(1)
    ncFile = args[1]
    init(ncFile)
    parseAndIndex()
    close()

if __name__ == '__main__':
    main(sys.argv)