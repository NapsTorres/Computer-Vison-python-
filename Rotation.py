import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('rick.jpg', 0)
rows, cols = img.shape

# Create a figure and subplot grid
fig, axs = plt.subplots(2, 2)

# Iterate through different rotation angles
for i, angle in enumerate([45, 180, 90, 270]):
    # Calculate the rotation matrix
    M = cv.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), angle, 1)
    # Apply the transformation
    dst = cv.warpAffine(img, M, (cols, rows))
    # Display the transformed image in the corresponding subplot
    axs[i // 2, i % 2].imshow(dst, cmap='gray')
    axs[i // 2, i % 2].set_title(f'Rotation: {angle} degrees')

# Hide the axis ticks and labels
for ax in axs.flat:
    ax.axis('off')

# Show the collage
plt.tight_layout()
plt.show()
