import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"D:\Computer Vision\img\9.png")
crop = img[0:50, 240:608]
change = 255 - crop

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
crop_rgb = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
change_rgb = cv2.cvtColor(change, cv2.COLOR_BGR2RGB)

plt.subplot(311), plt.imshow(img_rgb)
plt.subplot(312), plt.imshow(crop_rgb)
plt.subplot(313), plt.imshow(change_rgb)
plt.show()