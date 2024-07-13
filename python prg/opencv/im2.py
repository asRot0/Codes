# import Opencv 
import cv2 

# import Numpy 
import numpy as np 

# read a image using imread 
img = cv2.imread('../pic_list/images (2).jpeg')

# creating a Histograms Equalization 
# of a image using cv2.equalizeHist() 
#equ = cv2.equalizeHist(img) 
flip=cv2.flip(img, 2)

# stacking images side-by-side 
res = np.hstack((img, flip)) 

# show image input vs output 
cv2.imshow('image', res) 
#cv2.imwrite('pic_list/flip2.jpeg',res)

cv2.waitKey(0) 
cv2.destroyAllWindows() 
