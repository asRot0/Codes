# importing required packages 
import tkinter 
from PIL import ImageTk, Image 
import os
import cv2

# creating main window 
root = tkinter.Tk() 

# loading the image 
#img = ImageTk.PhotoImage(Image.open("images (2).jpeg")) 

img =cv2.imread("images (2).jpeg")

gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

immg = Image.fromarray(gray)
imgg=ImageTk.PhotoImage(immg)

#show=cv2.imshow("Gray", gray)

# reading the image 
panel = tkinter.Label(root, image =imgg) 

# setting the application 

panel.pack(side = "bottom", fill = "both", 
		expand = "yes") 

# running the application 
root.mainloop() 
