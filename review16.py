#16.	Đọc ảnh và thực hiện các thao tác sau: 
#-	Đổi ảnh vừa cắt sang ảnh GRAY 
#-	Phân ngưỡng ảnh bằng thuật toán phân ngưỡng Otsu 
#-	Hiển thị các ảnh trên matplotlib 

import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"D:\Computer Vision\review\logo-VinhUni.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY, cv2.THRESH_OTSU)

plt.subplot(131), plt.imshow(img)
plt.subplot(132), plt.imshow(gray, cmap='gray')
plt.subplot(133), plt.imshow(otsu, cmap='gray')
plt.show()