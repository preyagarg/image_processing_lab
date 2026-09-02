import cv2
import numpy as np

img = cv2.imread('images/sample_image.png')
if img is None:
    img = cv2.imread('../images/sample_image.png')

B = img[:, :, 0].astype(np.float64)
G = img[:, :, 1].astype(np.float64)
R = img[:, :, 2].astype(np.float64)
gray = ((R + G + B) / 3).astype(np.uint8)

input_min = int(input('Enter lower input intensity: '))
input_max = int(input('Enter upper input intensity: '))
output_min = int(input('Enter lower output intensity: '))
output_max = int(input('Enter upper output intensity: '))

stretched = gray.astype(np.float64)
stretched = output_min + ((stretched - input_min) * (output_max - output_min) / (input_max - input_min))
stretched = np.clip(stretched, 0, 255).astype(np.uint8)

cv2.imshow('Original Grayscale Image', gray)
cv2.imshow('Contrast Stretched Image', stretched)
cv2.waitKey(0)
cv2.destroyAllWindows()
