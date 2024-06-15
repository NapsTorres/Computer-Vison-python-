import cv2
import numpy as np

# Load the image
img = cv2.imread("Coins.jpg")

# Convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Convert to binary image by thresholding
_, threshold = cv2.threshold(img_gray, 245, 255, cv2.THRESH_BINARY_INV)
# Find the contours
contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# For each contour approximate the curve and
# detect the shapes.
for cnt in contours:
    # Approximate the contour
    perimeter = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.04 * perimeter, True)
    # Calculate the area and perimeter ratio to determine circularity
    area = cv2.contourArea(cnt)
    if perimeter == 0:
        circularity = 0
    else:
        circularity = 4 * np.pi * area / (perimeter * perimeter)

    # Filter circular shapes
    if circularity > 0.8:
        # Get the center and radius of the contour
        (x, y), radius = cv2.minEnclosingCircle(cnt)
        center = (int(x), int(y))
        radius = int(radius)
        # Draw a circle around the circular shape
        cv2.circle(img, center, radius, (0, 255, 0), 2)

# Show the final image
cv2.imshow("Coin Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
