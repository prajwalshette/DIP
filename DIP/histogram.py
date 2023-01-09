import cv2
from matplotlib import pyplot as plt

lowing = cv2.imread('image2.jpg',0)
# find frequency of pixels in range 0-255
low = cv2.calcHist([lowing], [0], None, [256],[0,256])

# show the plotting graph of an image
plt.subplot(4,2,1)
plt.imshow(lowing)
plt.subplot(4,2,2)
plt.plot(low)
plt.title('Low Contrast')

highing = cv2.imread('image1.jpg',0)
# find frequency of pixels in range 0-255 
high = cv2.calcHist([highing], [0], None, [256],[0,256])
# show the plotting graph of an image 
plt.subplot(4,2,3)
plt.imshow(highing)
plt.subplot(4,2,4) 
plt.plot(high)
plt.title('High Contrast')

brighting = cv2.imread('img1.jpg',0) 
# find frequency of pixels in range 0-255

bright = cv2.calcHist([brighting], [0],None, [256], [0,256])
# show the plotting graph of an image
plt.subplot(4,2,5)
plt.imshow(brighting)
plt.subplot(4,2,6)
plt.plot(bright)
plt.title('Bright Image')

darking = cv2.imread('Dark.png', 0)

# find frequency of pixels in range 0-255 
dark = cv2.calcHist([darking], [0], None, [256], [0,256])

# show the plotting graph of an image

plt.subplot(4,2,7)
plt.imshow(darking)
plt.subplot(4,2,8)
plt.plot(dark)
plt.title('Dark Image')
plt.show()

