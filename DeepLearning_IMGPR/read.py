import cv2
# Read an image
image = cv2.imread("D:\INTERNSHIP\image.jpg")
# Display the image using OpenCV
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# To check dimensions of the image
print(image.shape)