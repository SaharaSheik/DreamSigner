#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=1
#SBATCH --time=24:00:00
#SBATCH --output=myjobresults-%J.out
#SBATCH --job-name=ASL
#SBATCH --gres=gpu:1
#SBATCH -C [gpu80]
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user sa641631@ucf.edu


# Load modules
echo "Slurm nodes assigned :$SLURM_JOB_NODELIST"
module purge
module load cuda
module load gcc/gcc-9.1.0
module load oneapi/mkl
source ~/.bashrc

conda activate animate
# export LD_LIBRARY_PATH=/home/ssheikholeslami/anaconda3/envs/animate/lib

cd /home/ssheikholeslami/Moore-AnimateAnyone
accelerate launch train_stage_2.py --config configs/train/stage2.yaml


