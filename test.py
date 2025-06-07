import cv2

img  = cv2.imread(r"D:\Computer Vision\img_NCKH\000104.jpg")

x = int(input('Nhap toa do x: '))
print(img[x, x])