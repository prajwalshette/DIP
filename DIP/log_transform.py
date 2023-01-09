import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
   
# Read an image
image = cv2.imread('image1.jpg')
   
# Apply log transformation method
c = 255 / np.log(1 + np.max(image))
log_image = c * (np.log(image + 1))
   
# Specify the data type so that
# float value will be converted to int
log_image = np.array(log_image, dtype = np.uint8)
   
# Display both images
plt.imshow(image)
plt.show()
plt.imshow(log_image)
plt.show()