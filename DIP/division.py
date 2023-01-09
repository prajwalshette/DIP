import cv2
import numpy as np

# Reading image file
img = cv2.imread('image1.jpg')
 
# Applying OpenCV scalar division on image
fimg = cv2.divide(img, 2)
 
# Saving the output image
cv2.imwrite('image2', fimg)