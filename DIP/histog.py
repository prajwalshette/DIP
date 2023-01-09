import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image1.jpg',0)

hist,bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')
img2 = cdf[img]
img = cv2.imread('image1.jpg',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imwrite('image2.jpg',res)
plt.show()



# import cv2
# from matplotlib import pyplot as plt 
# lowimg = cv2.imread('low.jpg',0)
# # find frequency of pixels in range 0-255
# low = cv2.calcHist([lowimg],[0],None,[256],[0,256])
# # show the plotting graph of an image 
# plt.subplot(4,2,1)  
# plt.imshow(lowimg) 
# plt.subplot(4,2,2)  
# plt.plot(low) 
# plt.title('Low Contrast')

# highimg = cv2.imread('high.jpg',0)
# # find frequency of pixels in range 0-255
# high = cv2.calcHist([highimg],[0],None,[256],[0,256])
# # show the plotting graph of an image 
# plt.subplot(4,2,3)  
# plt.imshow(highimg) 
# plt.subplot(4,2,4)  
# plt.plot(high) 
# plt.title('High Contrast')

# brightimg = cv2.imread('bright.jpg',0)
# # find frequency of pixels in range 0-255
# bright = cv2.calcHist([brightimg],[0],None,[256],[0,256])
# # show the plotting graph of an image 
# plt.subplot(4,2,5)  
# plt.imshow(brightimg) 
# plt.subplot(4,2,6)  
# plt.plot(bright) 
# plt.title('Bright Image')

# darkimg = cv2.imread('dark.jpg',0)
# # find frequency of pixels in range 0-255
# dark = cv2.calcHist([darkimg],[0],None,[256],[0,256])
# # show the plotting graph of an image 
# plt.subplot(4,2,7)  
# plt.imshow(darkimg) 
# plt.subplot(4,2,8)  
# plt.plot(dark) 
# plt.title('Dark Image')

# plt.show()
