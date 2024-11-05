import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np

# Load images
reference_image_path = '/home/ssheikholeslami/Moore-AnimateAnyone/configs/inference/pose_images/10.PNG'
video_clip_image_path = '/home/ssheikholeslami/Moore-AnimateAnyone/configs/inference/pose_images/10.PNG'
pose_sequence_image_path = '/home/ssheikholeslami/Moore-AnimateAnyone/configs/inference/pose_images/SSSS.PNG'

reference_image = Image.open(reference_image_path)
video_clip_image = Image.open(video_clip_image_path)
pose_sequence_image = Image.open(pose_sequence_image_path)

# Create figure and axis
fig, ax = plt.subplots(figsize=(16, 8))

# Display images
ax.imshow(np.ones((800, 1600, 3), dtype=np.uint8) * 255)  # White background

# Place the images
ax.imshow(reference_image, extent=(50, 250, 400, 700))
ax.imshow(pose_sequence_image, extent=(50, 250, 50, 350))
ax.imshow(video_clip_image, extent=(1350, 1550, 400, 700))

# Add annotations
ax.text(150, 720, 'Reference Image', ha='center', va='center')
ax.text(150, 20, 'Pose Sequence', ha='center', va='center')
ax.text(1450, 720, 'Video Clip', ha='center', va='center')

# Draw boxes
ax.add_patch(patches.Rectangle((50, 400), 200, 300, linewidth=1, edgecolor='r', facecolor='none'))
ax.add_patch(patches.Rectangle((50, 50), 200, 300, linewidth=1, edgecolor='g', facecolor='none'))
ax.add_patch(patches.Rectangle((1350, 400), 200, 300, linewidth=1, edgecolor='b', facecolor='none'))

# Draw arrows
ax.arrow(250, 550, 100, 0, head_width=20, head_length=20, fc='k', ec='k')
ax.arrow(250, 200, 100, 0, head_width=20, head_length=20, fc='k', ec='k')
ax.arrow(1250, 550, 100, 0, head_width=20, head_length=20, fc='k', ec='k')

# Add intermediate steps
ax.text(650, 550, 'ReferenceNet', ha='center', va='center')
ax.text(650, 200, 'Pose Guider', ha='center', va='center')
ax.text(1050, 550, 'Denoising UNet', ha='center', va='center')

# Disable axis
ax.axis('off')

# Save the plot as a file
output_path = '/home/ssheikholeslami/Moore-AnimateAnyone/configs/inference/pose_images/plot.png'
plt.savefig(output_path, bbox_inches='tight')

# Close the plot
plt.close(fig)