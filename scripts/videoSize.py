import cv2

def get_video_resolution(video_path):
    """Get the resolution of the video."""
    # Open the video file
    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return None

    # Get the width and height of the video frames
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Release the video capture object
    video.release()

    return width, height

def main():
    video_path = '/home/ssheikholeslami/Moore-AnimateAnyone/data/train/raw_videos/_4PBd_wiX_A_0-5-rgb_front.mp4'
    resolution = get_video_resolution(video_path)

    if resolution:
        print(f"Video resolution: {resolution[0]} x {resolution[1]}")

if __name__ == "__main__":
    main()