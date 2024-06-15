import numpy as np
import cv2

# Load the original input 
image = cv2.imread("tomjerry.jpg")

# Create blank images for the masks with the same size as the input image
mask1 = np.zeros(image.shape[:2], dtype=np.uint8)
mask2 = np.zeros(image.shape[:2], dtype=np.uint8)

# Create the first circular mask
cv2.circle(mask1, (600, 120), 150, 255, -1)

# Create the second circular mask
cv2.circle(mask2, (150, 300), 120, 255, -1)

# Combine the masks using bitwise 
combined_mask = cv2.bitwise_or(mask1, mask2)

# Apply the combined mask to the image
masked = cv2.bitwise_and(image, image, mask=combined_mask)

# Create a blank canvas to combine the circular masks (black background)
canvas = np.zeros_like(image)

# Draw the circular masks on the canvas (white color)
canvas[mask1 > 0] = 255  
canvas[mask2 > 0] = 255  

# Show the results
cv2.imshow("Original", image)
cv2.imshow("Mask Applied to Image", masked)
cv2.imshow("Circular Masks", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
