import os
from moviepy.editor import VideoFileClip
import sys

def trim_video(original_path, target_path, output_path):
    # Load video files
    original_clip = VideoFileClip(original_path)
    target_clip = VideoFileClip(target_path)

    # Trim target clip to the duration of the original clip
    trimmed_clip = target_clip.subclip(0, min(original_clip.duration, target_clip.duration))

    # Create output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Save the trimmed clip
    trimmed_file_path = os.path.join(output_path, os.path.basename(target_path))
    trimmed_clip.write_videofile(trimmed_file_path, codec='libx264')

    original_clip.close()
    target_clip.close()
    trimmed_clip.close()

def match_and_trim(dir1, dir2, output_dir):
    # Get lists of files in both directories
    files1 = set(os.listdir(dir1))
    files2 = set(os.listdir(dir2))

    # Find common files
    common_files = files1.intersection(files2)

    # Process each common file
    for file_name in common_files:
        original_path = os.path.join(dir1, file_name)
        target_path = os.path.join(dir2, file_name)
        trim_video(original_path, target_path, output_dir)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python /home/ssheikholeslami/Moore-AnimateAnyone/scripts/videoTrimmer.py <directory1> <directory2> <output_directory>")
        #python /home/ssheikholeslami/Moore-AnimateAnyone/scripts/videoTrimmer.py /groups/sernam/ASL/generatedInfo/trainVideos /home/ssheikholeslami/Moore-AnimateAnyone/data/train/raw_videos /home/ssheikholeslami/Moore-AnimateAnyone/data/oneTrim
        sys.exit(1)

    dir1, dir2, output_dir = sys.argv[1], sys.argv[2], sys.argv[3]
    match_and_trim(dir1, dir2, output_dir)