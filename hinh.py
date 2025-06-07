import cv2
import numpy as np

img = cv2.imread(r"D:\Computer Vision\img\10.jpg")

cv2.line(img, (50, 50), (200, 50), (0, 255, 0), 2)

cv2.rectangle(img, (150,200), (400, 600), (18, 35, 81), 6, 2, 1)

cv2.rang

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()