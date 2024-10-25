import cv2

img = cv2.imread("D:/INTERNSHIP/image1/57-577323_full-hd-bike-background.jpg")
cropped = img[500:600, 100:300]

cv2.imshow('Cropped Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()