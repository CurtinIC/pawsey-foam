#!/bin/bash
#SBATCH -N 3 --ntasks-per-node
odule unload PrgEnv-cray/5.2.82
module load PrgEnv-gnu
module load openfoam
module load faprun

