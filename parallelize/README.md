# Parallelize Jobs using SLURM - TACC Wrangler

This space is reserved for the TACC Wrangler slurm jobs (to be run in Hadoop or Local mode). Wranlger employs the **S**imple **L**inux **U**tility for **R**esource **M**anagement (SLURM) job scheduler which leverages the tools and commands to perform the most important operations in batch processing: job submission, job monitoring, and job control (cancel, resource request modification, etc.)

Please refer to the SLURM [scripts](slurm_scripts) for details on the headers and format. The scripts also includes the Wrangler's [Launcher](https://github.com/TACC/launcher) facility to run jobs in embarrasingly parallel mode.

Some examples of job files can be seen [here](job_examples).

Here are few things to keep in mind.

* It is a good practice to use **.slurm** extension for the slurm file.
* **sinfo -o "%20P %5a %.10l %16F"** - Lists the availability and status of queues. The output contains a header (A/I/O/T) for the *NODES* which means:
    * **A**: Allocated Nodes
    * **I**: Idle Nodes
    * **O**: Other Status for Nodes
    * **T**: Total Nodes in the partition
* **squeue -u <username>** - Helps to monitor the jobs. Displays job status and other basic information.
* **showq -u <username>** - Helps to moniter the jobs. Displays job status and other basic information.
* **scontrol show job <job id>** - Provide more details about the job, its dependencies, working directory, etc.
* **sbatch <job file>** - Schedules the job into SLURM scheduler. From here, the job scheduler takes the lead, look for available nodes and executes the job. If there is no available node, the job show "PD" (Pending) status.
* **scancel <job id>** - Cancels the job for the given job id.
