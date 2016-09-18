#!/bin/bash
#
# Simple SLURM script for submitting multiple serial
# jobs (e.g. parametric studies) using a script wrapper
# to launch the jobs.
#
# To use, build the launcher executable and your
# serial application(s) and place them in your WORKDIR
# directory.  Then, edit the CONTROL_FILE to specify 
# each executable per process.
#-------------------------------------------------------
#-------------------------------------------------------
# 
#         <------ Setup Parameters ------>
#
#SBATCH -J MERRA2 
#SBATCH -N 1
#SBATCH -n 24 
#SBATCH -p normal 
#SBATCH -o MERRA2.o%j
#SBATCH -t 48:00:00
#          <------ Account String ----->
# <--- (Use this ONLY if you have MULTIPLE accounts) --->
#SBATCH -A TG-MCB090174
#------------------------------------------------------

#-------------------------------------------------------
#         <------ Custom Parameters ------>

export LAUNCHER_DIR=/data/projects/G-817549/aerosols/launcher
export DATA_PATH=/data/projects/G-817549/aerosols/data
export LAUNCHER_PPN=438
module load java64;

#-------------------------------------------------------

export LAUNCHER_PLUGIN_DIR=$LAUNCHER_DIR/plugins
export LAUNCHER_RMI=SLURM
export LAUNCHER_JOB_FILE=/data/projects/G-817549/aerosols/jobs/merra2_buffer.job

date; 
$LAUNCHER_DIR/paramrun
date;

