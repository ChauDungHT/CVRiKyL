import cv2
import matplotlib.pyplot as plt

img0 = cv2.imread(r'D:\Computer Vision\img\11.png')

img = cv2.cvtColor(img0, cv2.COLOR_BGR2RGB)

#Bộ lọc trung bình
img_blur = cv2.blur(img, (9, 9))

#Bộ lọc trung vị
img_median = cv2.medianBlur(img, 5)

#Bộ lọc Gauss
img_gauss = cv2.GaussianBlur(img, (5, 5), 0)

#Bộ lọc song phương
img_bilateral = cv2.bilateralFilter(img, 9, 50, 50)

#Hiển thị ảnh
plt.subplot(321), plt.imshow(img)
plt.subplot(322), plt.imshow(img_blur)
plt.subplot(323), plt.imshow(img_median)
plt.subplot(324), plt.imshow(img_gauss)
plt.subplot(325), plt.imshow(img_bilateral)
plt.show()