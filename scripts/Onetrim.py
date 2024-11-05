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

def match_and_trim_specific_file(dir1, dir2, output_dir, filename):
    # Construct file paths
    original_path = os.path.join(dir1, filename)
    target_path = os.path.join(dir2, filename)

    # Check if files exist
    if os.path.exists(original_path) and os.path.exists(target_path):
        trim_video(original_path, target_path, output_dir)
    else:
        print("Error: One or both files do not exist in the specified directories.")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <directory1> <directory2> <output_directory> <filename>")
        sys.exit(1)

    dir1, dir2, output_dir, filename = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    match_and_trim_specific_file(dir1, dir2, output_dir, filename)