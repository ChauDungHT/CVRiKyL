# 4. Thay đổi kích thước ảnh gấp 1.5 lần
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"D:\Computer Vision\img\logo-VInhUni.png")
resize = cv2.resize(img, None, fx=1.5, fy=1.5)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.subplot(122), plt.imshow(resize, cmap='gray')
plt.show()