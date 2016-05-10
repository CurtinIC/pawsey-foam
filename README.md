## __pawseyFOAM__
#### *Steps to running OpenFOAM code optimally on Pawsey*
#### __Distributed ramfs__
##### 

- On magnus, download and install pawseyFOAM using:
```sh
$ git clone https://github.com/CurtinIC/pawsey-foam.git
$ cd pawsey-foam
$ ./install
```
- Change certain fields in system/decomposeParDict:
```sh
distributed yes;
roots();
```
- Change the slurm submit script (file - slurm):

Original:
```sh
#!/bin/bash
#SBATCH -N 3 --ntasks-per-node
decomposePar
setFields
aprun interFoam
```

Modified job script:
```sh
#!/bin/bash
#SBATCH -N 3 --ntasks-per-node
module unload PrgEnv-cray/5.2.82
module load PrgEnv-gnu
module load openfoam
module load faprun
decomposePar
setFields
faprun mkdir -p /dev/shm/foam
faprun cp -r $SLURM_SUBMIT_DIR/{0,case.foam,constant,system} /dev/shm/foam
cd /dev/shm/foam
faprun cp -r $SLURM_SUBMIT_DIR/processor@rank .
faprun aprun interFoam @stop -10 #sends SIGTERM 10s before the walltime expires - just in time to copy directories back to LUSTRE--being tested]
faprun cp -r processor* $SLURM_SUBMIT_DIR
faprun rm -rf /dev/shm/*
```

#### __"LUSTRE" on LUSTRE__
##### **To be updated

