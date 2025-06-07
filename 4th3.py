import cv2
import numpy as np

img = cv2.imread(r"D:\Computer Vision\img\9.png")

h, w = img.shape[:2]

tx, ty = 100, -50

M = np.float32([[1,0,tx], [0,1,ty]])

result = cv2.warpAffine(img, M, (w,h))

cv2.imshow('anh goc', img)
cv2.imshow('anh sua', result)
cv2.waitKey(0)
cv2.destroyAllWindows