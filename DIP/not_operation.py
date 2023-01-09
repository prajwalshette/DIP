import cv2

img2 = cv2.imread("image1.jpg")
bitwise_not = cv2.bitwise_not(img2)

cv2.imshow("bitwise_not", bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()