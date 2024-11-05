import subprocess
import os
import sys

def run_openpose(input_video, output_dir):
    # Check if the output directory exists, if not, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Path to the OpenPose binary
    openpose_bin = './build/examples/openpose/openpose.bin'

    # Check if the OpenPose binary exists
    if not os.path.isfile(openpose_bin):
        print("OpenPose binary does not exist. Please check your OpenPose installation.")
        return

    # Command to run OpenPose
    openpose_command = [
        openpose_bin,
        '--video', input_video,
        '--write_json', output_dir,
        '--face',
        '--hand',
        '--body', '1',
        '--display', '0',
        '--render_pose', '0'
    ]

    # Run OpenPose
    print("Running OpenPose...")
    subprocess.run(openpose_command)

    # Uncomment the following lines to enable video output with keypoints overlay
    openpose_command.extend([
        '--write_video', os.path.join(output_dir, 'output_video.avi'),
        '--render_pose', '1'
    ])
    subprocess.run(openpose_command)

    print("OpenPose processing complete. Output saved to", output_dir)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python run_openpose.py <input_video.mp4> <output_directory>")
        sys.exit(1)

    input_video = sys.argv[1]
    output_dir = sys.argv[2]
    run_openpose(input_video, output_dir)