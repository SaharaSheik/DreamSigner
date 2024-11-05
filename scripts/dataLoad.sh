#!/bin/bash

cd /home/ssheikholeslami/DPSL/DreamPose/data

mkdir test
mkdir validation
mkdir training

#test keyponits
cd test
gdown --id 1g8tzzW5BNPzHXlamuMQOvdwlHRa-29Vp
tar -xvzf test_2D_keypoints.tar.gz
cd ..
# test videos
gdown --id 1qTIXFsu8M55HrCiaGv7vZ7GkdB3ubjaG
unzip test_rgb_front_clips.zips

## Training
cd training
gdown --id 1TBX7hLraMiiLucknM1mhblNVomO9-Y0r
tar -xvzf train_2D_keypoints.tar.gz
cd ..


# validation
cd validation
gdown --id 1DhLH8tIBn9HsTzUJUfsEOGcP4l9EvOiO
tar -xvzf val_2D_keypoints.tar.gz
cd ..
cd ..