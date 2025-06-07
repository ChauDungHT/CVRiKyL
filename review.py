import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"D:\Computer Vision\TH\logo-VinhUni.png")
print(img.shape[:2])
w = int(input("Nhap toa do x: "))
h = int(input("Nhap toa do y: "))

new = img[0:w, 0:h]
gray = cv2.cvtColor(new, cv2.COLOR_RGB2GRAY)

#phân ngưỡng ảnh
_, new = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)

plt.subplot(121), plt.imshow(img)
plt.subplot(122), plt.imshow(new)
plt.show()