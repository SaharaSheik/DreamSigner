import os
import yaml

def generate_test_cases(directory):
    test_cases = {}
    test_cases['pretrained_base_model_path'] = "./pretrained_weights/stable-diffusion-v1-5/"
    test_cases['pretrained_vae_path'] = "./pretrained_weights/sd-vae-ft-mse"
    test_cases['image_encoder_path'] = "./pretrained_weights/image_encoder"
    test_cases['denoising_unet_path'] = "./pretrained_weights/denoising_unet.pth"
    test_cases['reference_unet_path'] = "./pretrained_weights/reference_unet.pth"
    test_cases['pose_guider_path'] = "./pretrained_weights/pose_guider.pth"
    test_cases['motion_module_path'] = "./pretrained_weights/motion_module.pth"

    test_cases['inference_config'] = "./configs/inference/inference_v2.yaml"
    test_cases['weight_dtype'] = 'fp16'

    test_cases['test_cases'] = {}
    test_cases['test_cases']['video_files'] = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".mp4"):  # Change the extension as needed
                x = os.path.join(root, file)
                y = str("")+x+str("")
                # test_cases['test_cases']['video_files'].append(os.path.join(root, file))
                test_cases['test_cases']['video_files'].append(y)

    return test_cases

def write_yaml(data, output_file):
    with open(output_file, 'w') as yaml_file:
        yaml_file.write("pretrained_base_model_path: \"./pretrained_weights/stable-diffusion-v1-5/\"\n")
        yaml_file.write("pretrained_vae_path: \"./pretrained_weights/sd-vae-ft-mse\"\n")
        yaml_file.write("image_encoder_path: \"./pretrained_weights/image_encoder\"\n")
        yaml_file.write("denoising_unet_path: \"./pretrained_weights/denoising_unet.pth\"\n")
        yaml_file.write("reference_unet_path: \"./pretrained_weights/reference_unet.pth\"\n")
        yaml_file.write("pose_guider_path: \"./pretrained_weights/pose_guider.pth\"\n")
        yaml_file.write("motion_module_path: \"./pretrained_weights/motion_module.pth\"\n")
        yaml_file.write("inference_config: \"./configs/inference/inference_v2.yaml\"\n")
        yaml_file.write("weight_dtype: 'fp16'\n\n")
        yaml.dump(data, yaml_file)

if __name__ == "__main__":
    # directory = '/home/ssheikholeslami/Moore-AnimateAnyone/data/test'
    directory = '/groups/sernam/ASL/poseVideos/allVids' # Change this to your video directory
    output_file = 'animation2.yaml' # Change this to your desired output file

    test_cases_data = generate_test_cases(directory)
    write_yaml(test_cases_data['test_cases'], output_file)




# import os
# import yaml

# def generate_test_cases(directory):
#     test_cases = {}
#     test_cases['test_cases'] = {}
#     test_cases['test_cases']['video_files'] = []

#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if file.endswith(".mp4"):  # Change the extension as needed
#                 test_cases['test_cases']['video_files'].append(os.path.join(root, file))

#     return test_cases

# def write_yaml(data, output_file):
#     with open(output_file, 'w') as yaml_file:
#         yaml.dump(data, yaml_file)

# if __name__ == "__main__":
#     directory = '/home/ssheikholeslami/Moore-AnimateAnyone/data/test'  # Change this to your video directory
#     output_file = 'test_cases.yaml' # Change this to your desired output file

#     test_cases_data = generate_test_cases(directory)
#     write_yaml(test_cases_data, output_file)