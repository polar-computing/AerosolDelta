for y in {1980..2016}
do
  for m in 01 02 03 04 05 06 07 08 09 10 11 12
  do
    wget ftp://goldsmr4.sci.gsfc.nasa.gov/data/s4pa/MERRA2_MONTHLY/M2TMNXAER.5.12.4/$y/MERRA2_100.tavgM_2d_aer_Nx.$y$m.nc4
  done
done
