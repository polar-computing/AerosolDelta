# Aerosols over Cryosphere
Quantifying aerosol presence and composition over Earth's ice sheets and glaciers - mapping anthropogenic and natural aerosol patters and estimating changes over time

# Description
Many of Earth’s glaciers have been losing mass at an alarming rate in the past few decades. Both anthropogenic and natural aerosols deposited on snow and ice can darken reflective surfaces, increase solar absorption and subsequently enhance snow and ice melt rates. This project seeks to map aerosols over Earth's cryosphere using the global land ice identification mask and monthly mean MERRA-2 aerosol data. Ideally, the project will be completed for all of Earth, mapping aerosol concentrations, with seasonal and annual totals from 1980-present. If time/space limits us, the project can be reduced geographically (e.g. Arctic or Himalaya) and temporally (2000-present).

# Input data:
[**Randolph Glacier Inventory Data**](http://www.glims.org/RGI/rgi50_dl.html), RGI 5.0, delineates the spatial extent of Earth’s glaciers.
Data format = SHP shapefile, vector format. 
File size: whole inventory 410 mb zipped, 739 MB unzipped, 125 files, organized by 19 regions.

- 01_Alaska
- 02_WesternCanadaUS
- 03_ArcticCanadaNorth
- 04_ArcticCanadaSouth
- 05_GreenlandPeriphery
- 06_Iceland
- 07_Svalbard
- 08_Scandinavia
- 09_RussianArctic
- 10_NorthAsia
- 11_CentralEurope
- 12_CaucasusMiddleEast
- 13_CentralAsia
- 14_SouthAsiaWest
- 15_SouthAsiaEast
- 16_LowLatitudes
- 17_SouthernAndes
- 18_NewZealand
- 19_AntarcticSubantarctic

[**MERRA-2 Aerosol Raster Modeled Data**](http://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/data_access/). Required input data, filename M2TMNXAER.5.12.4, consists of monthly mean dust, organic carbon, black carbon, sea salt and sulfate aerosol surface mass concentration and scattering aerosol optical thickness (AOT). 

Scientific data set (SDS) or bands are: 

- BCSCATAU - Black Carbon Scattering AOT (550 nm)
- BCSMASS - Black Carbon Surface Mass Concentration
- OCSCATAU - Organic Carbon Scattering AOT (550 nm)
- OCSMASS - Organic Carbon Surface Mass Concentration (Particulate Matter)
- DUSCATAU - Dust Scattering AOT (550 nm)
- DUSMASS - Dust Surface Mass Concentration
- SSSCATAU - Sea Salt Scattering AOT (550 nm)
- SSSMASS - Sea Salt Surface Mass Concentration
- SUSCATAU - SO4 Scattering AOT (550 nm)
- SO4SMASS - SO4 Surface Mass Concentration
- SO2SMASS - SO2 Surface Mass Concentration
- TOTSCATAU - Total Aerosol Scattering AOT (550 nm)

MERRA-2 monthly surface albedo is available from filename M2TMNXRAD.5.12.4, SDS:
 - ALBEDO - surface albedo


To get the data, visit [DISC data ordering site](http://disc.sci.gsfc.nasa.gov/uui/datasets?keywords=%22MERRA-2%22) or Direct download via ftp://goldsmr4.sci.gsfc.nasa.gov/data/s4pa/.  
More info can be found in this [pdf](http://gmao.gsfc.nasa.gov/pubs/docs/Bosilovich785.pdf).  

MERRA-2 data has a resolution of 0.625 degrees (longitude) (576 grid points) by 0.5 degrees (latitude) (361 grid points) or approximately 50km spatial resolution.
Data format = NetCDF-4.  File sizes ~3-155 MB per monthly mean file.

[**CALIOP aerosol raster observation Version 3, Level 3 Aerosol Profile, Cloud Free data**](https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l3_apro_cloudfree-standard-V3-00)
Monthly global gridded data, nighttime aerosol extinction profiles, cloud-free. Filename is "CAL_LID_L3_APro_CloudFree_Standard-V3-00.hdf"   Available from 2006-present, between latitudes of 85 degrees North to 85 degrees South.    Sun synchronous orbit, equator crossing time of 2 pm, 16-day orbit repeat cycle.  Spatial resolution 2 degrees in latitude, 5 degrees in longitude. 
Observations are to be compared with modeled MERRA-2 aerosol results.
To get data, visit [ASDC HTML Order Tool](https://eosweb.larc.nasa.gov/HORDERBIN/HTML_Start.cgi) /  [CALIPSO Data Products Catalog](http://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev3x8.pdf)  /  [CALIPSO Data User's Guide](http://www-calipso.larc.nasa.gov/resources/calipso_users_guide/)
Data format = HDF.  File size ~180 MB.

Scientific data set (SDS) or bands are: 

-  Longitude_Midpoint
-  Latitude_Midpoint
-  AOD_Mean_Dust
-  AOD_Mean_Smoke
-  AOD_Mean_Polluted_Dust
-  AOD_Mean

**MODIS, Aqua, Collection 6, 8-day surface reflectance raster data**, to be collected coinciding with season or year corresponding to aerosol data. To learn more and access data: [LPDAAC website data ordering]
(https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/myd09a1)
or [Online list of data](http://e4ftl01.cr.usgs.gov/MOLA/MYD09A1.006/)
Data format = HDF.    
File size ~20-80 MB per tile. 460 tiles to cover Earth (see [MODIS Grid](http://modis-land.gsfc.nasa.gov/MODLAND_grid.html)),[MODIS Metadata](https://lpdaac.usgs.gov/dataset_discovery/modis)  tiles are 10 degrees by 10 degrees at the equator.

Scientific data set (SDS) or bands are: 

- Surface reflectance for band 1
- Surface reflectance for band 2
- Surface reflectance for band 3
- Surface reflectance for band 4
- Surface reflectance for band 5
- Surface reflectance for band 6
- Surface reflectance for band 7
- Surface reflectance 500m quality control flags
- Solar zenith
- View zenith
- Relative azimuth
- Surface reflectance 500m state flags
- Surface reflectance day of year

**Landsat Data** to be used for smaller mountain, peninsula, coastal glaciers.  Reflectance data will be collected to coincide with measured aerosol season or year (e.g. spring or annual).
Landsat, raster, surface reflectance data
To learn more and access data: [Landsat website](http://landsat.usgs.gov/CDR_LSR.php)
File size ~2.5 GB per Landsat scene, all 7 spectral bands, 190 km x 180 km area per file.
Data format = GeoTIFF. [Landsat 4-7 Surface Reflectance User Guide (data from 1982-present)](http://landsat.usgs.gov/documents/cdr_sr_product_guide.pdf)  [Landsat 8 Surface Reflectance User Guide (data from 2013-present)](http://landsat.usgs.gov/documents/provisional_lasrc_product_guide.pdf)   [Landsat sensor versions/history]( http://landsat.usgs.gov/about_mission_history.php) 
[GitHub tool for bulk downloading Landsat orders](https://github.com/USGS-EROS/espa-bulk-downloader)

Scientific data set (SDS) or bands are:   (Note Landsat filenames use the sensor id (LXX), path (PPP), row (RRR), year (YYYY), julian date (DDD),  followed by '_sr_')  (Sensors LE7 for Landsat 7 Enhanced Thematic Mapper, LT5 for Landsat 5 Thematic Mapper, LT4 for Landsat 4 Thematic Mapper).  GeoTIFF files have latitude/longitude information in file format.

- Surface reflectance for band 1
- Surface reflectance for band 2
- Surface reflectance for band 3
- Surface reflectance for band 4
- Surface reflectance for band 5
- Surface reflectance for band 6
- Surface reflectance for band 7
- Surface reflectance atmospheric opacity
- Surface reflectance adjacent cloud QA
- Surface reflectance cloud QA
- Surface reflectance cloud shadow QA
- Surface reflectance snow QA
- Cloud mask band (CF mask)
- CF mask confidence band

# Tools
Python
(matlab, idl, ENVI/IDL, ArcGIS - commonly used proprietary software)  

[Daac2Disk tool](https://lpdaac.usgs.gov/lp_daac2disk_download_manager_release)
or [LP DAAC data pool / ftp or http download](https://lpdaac.usgs.gov/data_access/data_pool)  - for downloading MODIS data

[pyMODIS](http://www.pymodis.org/) --  mosaicing/reprojecting/gridding/downloading MODIS data

[MODIS Grid](http://modis-land.gsfc.nasa.gov/MODLAND_grid.html) -- information on MODIS grid / tiles

[hdfgroup.org website](https://www.hdfgroup.org/) -- information / tools /readers for understanding MODIS, CALIOP HDF formats

[Example NetCDF readers](http://www-pord.ucsd.edu/~cjiang/python.html)

[Randolph Glacier Inventory 5.0](http://www.glims.org/RGI/)

[MERRA-2 User Guide](http://gmao.gsfc.nasa.gov/pubs/tm/docs/Bosilovich803.pdf)

[CALIOP Website, Tools, Information](https://eosweb.larc.nasa.gov/news/calipso-v3-00-lidar-level-3-aerosol-product-release)

[MODIS Surface Reflectance User Guide](http://modis-sr.ltdri.org/guide/MOD09_UserGuide_v1.4.pdf)

[Landsat Data Homepage](http://landsat.gsfc.nasa.gov/?page_id=9)






