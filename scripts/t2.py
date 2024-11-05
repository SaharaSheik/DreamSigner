import os
from moviepy.editor import VideoFileClip

def trim_video_to_match(original_path, target_path, output_folder):
    # Determine output file path
    output_path = os.path.join(output_folder, os.path.basename(target_path))

    # Check if the output file already exists
    if os.path.exists(output_path):
        print(f"Skipping {os.path.basename(target_path)} as it already exists in the output folder.")
        return

    # Load the videos
    original_clip = VideoFileClip(original_path)
    target_clip = VideoFileClip(target_path)

    # Determine the shorter duration
    min_duration = min(original_clip.duration, target_clip.duration)

    # Trim the target video to the duration of the original video
    trimmed_clip = target_clip.subclip(0, min_duration)

    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save the trimmed video
    trimmed_clip.write_videofile(output_path, codec='libx264')

    # Close the clips to free up resources
    original_clip.close()
    target_clip.close()
    trimmed_clip.close()

def match_and_trim_videos(dir1, dir2, output_dir):
    # Ensure we are working with full paths
    dir1 = os.path.abspath(dir1)
    dir2 = os.path.abspath(dir2)
    output_dir = os.path.abspath(output_dir)

    # Get lists of filenames from both directories
    filenames1 = set(os.listdir(dir1))
    filenames2 = set(os.listdir(dir2))

    # Find common filenames
    common_files = filenames1.intersection(filenames2)

    # Process each common file
    for filename in common_files:
        original_path = os.path.join(dir1, filename)
        target_path = os.path.join(dir2, filename)
        trim_video_to_match(original_path, target_path, output_dir)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 4:
        print("Usage: python script.py <directory1> <directory2> <output_directory>")
        sys.exit(1)

    dir1, dir2, output_dir = sys.argv[1], sys.argv[2], sys.argv[3]
    match_and_trim_videos(dir1, dir2, output_dir)