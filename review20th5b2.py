import cv2

video = cv2.VideoCapture(r"D:\Computer Vision\CodeLesson\video.mp4")

while True:
    ret, frame = video.read()
    cv2.imshow('video', frame)
    if cv2.waitKey(10) == ord('q') : break
    if cv2.waitKey(10) == ord('x'):
        cv2.imwrite('img.jpg', frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
video.release()
laplace = cv2.Laplacian(gray, cv2.CV_64F)
laplace = cv2.convertScaleAbs(laplace)
cv2.imshow('laplace', laplace)
cv2.imwrite('laplace.jpg', laplace)

cv2.destroyAllWindows