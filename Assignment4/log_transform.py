import cv2
import numpy as np

img = cv2.imread('images/sample_image.png')
if img is None:
    img = cv2.imread('../images/sample_image.png')

B = img[:, :, 0].astype(np.float64)
G = img[:, :, 1].astype(np.float64)
R = img[:, :, 2].astype(np.float64)
gray = ((R + G + B) / 3).astype(np.uint8)

c = 1
r = gray.astype(np.float64) / 255.0
log_image = c * np.log(1 + r)
log_image = (log_image / log_image.max() * 255).astype(np.uint8)

cv2.imshow('Original Grayscale Image', gray)
cv2.imshow('Log Transformed Image', log_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
