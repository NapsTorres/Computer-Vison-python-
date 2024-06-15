import cv2
from PIL import Image
import numpy as np

image = Image.open('rick.JPG')

image.thumbnail((450, 500))
image.save('rick_resized.JPG')

originalImage = cv2.imread('rick_resized.JPG')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
invertImage = cv2.bitwise_not(originalImage)
(thresh, blackAndWhiteimage) = cv2.threshold(grayImage, 125, 255, cv2.THRESH_BINARY)
blackAndWhiteimage=cv2.cvtColor(blackAndWhiteimage, cv2.COLOR_GRAY2BGR)

grayImage_bgr = cv2.cvtColor(grayImage, cv2.COLOR_GRAY2BGR)


collage = np.concatenate((np.concatenate((originalImage, blackAndWhiteimage), axis=1),
                          np.concatenate((grayImage_bgr, invertImage), axis=1)), axis=0)

cv2.imshow('Rickroll', collage)
cv2.imwrite('PE13_Torres.jpg', collage)

cv2.waitKey(0)
