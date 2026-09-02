import cv2
import numpy as np

img = cv2.imread('images/sample_image.png')
if img is None:
    img = cv2.imread('../images/sample_image.png')

B = img[:, :, 0].astype(np.float64)
G = img[:, :, 1].astype(np.float64)
R = img[:, :, 2].astype(np.float64)

gray = ((R + G + B) / 3).astype(np.uint8)

threshold = int(input('Enter threshold value (0-255): '))

binary = np.zeros_like(gray)
binary[gray >= threshold] = 255

cv2.imshow('Grayscale Image', gray)
cv2.imshow('Binary Image', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
