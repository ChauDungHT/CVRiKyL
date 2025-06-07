import cv2

video = cv2.VideoCapture(r"D:\Computer Vision\TH\TH03\video.mp4")

gray_mode = False
while True:
    ret, frame = video.read()
    if gray_mode: 
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        cv2.imshow('Video', gray_frame)
    else: cv2.imshow('Video', frame)
    if cv2.waitKey(10) == ord('g') : gray_mode = not gray_mode
    if cv2.waitKey(10) == ord('s') : cv2.imwrite(r"D:\Computer Vision\CodeLesson\frame.jpg")
    elif cv2.waitKey(10) == ord('q') : break
video.release()
cv2.destroyAllWindows