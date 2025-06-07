import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"D:\Computer Vision\img\test.jpg")
src = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gay = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)

grad_x = cv2.Sobel(gay, cv2.CV_64F, 1, 0, 3)
grad_y = cv2.Sobel(gay, cv2.CV_64F, 0, 1, 3)
abs_grad_x = cv2.convertScaleAbs(grad_x)
abs_grad_y = cv2.convertScaleAbs(grad_y)

grad = cv2.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)

laplace = cv2.Laplacian(gay, cv2.CV_64F, 3)
rs = cv2.convertScaleAbs(laplace)

canny = cv2.Canny(gay, 600, 200)

plt.subplot(221), plt.imshow(src)
plt.subplot(222), plt.imshow(gay, cmap='gray')
plt.subplot(223), plt.imshow(rs, cmap='gray')
plt.subplot(224), plt.imshow(canny, cmap='gray')
plt.show()