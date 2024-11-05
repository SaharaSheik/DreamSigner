import cv2
import os

def extract_all_frames(video_path, output_folder):
    """
    Extracts all frames from a video and saves each frame as a PNG file.

    :param video_path: Path to the video file.
    :param output_folder: Folder where the frames will be saved.
    """
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load the video
    video = cv2.VideoCapture(video_path)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_number = 0

    # Iterate over all frames in the video
    while True:
        success, frame = video.read()
        if not success:
            break

        # Save the frame
        base_name = os.path.basename(video_path)
        file_name = os.path.splitext(base_name)[0] + f"_frame_{frame_number}.png"
        output_path = os.path.join(output_folder, file_name)
        cv2.imwrite(output_path, frame)
        print(f"Frame {frame_number} saved to {output_path}")
        frame_number += 1

    # Release the video capture object
    video.release()

def main():
    input_folder = '/home/ssheikholeslami/Moore-AnimateAnyone/output/20240522/0717--seed_42-1280x720'
    output_folder = '/home/ssheikholeslami/Moore-AnimateAnyone/savedFrames'

    # List all video files in the input directory
    video_files = [f for f in os.listdir(input_folder) if f.endswith(('.mp4', '.avi'))]  # Add other video formats if needed

    # Process each video
    for video_file in video_files:
        video_path = os.path.join(input_folder, video_file)
        extract_all_frames(video_path, output_folder)

if __name__ == "__main__":
    main()