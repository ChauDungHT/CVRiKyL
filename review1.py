import cv2
import matplotlib.pyplot as plt

img  = cv2.imread(r"D:\Computer Vision\img\logo-VInhUni.png")

w, h = img.shape[:2]

new = img[0:w, 0:h//2]
gray = cv2.cvtColor(new, cv2.COLOR_BGR2GRAY)
amban = 255 - new

plt.subplot(221), plt.imshow(img, cmap="gray")
plt.subplot(222), plt.imshow(new, cmap="gray")
plt.subplot(223), plt.imshow(gray, cmap="gray")
plt.subplot(224), plt.imshow(amban, cmap="gray")
plt.show()