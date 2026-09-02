import cv2
import numpy as np

img = cv2.imread('images/sample_image.png')
if img is None:
    img = cv2.imread('../images/sample_image.png')

B = img[:, :, 0].astype(np.float64)
G = img[:, :, 1].astype(np.float64)
R = img[:, :, 2].astype(np.float64)
gray = ((R + G + B) / 3).astype(np.uint8)

size = int(input('Enter odd filter size: '))
padding = input('Enter padding method (zero/replicate): ').strip().lower()
pad = size // 2
h, w = gray.shape

padded = np.zeros((h + 2 * pad, w + 2 * pad), dtype=np.float64)
padded[pad:pad+h, pad:pad+w] = gray

if padding == 'replicate':
    padded[:pad, pad:pad+w] = gray[0, :]
    padded[pad+h:, pad:pad+w] = gray[-1, :]
    padded[:, :pad] = padded[:, pad:pad+1]
    padded[:, pad+w:] = padded[:, pad+w-1:pad+w]

kernel = np.ones((size, size), dtype=np.float64) / (size * size)
output = np.zeros((h, w), dtype=np.float64)

for i in range(h):
    for j in range(w):
        region = padded[i:i+size, j:j+size]
        output[i, j] = np.sum(region * kernel)

output = np.clip(output, 0, 255).astype(np.uint8)

cv2.imshow('Original Image', gray)
cv2.imshow('Averaging Filter', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
