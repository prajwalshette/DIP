import cv2

img1 = cv2.imread("image1.jpg")
img2 = cv2.imread("image2.jpg")
bitwise_and = cv2.bitwise_and(img2, img1)

cv2.imshow("bit_and", bitwise_and)

cv2.waitKey(0)
cv2.destroyAllWindows()