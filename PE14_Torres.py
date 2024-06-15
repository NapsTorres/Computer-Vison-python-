import cv2
from PIL import Image
import numpy as np

image = Image.open('rose.JPG')

image.thumbnail((450, 500))
image.save('rose_resized.JPG')

originalImage = cv2.imread('rose_resized.JPG')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
invertImage = cv2.bitwise_not(originalImage)
cv2.imwrite('gray.png', grayImage)
cv2.imwrite('invert.png', invertImage)

mountain = cv2.imread('gray.png', 1) 
  
# Read image2 
dog = cv2.imread('invert.png', 1) 
  
# Blending the images with 0.3 and 0.7 
img = cv2.addWeighted(mountain, 0.7, dog, 0.3, 9) 
  
# Show the image 
cv2.imshow('orig', originalImage)
cv2.imshow('image', img) 
  
# Wait for a key 
cv2.waitKey(0) 
  
# Distroy all the window open 
cv2.distroyAllWindows() 


