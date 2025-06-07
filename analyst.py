import cv2

img = cv2.imread(r"D:\Computer Vision\img\8.png")

cv2.imshow('image', img)

kq = cv2.convertScaleAbs(img, alpha=2, beta=100)
cv2.imshow('sau khi doi', kq)
cv2.waitKey(0)
cv2.destroyAllWindows