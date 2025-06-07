import cv2
import matplotlib.pyplot as plt

img  = cv2.imread(r"D:\DACN\DACN\image-test\nguoi32.jpg")

blur = cv2.blur(img, (5,5))
mediaBlur = cv2.medianBlur(img, 3)
gauss = cv2.GaussianBlur(img, (5,5), 0)
bilateral = cv2.bilateralFilter(img, 5, 50, 50)

plt.subplot(231), plt.imshow(img, cmap='gray')
plt.subplot(232), plt.imshow(blur, cmap='gray')
plt.subplot(233), plt.imshow(mediaBlur, cmap='gray')
plt.subplot(234), plt.imshow(gauss, cmap='gray')
plt.subplot(235), plt.imshow(bilateral, cmap='gray')
plt.show()