import cv2

img = cv2.imread(r"D:\Computer Vision\img\8.png")

cv2.namedWindow('trackbar')

def get_alpha(pos):
	global tuongphan
	tuongphan = pos/10
def get_beta(pos):
	global dosang
	dosang = pos

tuongphan = 1
dosang = 0

cv2.createTrackbar('alpha', 'trackbar', 10, 30, get_alpha)
cv2.createTrackbar('meta', 'trackbar', 0, 100, get_beta)

while True:
	new = cv2.convertScaleAbs(img, alpha=tuongphan, beta=dosang)
	cv2.imshow('trackbar', new)
	if cv2.waitKey(10) == ord('p') : break
cv2.destroyWindow()