import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('rick.jpg', 0)
rows, cols = img.shape

fig, axs = plt.subplots(2, 2)
for i, angle in enumerate([45, 180, 90, 270]):

    M = cv.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), angle, 1)

    dst = cv.warpAffine(img, M, (cols, rows))

    axs[i // 2, i % 2].imshow(dst, cmap='gray')
    axs[i // 2, i % 2].set_title(f'{angle} degrees')


for ax in axs.flat:
    ax.axis('off')

plt.tight_layout()
plt.show()


