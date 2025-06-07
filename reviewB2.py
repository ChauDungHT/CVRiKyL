import cv2
import numpy as np

cv2.namedWindow('edit')
img = cv2.imread(r"D:\Computer Vision\TH\logo-VinhUni.png")
w, h = img.shape[:2]
#hàm dịch chuyển
def get_deg(pos):
    global deg
    deg = pos

deg = 180
cv2.createTrackbar('Xoay', 'edit', 0, 1000, get_deg)
while True:
    M = np.float32([[1, 0, deg], [0, 1, 0]])
    new = cv2.warpAffine(img, M, (w, h))
    cv2.imshow('edit', new)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()