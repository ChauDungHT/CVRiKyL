import cv2

img = cv2.imread(r"D:\Computer Vision\img\8.png")
#Tạo trackbar
cv2.namedWindow('Trackbar')
def get_alpha(pos):
    global tuongphan
    tuongphan = pos
def get_beta(pos):
    global dosang
    dosang = pos
cv2.createTrackbar('alpha','Trackbar',1,3, get_alpha)
#setup giá trị
tuongphan = 1
dosang = 0
#tạo Trackbar
while True:
    new = cv2.convertScaleAbs(img, alpha=tuongphan, beta=dosang)
    cv2.imshow('Trackbar', new)
    if cv2.waitKey(10) == ord('q') : break
cv2.destroyAllWindows