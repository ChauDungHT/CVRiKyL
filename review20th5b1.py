import cv2
import matplotlib.pyplot as plt

path  = cv2.imread("D:\Computer Vision\CodeLesson\logo-VInhUni.png")
img  = cv2.cvtColor(path, cv2.COLOR_BGR2GRAY)
print(img.shape[:2])
w, h = int(input('Nhap x: ')), int(input("Nhap y: "))
new = cv2.resize(img, (w,h))

thresh = cv2.adaptiveThreshold(new, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

plt.subplot(131), plt.imshow(img, cmap='gray')
plt.subplot(132), plt.imshow(new, cmap='gray')
plt.subplot(133), plt.imshow(thresh, cmap='gray')
plt.show()