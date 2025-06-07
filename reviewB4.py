import cv2

img = cv2.imread(r"D:\Computer Vision\TH\logo-VinhUni.png")
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
canny = cv2.Canny(gray, 600, 200)