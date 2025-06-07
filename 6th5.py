import cv2

video = cv2.VideoCapture(r"D:\Computer Vision\TH\TH01\video.mp4")

while True: 
    ret, frame = video.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == ord('x'):
        cv2.imwrite(r"D:\Computer Vision\CodeLesson\save.jpg", frame)
        break
    elif cv2.waitKey(10) == ord('q'): break
cv2.destroyAllWindows