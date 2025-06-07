import cv2

img = cv2.imread(r"D:\Computer Vision\img\9.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

crop = img[0:50, 230:608]

cv2.imshow('crop', crop)

cv2.waitKey(0)
cv2.destroyAllWindows