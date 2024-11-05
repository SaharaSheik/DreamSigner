import tensorflow as tf
import tensorflow_gan as tfgan
import ffmpeg
import numpy as np
import os




# 1280 -H 720
def load_video(filename, frame_size=(1280, 720), num_frames=169):

    print(tf.__version__)
    print(tfgan.__version__)

    """Load a video and convert it to a tensor of shape (num_frames, height, width, channels)."""
    out, _ = (
        ffmpeg.input(filename)
        .filter('fps', fps=25)
        .filter('scale', frame_size[0], frame_size[1])
        .output('pipe:', format='rawvideo', pix_fmt='rgb24')
        .run(capture_stdout=True, capture_stderr=True)
    )
    video = np.frombuffer(out, np.uint8).reshape([-1, frame_size[1], frame_size[0], 3])

    # Sample or pad the video to the required number of frames
    if video.shape[0] > num_frames:
        video = video[:num_frames]
    elif video.shape[0] < num_frames:
        padding = np.zeros((num_frames - video.shape[0], frame_size[1], frame_size[0], 3), dtype=np.uint8)
        video = np.concatenate([video, padding], axis=0)

    return video

def preprocess_videos(videos):
    """Preprocess videos for FVD computation."""
    videos = tf.convert_to_tensor(videos, dtype=tf.float32)
    videos = tf.image.resize(videos, [1280, 720])
    videos = videos / 255.0 * 2.0 - 1.0  # Normalize to [-1, 1]
    return videos

def compute_fvd(ground_truth_video, produced_video):
    """Compute the Fréchet Video Distance (FVD) between two videos."""
    ground_truth_video = preprocess_videos(ground_truth_video)
    produced_video = preprocess_videos(produced_video)

    fvd = tfgan.eval.frechet_inception_distance(
        ground_truth_video,produced_video
    )

    return fvd

def main():
    ground_truth_video_path = '_4PBd_wiX_A_0-5-rgb_front.mp4'
    produced_video_path = 'random_frame__4PBd_wiX_A_0-5-rgb_front_720x1280_3_0236.mp4'

    ground_truth_video = load_video(ground_truth_video_path)
    produced_video = load_video(produced_video_path)

    fvd_score = compute_fvd(ground_truth_video, produced_video)
    print(f"FVD Score: {fvd_score}")