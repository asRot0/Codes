import cv2
import numpy as np

path= r'../pic_list/girl1.png'
pic= cv2.imread(path)

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


kernel= np.ones((3,3), np.uint8)
canny= cv2.Canny(pic, 80, 180)
dilation= cv2.dilate(canny, kernel, iterations=1)
erode= cv2.erode(dilation, kernel, iterations=1)


img= np.zeros((512,512,3), np.uint8)
img2= np.ones((512,512))
img[:]= 255,200,0
#im1= cv2.imshow('zero', img)
#im2= cv2.imshow('ones', img2)

'''
im3= cv2.imshow('pic', pic)
im4= cv2.imshow('canny', canny)
im5= cv2.imshow('dilation', dilation)
im6= cv2.imshow('erode', erode)
'''
imgStack = stackImages(0.3,([pic,canny,dilation],[pic,erode,canny]))
cv2.imshow("Stacked Images", imgStack)

cv2.waitKey(0)
