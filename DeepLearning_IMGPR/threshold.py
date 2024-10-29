import cv2

img = cv2.imread("D:/INTERNSHIP/image1/57-577323_full-hd-bike-background.jpg", 0)
_, threshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Threshold Image', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()