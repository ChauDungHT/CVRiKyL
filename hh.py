import cv2

img_path = 'C:/Users/aceri/OneDrive/Pictures/image_1.jpg'

image = cv2.imread(img_path)

print(image.size)

cv2.imshow('Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()