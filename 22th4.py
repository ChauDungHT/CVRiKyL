import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"D:\Computer Vision\img\test.jpg")
a, b = img.shape[:2]
print("Ngang: ", a, " Doc: ", b)

x, y = 0, 0
cao = int(input("Nhap chieu cao anh: "))
rong = int(input("Nhap chieu rong anh: "))

if cao<a and rong<b:
    crop = img[x:x+cao, y:y+rong]
    gauss = cv2.GaussianBlur(crop, (3, 3), 0)

    ret, threshold = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)

    plt.subplot(221), plt.imshow(img)
    plt.subplot(222), plt.imshow(crop)
    plt.subplot(224), plt.imshow(threshold)
    plt.subplot(223), plt.imshow(gauss)
    plt.show()
else:
    print("Nhap cao va rong nho hon!")