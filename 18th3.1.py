import cv2

img0 = cv2.imread(r'D:\Computer Vision\img\11.png')

img = cv2.cvtColor(img0, cv2.COLOR_BGR2RGB)

#Tạo trackbar
cv2.namedWindow('trackbar')

blur = 1

def get_blur(pos):
    global blur
    blur = pos
    if pos%2 == 0 : blur+=1

def get_medianBlur(pos):
cv2.createTrackbar('blur', 'trackbar', 1, 11, get_blur)

#Vòng lặp
while True:
    new = cv2.blur(img, (blur, blur))
    cv2.imshow('trackbar', new)
    if cv2.waitKey(10) == ord('q') : break
cv2.destroyAllWindows