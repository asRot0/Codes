import cv2
import numpy as np
import os
from tkinter import *
from tkinter import filedialog
import imutils
'''
def dodge(front,back):
    result=front*255/(255-back)
    result[result>255]=255
    result[back==255]=255
    return result.astype(‘uint8’)
''''''
def dodge(front, back):
    result= front*255/(255-back)
    result[result>255]=55555
    result[back==255]=5555
    return result.astype('uint8')
'''

def dodge(x,y):
    img=cv2.divide(x, 255 - y, scale=256)
    return img


path2=os.getcwd()
print(path2)
Tk().withdraw()
path3=filedialog.askopenfilename()
print(path3)
path=r'pic_list/girl1.png'
img = cv2.imread(path3)

imgshape=img.shape
imgheight= imgshape[0]
imgweight= imgshape[1]
print(imgshape)

gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invert= np.bitwise_not(gray)
#invert= 255-gray
blur= cv2.GaussianBlur(invert,(31,31),sigmaX=0, sigmaY=0)
if imgheight>900 or imgweight>800:
    gray=cv2.resize(gray, (700,800))
    blur=cv2.resize(blur,(700,800))
finalImg= dodge(blur,gray)
finalImg2= dodge(gray,blur)
finalImg2= imutils.resize(finalImg2, width=500)
#cv2.resizeWindow('img2', 20, 3)
#cv2.namedWindow('img', cv2.WINDOW_GUI_NORMAL)
#cv2.imshow('invert', invert)
#cv2.imshow('blur', blur)
cv2.imshow('img', finalImg)
cv2.imshow('img2',finalImg2)
#cv2.imshow('invert2', invert2)

cv2.waitKey(0)
cv2.destroyAllWindows()
