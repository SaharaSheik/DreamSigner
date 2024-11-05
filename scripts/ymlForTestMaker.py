import os
import sys
import yaml

def collect_files(directory, extension):
    """ Collect all files in the specified directory with the given extension """
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(extension)]

def write_yaml(ref_image_path, output_file):
    """ Write the predefined paths and dynamic test case for the single image to a YAML file """
    config = {
        "pretrained_base_model_path": "./pretrained_weights/stable-diffusion-v1-5/",
        "pretrained_vae_path": "./pretrained_weights/sd-vae-ft-mse",
        "image_encoder_path": "./pretrained_weights/image_encoder",
        "denoising_unet_path": "./pretrained_weights/denoising_unet.pth",
        "reference_unet_path": "./pretrained_weights/reference_unet.pth",
        "pose_guider_path": "./pretrained_weights/pose_guider.pth",
        "motion_module_path": "./pretrained_weights/motion_module.pth",
        "inference_config": "./configs/inference/inference_v2.yaml",
        "weight_dtype": "fp16",
        "test_cases": {}
    }

    # Directory for pose videos
    video_dir = '/home/ssheikholeslami/Moore-AnimateAnyone/data/test/keypoints'

    if os.path.exists(video_dir):
        videos = collect_files(video_dir, ".mp4")

        # Store video paths with explicit double quotes
        config["test_cases"][ref_image_path] = videos

    # Custom function to force double quotes in YAML without any additional single quotes
    def quoted_str_presenter(dumper, data):
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')

    yaml.add_representer(str, quoted_str_presenter)

    # Save to YAML
    with open(output_file, 'w') as file:
        yaml.dump(config, file, sort_keys=False, allow_unicode=True)


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <path_to_single_image> <output_yaml_file>")
        sys.exit(1)

    ref_image_path = sys.argv[1]  # Path to the single reference image
    output_file = sys.argv[2]  # Output YAML file path

    if not os.path.exists(ref_image_path):
        print(f"Error: The specified image does not exist at {ref_image_path}")
        sys.exit(1)

    write_yaml(ref_image_path, output_file)
    print(f'YAML configuration has been written to {output_file}')

if __name__ == "__main__":
    main()