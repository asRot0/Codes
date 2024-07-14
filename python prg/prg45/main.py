# Python code to reading an image using OpenCV 
import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../pic_list/images (11).jpeg',
                 cv2.IMREAD_GRAYSCALE)

cv2.imshow('image', img)
cv2.waitKey(1000)

# You can give path to the 
# image as first argument 
img = cv2.imread('../pic_list/images (9).jpeg', 0)

# will show the image in a window 
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF

# wait for ESC key to exit 
if k == 27:
    cv2.destroyAllWindows()

# wait for 's' key to save and exit 
elif k == ord('s'):
    cv2.imwrite('messigray.png', img)
    cv2.destroyAllWindows()
