import cv2

img = cv2.imread(r"D:\Computer Vision\img\8.png")

#tạo cửa sổ mới
cv2.namedWindow('Trackbar')

#hàm truyền độ sáng và tương phản
def get_alpha(pos):
    global tuongphan
    tuongphan = pos
def get_beta(pos):
    global dosang
    dosang = pos

#thiết lập giá trị ban đầu
tuongphan = 1
dosang  = 0

#Tạo trackbar
cv2.createTrackbar('alpha', 'Trackbar', 1, 3, get_alpha)
cv2.createTrackbar('beta', 'Trackbar', 0, 100, get_beta)

#vòng lặp
while True:
    new = cv2.convertScaleAbs(img, alpha=tuongphan, beta=dosang)
    cv2.imshow('Trackbar', new)
    if (cv2.waitKey(10)) == ord('q') :break
cv2.destroyAllWindows