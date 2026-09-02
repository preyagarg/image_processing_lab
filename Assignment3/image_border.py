import cv2
import numpy as np

img = cv2.imread('images/sample_image.png')
if img is None:
    img = cv2.imread('../images/sample_image.png')

B = img[:, :, 0].astype(np.float64)
G = img[:, :, 1].astype(np.float64)
R = img[:, :, 2].astype(np.float64)
gray = ((R + G + B) / 3).astype(np.uint8)

threshold = int(np.mean(gray))
binary = np.zeros_like(gray)
binary[gray >= threshold] = 255

width = int(input('Enter border width in pixels: '))
gray_color = int(input('Enter grayscale border value (0-255): '))
binary_color = int(input('Enter binary border value (0 or 255): '))

h, w = gray.shape

gray_bordered = np.full((h + 2 * width, w + 2 * width), gray_color, dtype=np.uint8)
gray_bordered[width:width+h, width:width+w] = gray

binary_bordered = np.full((h + 2 * width, w + 2 * width), binary_color, dtype=np.uint8)
binary_bordered[width:width+h, width:width+w] = binary

cv2.imshow('Grayscale with Border', gray_bordered)
cv2.imshow('Binary with Border', binary_bordered)
cv2.waitKey(0)
cv2.destroyAllWindows()
