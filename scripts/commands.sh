#weight download
git lfs install
git clone https://huggingface.co/guoyww/animatediff

#get json filefor our videos
# python tools/extract_meta_info.py --root_path /home/ssheikholeslami/DPSL/DreamPose/data/test/raw_videos --dataset_name h2s
#new files
python tools/extract_meta_info.py --root_path /home/ssheikholeslami/Moore-AnimateAnyone/data/train/raw_videos --dataset_name h4s


#with trimmed vides make meta

python tools/extract_meta_info.py --root_path /home/ssheikholeslami/Moore-AnimateAnyone/data/oneTrim --dataset_name h5s

python tools/extract_dwpose_from_vid.py --video_root /home/ssheikholeslami/Moore-AnimateAnyone/data/train/raw_videos

accelerate launch train_stage_1.py --config configs/train/stage1.yaml
accelerate launch train_stage_2.py --config configs/train/stage2.yaml

accelerate launch train_stage_1.py --config configs/train/train_stage_1copy.yaml


python -m scripts.pose2vid --config ./configs/prompts/animation.yaml -W 512 -H 784 -L 64


#neew script with video
python -m scripts.pose2vidcopy --config ./configs/prompts/animation.yaml -W 1024 -H 1024 -L 64
python -m scripts.pose2vidcopy --config /home/ssheikholeslami/Moore-AnimateAnyone/animation2.yaml -W 1024 -H 1024 -L 64
python -m scripts.pose2vidcopy --config ./configs/prompts/animation.yaml -W 1280 -H 720 -L 64

python -m scripts.pose2vidcopy --config /home/ssheikholeslami/Moore-AnimateAnyone/animation2.yaml -W 1280 -H 720 -L 64

python tools/extract_meta_info.py --root_path /home/ssheikholeslami/Moore-AnimateAnyone/data/validation --dataset_name h2s2

#animmation yml generaor
python /home/ssheikholeslami/Moore-AnimateAnyone/scripts/ymlForTestMaker.py /home/ssheikholeslami/Moore-AnimateAnyone/configs/inference/pose_images/10.PNG animation3.yaml


python -m scripts.pose2vidcopy --config animation3.yaml -W 1024 -H 1024 -L 64

python -m scripts.pose2vidcopy --config ./configs/prompts/animation.yaml -W 512 -H 784 -L 64

/groups/sernam/ASL/h2sInfo/processedH2STrainVids

python /home/ssheikholeslami/Moore-AnimateAnyone/scripts/t2.py /groups/sernam/ASL/generatedInfo/trainVideos /home/ssheikholeslami/Moore-AnimateAnyone/data/train/raw_videos /home/ssheikholeslami/Moore-AnimateAnyone/data/oneTrim