import cv2
 

img1 = cv2.imread('image1.jpg')
img2 = cv2.imread('image2.jpg')
bitwise_or = cv2.bitwise_or(img2, img1)

cv2.imshow("bitwise_or", bitwise_or)

cv2.waitKey(0)
cv2.destroyAllWindows()