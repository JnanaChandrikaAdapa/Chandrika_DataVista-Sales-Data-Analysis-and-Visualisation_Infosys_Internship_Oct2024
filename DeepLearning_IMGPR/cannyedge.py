import cv2

img = cv2.imread("D:/INTERNSHIP/image1/57-577323_full-hd-bike-background.jpg", 0)
edges = cv2.Canny(img, 100, 200)

cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()