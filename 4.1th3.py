import cv2
import numpy as np

img = cv2.imread(r"D:\Computer Vision\img\11.jpg")

new_img = cv2.resize(img, (560,174))

M1 = np.float32([(680,875), (1435,862), (1441,2221), (492,2132)])
w,h = 450,500
M2 = np.float32([(0,0), (w,0), (w, h), (0,h)])
M = cv2.getPerspectiveTransform(M1, M2)
result = cv2.warpPerspective(img, M, (w,h))
cv2.imshow('anh goc', new_img)
cv2.imshow('anh ket qua', result)
cv2.waitKey(0)
cv2.destroyAllWindows()