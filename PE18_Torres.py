import cv2
import numpy as np

# Load the image
img = cv2.imread("3sample.jpg")

# Convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold the image to create a binary image
_, thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Perform morphological operations to clean up the image
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# Sure background area
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# Finding sure foreground area using distance transform
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 3)  # Adjusted distance transform size
_, sure_fg = cv2.threshold(dist_transform, 0.1*dist_transform.max(), 255, 0)  # Adjusted threshold value

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# Marker labelling
_, markers = cv2.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown == 255] = 0

# Apply watershed algorithm
markers = cv2.watershed(img, markers)
# Generate random colors
colors = np.random.randint(0, 255, (markers.max() + 1, 3))

# Initialize circle counter
circle_count = 0

# Loop over the unique markers
for marker in np.unique(markers):
    if marker == 0:
        continue
    # Create a mask to segment out the region belonging to the current marker
    mask = np.zeros(img.shape[:2], dtype="uint8")
    mask[markers == marker] = 255

    # Find contours in the mask and approximate the contours
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # For each contour, approximate the curve and detect the shapes.
    for cnt in contours:
        # Approximate the contour
        perimeter = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.03 * perimeter, True)  # Adjusted epsilon value

        # Calculate the area and perimeter ratio to determine circularity
        area = cv2.contourArea(cnt)
        if perimeter == 0:
            circularity = 0
        else:
            circularity = 4 * np.pi * area / (perimeter * perimeter)

        # Filter circular shapes
        if circularity > 0.7:  # Adjusted circularity threshold
            # Increment circle count
            circle_count += 1

            # Get the center and radius of the contour
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            center = (int(x), int(y))
            radius = int(radius)

            # Draw a circle around the circular shape
            cv2.circle(img, center, radius, colors[marker].tolist(), 2)
            
            # Draw the count number next to each circle
            cv2.putText(img, str(circle_count), (center[0] + radius, center[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

# Create a border for the text
border_size = 50
border_color = (255, 255, 255)
img_with_border = cv2.copyMakeBorder(img, border_size, 0, 0, 0, cv2.BORDER_CONSTANT, value=border_color)

# Display the total count of circles detected on the border
cv2.putText(img_with_border, "Total Money Count: " + str(circle_count), (10, border_size - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# Show the final image
cv2.imshow("Coin Detection", img_with_border)
print("Number of circles detected:", circle_count)
cv2.waitKey(0)
cv2.destroyAllWindows()
