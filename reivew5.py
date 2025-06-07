# 5. Xoay ảnh với góc xoay nhập vào từ bàn phím, tâm xoay ở góc trên bên trái ảnh
import cv2

img = cv2.imread(r"D:\Computer Vision\img\logo-VInhUni.png")

cv2.namedWindow('xoay')
h, w = img.shape[:2]
center = (w//2, h//2)

def get_deg(pos):
    global deg
    deg = pos

deg =  0

cv2.createTrackbar('xoay', 'xoay', 0, 360, get_deg)

while True:
    M = cv2.getRotationMatrix2D(center, deg, 1.0)
    new = cv2.warpAffine(img, M, (w,h))
    cv2.imshow('xoay', new)
    if cv2.waitKey(10) == ord('d') : break
cv2.destroyAllWindows