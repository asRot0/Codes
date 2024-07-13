import cv2 
import numpy as np 
#'pic_list/images (9).jpeg'
FILE_NAME = '../pic_list/images (9).jpeg'
try: 
	# Read image from disk. 
	img = cv2.imread(FILE_NAME) 

	# Canny edge detection. 
	edges = cv2.Canny(img, 200, 200) 

	# Write image back to disk. 
	cv2.imshow('result', edges)
except IOError: 
	print ('Error while reading files !!!') 

if cv2.waitKey(0) & 0XFF==27:
	cv2.destroyAllWindows()