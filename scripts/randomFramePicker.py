import cv2
import random
import os

def save_random_frame(video_path, output_path):
    """Save a random frame from the video as a JPEG file."""
    # Open the video file
    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    # Get the total number of frames in the video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Pick a random frame number
    random_frame_number = random.randint(0, total_frames - 1)

    # Set the video to the random frame
    video.set(cv2.CAP_PROP_POS_FRAMES, random_frame_number)

    # Read the random frame
    success, frame = video.read()

    if success:
        # Save the frame as a JPEG file
        cv2.imwrite(output_path, frame)
        print(f"Random frame saved to {output_path}")
    else:
        print(f"Error: Could not read frame {random_frame_number} from video")

    # Release the video capture object
    video.release()

def main():
    video_path = '/home/ssheikholeslami/Moore-AnimateAnyone/data/test/raw_videos/-fZc293MpJk_6-1-rgb_front.mp4'
    output_path = '/home/ssheikholeslami/Moore-AnimateAnyone/configs/inference/pose_images/random_frame2.jpg'

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    save_random_frame(video_path, output_path)

if __name__ == "__main__":
    main()