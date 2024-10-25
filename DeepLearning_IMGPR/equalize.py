import cv2

img = cv2.imread("D:/INTERNSHIP/image1/57-577323_full-hd-bike-background.jpg", 0)
equalized = cv2.equalizeHist(img)

cv2.imshow('Equalized Image', equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()