### Generate Graphs (plot_graph.py)

A Python script to generate graphs from the aerosol extracted data. The script currently supports MERRA-2 and CALIOP. The `usage` is described below.

```
usage: plot_graph.py [-h] -i INFILE -o OUTDIR -d DATA -op OPERATION -r REGIONS -y YEARS -gb GROUPBY

Plot Graphs for Aerosol Delta

optional arguments:
  -h, --help            				show this help message and exit
  -i INFILE, --inFile INFILE			Path to the input file (CSV)
  -o OUTDIR, --outDir OUTDIR			Path to the output directory where graphs will be stored
  -d DATA, --data DATA  				Data: merra2, merra2-catau, merra2-mass, caliop
  -op OPERATION, --operation OPERATION	Supports - min, max, median, mean, std
  -r REGIONS, --regions REGIONS			19 regions. Specify range here. 1:19 means all regions
  -y YEARS, --years YEARS				Specify year range. 2002:2016 means from year 2002 to 2016
  -gb GROUPBY, --groupBy GROUPBY		y: year, m: month, ym: year and month

```

<br/>
Example - Generate graphs from MERRA2 STRICT csv with the following conditions:

* Contain only CATAU fields.
* Generate for `max` operation.
* Generate all the regions.
* Use data from year 2006 to 2016
* Data is grouped by `year`


The arguments to the script will be as below:

```
python plot_graph.py -i <path to MERRA2_STRICT.csv file> -o <path to directory where the graphs will be saved> -d merra2-catau -op max -r 1:19 -y 2006:2016 -gb y
```
