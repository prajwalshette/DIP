import cv2
import numpy as np

img11 = cv2.imread('image2.jpg')
img22 = cv2.imread('image1.jpg')
result_image = cv2.multiply(img11, img22)
cv2.imshow('Multiply Image', result_image)

cv2.waitKey(0)
cv2.destroyAllWindows()