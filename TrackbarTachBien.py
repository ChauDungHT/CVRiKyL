import cv2

img = cv2.imread(r"D:\Computer Vision\img\1.png")
src = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gay = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)

def get_down(pos):
    global down
    down = pos

down = 50

cv2.namedWindow('Tach Bien')
cv2.createTrackbar('Up', 'Tach Bien', 0, 100, get_down)
while True:
    new = cv2.Canny(gay, down, (3*down))
    cv2.imshow('Tach Bien',new)
    if cv2.waitKey(10) == ord('q') : break
cv2.destroyAllWindows