# Aerosols over Cryosphere
Quantifying aerosol presence and composition over Earth's ice sheets and glaciers - mapping anthropogenic and natural aerosol patters and estimating changes over time

# Description
Many of Earth’s glaciers have been losing mass at an alarming rate in the past few decades. Both anthropogenic and natural aerosols deposited on snow and ice can darken reflective surfaces, increase solar absorption and subsequently enhance snow and ice melt rates. This project seeks to map aerosols over Earth's cryosphere using the global land ice identification mask and monthly mean MERRA-2 aerosol data. Ideally, the project will be completed for all of Earth, mapping aerosol concentrations, with seasonal and annual totals from 1980-present. If time/space limits us, the project can be reduced geographically (e.g. Arctic or Himalaya) and temporally (2000-present).

# Input data:
Randolph Glacier Inventory [data](http://www.glims.org/RGI/rgi50_dl.html), RGI 5.0, delineates the spatial extent of Earth’s glaciers.
Data format = SHP shapefile, vector format. 
File size: whole inventory 410 mb zipped, 739 MB unzipped, 125 files, organized by 19 regions.

MERRA-2 aerosol raster modeled [data](http://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/data_access/). Required input data consists of monthly mean dust, organic carbon, black carbon, sea salt and sulfate aerosol concentrations.
To get the data, visit [DISC data ordering site](http://disc.sci.gsfc.nasa.gov/uui/datasets?keywords=%22MERRA-2%22) or [Direct download](ftp://goldsmr4.sci.gsfc.nasa.gov/data/s4pa/)
More info can be found in this [pdf](http://gmao.gsfc.nasa.gov/pubs/docs/Bosilovich785.pdf)
Data format = NetCDF-4.  File sizes ~3-155 MB per monthly mean file.

CALIOP aerosol raster observation Version 3 [Aerosol Profile data](https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l3_apro_cloudfree-standard-V3-00)
Monthly global gridded data, nighttime aerosol extinction profiles, cloud-free. CAL_LID_L3_APro_CloudFree_Standard-V3-00   Available from 2006-present, between latitudes of 82 degrees North to 82 degrees South.    Sun synchronous orbit, equator crossing time of 2 pm, 16-day orbit repeat cycle.
Observations are to be compared with modeled aerosol results.
To get data, visit [ASDC HTML Order Tool](https://eosweb.larc.nasa.gov/HORDERBIN/HTML_Start.cgi)
Data format = HDF.  File size ~

MODIS, Aqua, Collection 6, 8-day surface reflectance raster data, to be collected coinciding with season or year corresponding to aerosol data.
To learn more and access data: [LPDAAC website data ordering]
(https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/myd09a1)
or [Online list of data](http://e4ftl01.cr.usgs.gov/MOLA/MYD09A1.006/)
Data format = HDF.   
File size ~80 MB per tile all 7 spectral bands, one tile. 460 tiles to cover Earth (see [MODIS Grid](http://modis-land.gsfc.nasa.gov/MODLAND_grid.html)), tiles are 10 degrees by 10 degrees at the equator.

Landsat data to be used for smaller mountain, peninsula, coastal glaciers.  Reflectance data will be collected to coincide with measured aerosol season or year (e.g. spring or annual).
Landsat, raster, surface reflectance data
To learn more and access data: [Landsat website](http://landsat.usgs.gov/CDR_LSR.php)
File size ~2.5 GB per Landsat scene, all 7 spectral bands, 190 km x 180 km area per file.
Data format = GeoTIFF.


# Tools
Potential tools/languages to be used: Python, QGIS, matlab, idl, ArcGIS, ENVI/IDL

