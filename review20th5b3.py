import cv2
import numpy as np

cv2.namedWindow('Dich anh len xuong')
img = cv2.imread(r"D:\Computer Vision\CodeLesson\logo-VInhUni.png")

x, y = img.shape[:2]

def get_y(pos):
    global y
    y = pos - x
def get_x(pos):
    global x
    x = pos
x = 0
y = 0

cv2.createTrackbar('Dich: ', 'Dich anh len xuong', 0, 1000, get_y)

while True:
    M = np.float32([[1,0,x],[0,1,y]])
    new = cv2.warpAffine(img, M, (x, y))
    cv2.imshow('Dich anh len xuong', new)
    if cv2.waitKey(10) == ord('q'): break
    
cv2.destroyAllWindows