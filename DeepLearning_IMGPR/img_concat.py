import cv2
import numpy as np

img1 = cv2.imread("D:/INTERNSHIP/image.jpg")
img2 = cv2.imread("D:/INTERNSHIP/image1/57-577323_full-hd-bike-background.jpg")

img1 = cv2.resize(img1, (500, 500))
img2 = cv2.resize(img2, (500, 500))

h_concat = np.hstack((img1, img2))
v_concat = np.vstack((img1, img2))

cv2.imshow('Horizontal Concatenation', h_concat)
cv2.imshow('Vertical Concatenation', v_concat)

cv2.waitKey(0)
cv2.destroyAllWindows()