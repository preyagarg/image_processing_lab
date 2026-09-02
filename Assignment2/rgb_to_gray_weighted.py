import cv2
import numpy as np

img = cv2.imread('images/sample_image.png')
if img is None:
    img = cv2.imread('../images/sample_image.png')

r_weight = float(input('Enter weight for R: '))
g_weight = float(input('Enter weight for G: '))
b_weight = float(input('Enter weight for B: '))

if r_weight < 0 or g_weight < 0 or b_weight < 0 or r_weight > 1 or g_weight > 1 or b_weight > 1:
    print('Weights must be between 0 and 1')
elif abs((r_weight + g_weight + b_weight) - 1) > 0.0001:
    print('Sum of weights must be 1')
else:
    B = img[:, :, 0].astype(np.float64)
    G = img[:, :, 1].astype(np.float64)
    R = img[:, :, 2].astype(np.float64)

    gray = (r_weight * R + g_weight * G + b_weight * B).astype(np.uint8)

    cv2.imshow('Original Image', img)
    cv2.imshow('Weighted Grayscale Image', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
