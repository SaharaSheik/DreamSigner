# import os
# import random
# import cv2
# import yaml

# def extract_random_frame(video_path, output_image_path):
#     cap = cv2.VideoCapture(video_path)
#     frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#     random_frame = random.randint(0, frame_count - 1)

#     cap.set(cv2.CAP_PROP_POS_FRAMES, random_frame)
#     ret, frame = cap.read()

#     if ret:
#         cv2.imwrite(output_image_path, frame)
#     cap.release()

# def create_animation_yaml(image_folder, video_folder, output_yaml_path):
#     pretrained_paths = {
#         'pretrained_base_model_path': "./pretrained_weights/stable-diffusion-v1-5/",
#         'pretrained_vae_path': "./pretrained_weights/sd-vae-ft-mse",
#         'image_encoder_path': "./pretrained_weights/image_encoder",
#         'denoising_unet_path': "./pretrained_weights/denoising_unet.pth",
#         'reference_unet_path': "./pretrained_weights/reference_unet.pth",
#         'pose_guider_path': "./pretrained_weights/pose_guider.pth",
#         'motion_module_path': "./pretrained_weights/motion_module.pth",
#         'inference_config': "./configs/inference/inference_v2.yaml",
#         'weight_dtype': 'fp32'
#     }

#     test_cases = {}

#     for filename in os.listdir(image_folder):
#         if filename.endswith(".png"):
#             image_path = os.path.join(image_folder, filename)
#             video_path = os.path.join(video_folder, filename.replace('.png', '.mp4'))
#             test_cases[f'"{image_path}"'] = [f' "{video_path}"']

#     data = {**pretrained_paths, 'test_cases': test_cases}

#     with open(output_yaml_path, 'w') as yaml_file:
#         yaml.dump(data, yaml_file, default_flow_style=False, sort_keys=False, width=4096)

# def main():
#     video_directory = '/home/ssheikholeslami/Moore-AnimateAnyone/data/test/testTrim'  # Directory containing videos
#     output_image_directory = '/home/ssheikholeslami/Moore-AnimateAnyone/ref_images'  # Directory to save reference images
#     output_yaml_path = '/home/ssheikholeslami/Moore-AnimateAnyone/YAML/animation.yaml'  # Path to save the YAML file

#     if not os.path.exists(output_image_directory):
#         os.makedirs(output_image_directory)

#     for root, _, files in os.walk(video_directory):
#         for file in files:
#             if file.endswith(".mp4"):
#                 video_path = os.path.join(root, file)
#                 output_image_path = os.path.join(output_image_directory, file.replace('.mp4', '.png'))
#                 extract_random_frame(video_path, output_image_path)

#     create_animation_yaml(output_image_directory, video_directory, output_yaml_path)

# if __name__ == "__main__":
#     main()

    # video_directory = '/home/ssheikholeslami/Moore-AnimateAnyone/data/test/raw_videos'  # Directory containing videos
    # output_image_directory = '/home/ssheikholeslami/Moore-AnimateAnyone/ref_images'  # Directory to save reference images
    # output_yaml_path = '/home/ssheikholeslami/Moore-AnimateAnyone/YAML/animation.yaml'  # Path to save the YAML file
    # test_video_directory = '/home/ssheikholeslami/Moore-AnimateAnyone/data/test/keypoints'  # Directory containing the test videos

import os
import random
import cv2
import yaml

def extract_random_frame(video_path, output_image_path):
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    random_frame = random.randint(0, frame_count - 1)

    cap.set(cv2.CAP_PROP_POS_FRAMES, random_frame)
    ret, frame = cap.read()

    if ret:
        cv2.imwrite(output_image_path, frame)
    cap.release()

def create_animation_yaml(image_folder, test_video_folder, output_yaml_path):
    pretrained_paths = {
        'pretrained_base_model_path': '"./pretrained_weights/stable-diffusion-v1-5/"',
        'pretrained_vae_path': '"./pretrained_weights/sd-vae-ft-mse"',
        'image_encoder_path': '"./pretrained_weights/image_encoder"',
        'denoising_unet_path': '"./pretrained_weights/denoising_unet.pth"',
        'reference_unet_path': '"./pretrained_weights/reference_unet.pth"',
        'pose_guider_path': '"./pretrained_weights/pose_guider.pth"',
        'motion_module_path': '"./pretrained_weights/motion_module.pth"',
        'inference_config': '"./configs/inference/inference_v2.yaml"',
        'weight_dtype': 'fp32'
    }

    test_cases = {}

    for filename in os.listdir(image_folder):
        if filename.endswith('.png'):
            image_path = os.path.join(image_folder, filename)
            video_path = os.path.join(test_video_folder, filename.replace('.png', '.mp4'))
            test_cases[f'"{image_path}"'] = [f'"{video_path}"']

    data = {**pretrained_paths}

    with open(output_yaml_path, 'w') as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=False, sort_keys=False, width=4096)

        # Manually add the test_cases section with the correct formatting
        yaml_file.write('test_cases:\n')
        for image_path, video_paths in test_cases.items():
            yaml_file.write(f'  {image_path}:\n')
            for video_path in video_paths:
                yaml_file.write(f'    - {video_path}\n')

def main():
    video_directory = '/home/ssheikholeslami/Moore-AnimateAnyone/data/test/raw_videos'  # Directory containing videos
    output_image_directory = '/home/ssheikholeslami/Moore-AnimateAnyone/ref_images'  # Directory to save reference images
    output_yaml_path = '/home/ssheikholeslami/Moore-AnimateAnyone/YAML/animation.yaml'  # Path to save the YAML file
    test_video_directory = '/home/ssheikholeslami/Moore-AnimateAnyone/data/test/keypoints'  # Directory containing the test videos



    if not os.path.exists(output_image_directory):
        os.makedirs(output_image_directory)

    for root, _, files in os.walk(video_directory):
        for file in files:
            if file.endswith('.mp4'):
                video_path = os.path.join(root, file)
                output_image_path = os.path.join(output_image_directory, file.replace('.mp4', '.png'))
                extract_random_frame(video_path, output_image_path)

    create_animation_yaml(output_image_directory, test_video_directory, output_yaml_path)

if __name__ == "__main__":
    main()

    # video_directory = '/home/ssheikholeslami/Moore-AnimateAnyone/data/test/testTrim'  # Directory containing videos
    # output_image_directory = '/home/ssheikholeslami/Moore-AnimateAnyone/ref_images'  # Directory to save reference images
    # output_yaml_path = '/home/ssheikholeslami/Moore-AnimateAnyone/YAML/animation.yaml'  # Path to save the YAML file
    # test_video_directory = '/home/ssheikholeslami/Moore-AnimateAnyone/data/test/keypoints'  # Directory containing the test videos

