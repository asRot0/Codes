import cv2
import numpy as np

# arr = np.full((500, 500, 3), 255, dtype=np.uint8)
arr = np.zeros([250, 500, 3], dtype=np.uint8)
arr[:, :] = [255, 255, 255]
for i in range(10):
    arr[:, len(arr)//3 + i] = [0, 0, 255]
    arr[len(arr)//2 + i, :] = [0, 0, 255]

print(arr)

cv2.imshow('white pic', arr)
cv2.waitKey()
cv2.destroyAllWindows()