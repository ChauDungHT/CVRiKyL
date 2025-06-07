import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"D:\Computer Vision\img\test.jpg")

src = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
src_gray = cv2.GaussianBlur(gray, (3, 3), 0)

grad_x = cv2.Sobel(src_gray, cv2.CV_64F, 1, 0, 3)
grad_y = cv2.Sobel(src_gray, cv2.CV_64F, 0, 1, 3)

abs_gray_x = cv2.convertScaleAbs(grad_x)
abs_gray_y = cv2.convertScaleAbs(grad_y)

grad = cv2.addWeighted(abs_gray_x, 0.5, abs_gray_y, 0.5, 0)

lap = cv2.Laplacian(src_gray, cv2.CV_64F, 3)
result = cv2.convertScaleAbs(lap)

canny = cv2.Canny(src_gray, 100, 200)

plt.subplot(131), plt.imshow(src)
plt.subplot(132), plt.imshow(canny)
plt.subplot(133), plt.imshow(result)
plt.show()