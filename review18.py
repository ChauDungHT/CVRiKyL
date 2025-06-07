#18.	Đọc video, hiện thông tin kích thước, số khung hình trên giây của video. 
# Ấn phím s để lấy ra 1 ảnh từ video, đổi ảnh vừa lấy ra thành ảnh xám, lưu lại ảnh này.

import cv2

video = cv2.VideoCapture(r"D:\Computer Vision\review\video.mp4")
# Lấy kích thước ảnh
w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(video.get(cv2.CAP_PROP_FPS))
print(f'kích thước ảnh là: {w}x{h}')
print(f'số khung hình trên giây là: {fps}')

# Hiển thị video, lưu ảnh
while True:
    ret, frame = video.read()
    if not ret: break
    cv2.imshow('video', frame)
    if cv2.waitKey(10) == ord('q') : break
    if cv2.waitKey(10) == ord('s'):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('frame_gray.jpg', gray)
video.release()
cv2.destroyAllWindows