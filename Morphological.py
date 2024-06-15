import cv2 as cv
import numpy as np
img = cv.imread('rick.jpg', 0) 

kernel = np.ones((10,10), np.uint8) 
erosion = cv.erode(img, kernel, iterations=1) 
dilation = cv.dilate(img, kernel, iterations=1) 
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel) 
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel) 
tophat= cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel) 
blackhat= cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel) 


cv.imshow( "Erosion", erosion ) 
cv.imshow( "Dilation", dilation )
cv.imshow("Opening", opening)
cv.imshow("Closing", closing)
cv.imshow("Gradient", gradient)
cv.imshow("Top Hat", tophat)
cv.imshow("Black Hat", blackhat)
cv.waitKey(0)
