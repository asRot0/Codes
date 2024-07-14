# Python program to explain cv2.imshow() method 

# importing cv2 
import cv2 

# path 
path = r'G:\zh\Saved Pictures\Desktop wallpapers\N1knY-aJ9jQ.jpg'
path1 = r'G:\zh\Saved Pictures\Desktop wallpapers\images (12).jpeg'

# Reading an image in grayscale mode 
image = cv2.imread(path, 0) 
image1 = cv2.imread(path1, 0) 

# Window name in which image is displayed 
window_name = 'image'

# Using cv2.imshow() method 
# Displaying the image 
cv2.imshow(window_name, image) 
cv2.waitKey(1000) 
cv2.imshow('image1', image1) 

# waits for user to press any key 
# (this is necessary to avoid Python kernel form crashing) 
cv2.waitKey(2000) 

# closing all open windows 
cv2.destroyAllWindows() 
