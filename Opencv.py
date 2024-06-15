import cv2 as cv
img =cv.imread("profile.png")
height, width, channels = img.shape

new_height = int(height*0.5)
new_width = int(width *0.3)

resized_img =cv.resize(img, (new_height, new_width))

cv.inshow("Original Size", img)
cv.imwrite("resized_img.png", resized_img )
cv.waitKey(0)