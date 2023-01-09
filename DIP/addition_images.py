import cv2
import numpy as np
   
image1 = cv2.imread('image2.jpg')
image2 = cv2.imread('image3.jpg')

print("image2 size: ",image2.shape)
print("image1 size: ",image1.shape)

scale_percent = 60

width = int(image2.shape[1]*scale_percent/100)
height = int(image2.shape[1]*scale_percent/100)

width = int(image1.shape[1]*scale_percent/100)
height = int(image1.shape[1]*scale_percent/100)

dim = (width, height)

resized2 = cv2.resize(image2,dim,interpolation=cv2)

# weightedSum = cv2.addWeighted(image1, 0.6, image2, 0.5, 0)
# cv2.imshow('Weighted Image', weightedSum)
 
# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()
