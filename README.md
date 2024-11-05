>📋  README.md for code accompanying a Machine Learning paper

# My Paper Title

This repository is the official implementation of [DreamSigner Pose-to-Video Synthesis for
Hyper-Realistic Sign Language Animation].

## Video demos:

[![Watch the video](https://img.youtube.com/vi/Yfax9UKug20/0.jpg)](https://www.youtube.com/watch?v=Yfax9UKug20)



## Requirements

We Recommend a python version >=3.10 and cuda version =11.7. Then build environment as follows:

```setup
python -m venv .venv
source .venv/bin/activate
# Install with pip:
pip install -r requirements.txt
# For face landmark extraction
git clone https://github.com/emilianavt/OpenSeeFace.git
```

>📋  Dowload weights
```
python tools/download_weights.py
```
Weights will be placed under the ./pretrained_weights direcotry.
```
weights will look like this:

./pretrained_weights/
|-- DWPose
|   |-- dw-ll_ucoco_384.onnx
|   `-- yolox_l.onnx
|-- image_encoder
|   |-- config.json
|   `-- pytorch_model.bin
|-- denoising_unet.pth
|-- motion_module.pth
|-- pose_guider.pth
|-- reference_unet.pth
|-- sd-vae-ft-mse
|   |-- config.json
|   |-- diffusion_pytorch_model.bin
|   `-- diffusion_pytorch_model.safetensors
|-- reenact
|   |-- denoising_unet.pth
|   |-- reference_unet.pth
|   |-- pose_guider1.pth
|   |-- pose_guider2.pth
`-- stable-diffusion-v1-5
    |-- feature_extractor
    |   `-- preprocessor_config.json
    |-- model_index.json
    |-- unet
    |   |-- config.json
    |   `-- diffusion_pytorch_model.bin
    `-- v1-inference.yaml
```
## Training

Most of the commands needed to train the model can be found under commands.sh under the script

To train the model(s) in the paper, run this command:

```train
accelerate launch train_stage_1.py --config configs/train/stage1.yaml
accelerate launch train_stage_2.py --config configs/train/stage2.yaml
```


## Evaluation

To evaluate my model on ImageNet, run:

```generate videos using this
python -m scripts.pose2vidcopy --config ./configs/prompts/animation.yaml -W 1024 -H 720 -L 64
```

then use the following
```FVID score
scripts/fvid.py
```

then use openPose to extract keypoints from the generated videos and compare them with key points og froundtroth.  Please refer to OpenPose repo for instructuins as to how to extract keypints


## Pre-trained Models

To comply with the anonymity requirements of NeurIPS, we have not included the GitHub link here. However, we have the pretrained weights available and would be happy to release them upon request.



## Results

Our model achieves the following performance on :


| Model name         |      FID-VID    |         FVD    |
| ------------------ |---------------- | -------------- |
| DreamSinger        |     19.08       |       81.8    |



## Acknowledgements

>📋  We first thank the authors of AnimateAnyone. Additionally, we would like to thank the contributors to the majic-animate, animatediff and Open-AnimateAnyone repositories, OpenPose for their open research and exploration. Furthermore, our repo incorporates some codes from dwpose and animatediff-cli-prompt-travel, and we extend our thanks to them as well.


