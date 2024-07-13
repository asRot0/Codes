from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import cv2
import imutils
import numpy as np
from PIL import ImageTk, Image

root = Tk()
root.title('Image convert')
root.geometry('650x500')
root.config(bg='#373936')


def img_path():
    filename = filedialog.askopenfilename()
    return filename


def open_img():
    path = img_path()

    if len(path) > 0:
        global panelA
        image = cv2.imread(path)
        image2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image2 = imutils.resize(image2, width=300)
        plwimg = Image.fromarray(image2)
        imgplw = ImageTk.PhotoImage(plwimg)
        if panelA is None:
            panelA = Label(image=imgplw)
            panelA.image = imgplw
            panelA.grid(row=2)
        else:
            panelA.configure(image=imgplw)
            panelA.image = imgplw

    def convert_img():
        global panelB
        aa = slt.get()

        if aa == 'gray':
            image3 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            image3 = imutils.resize(image3, width=300)
            plwimg2 = Image.fromarray(image3)
            imgplw2 = ImageTk.PhotoImage(plwimg2)
        if aa == 'rgb':
            image3 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image3 = imutils.resize(image3, width=300)
            plwimg2 = Image.fromarray(image3)
            imgplw2 = ImageTk.PhotoImage(plwimg2)
        if aa == 'canny':
            image3 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            image3 = imutils.resize(image3, width=300)
            image3 = cv2.Canny(image3, 50, 100)
            plwimg2 = Image.fromarray(image3)
            imgplw2 = ImageTk.PhotoImage(plwimg2)
        if aa == 'pancil':
            def dodge(x, y):
                img = cv2.divide(x, 255 - y, scale=256)
                return img

            image3 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            invert = np.bitwise_not(image3)
            blur = cv2.GaussianBlur(invert, (31, 31), sigmaX=0, sigmaY=0)
            finalImg = dodge(image3, blur)
            image3 = imutils.resize(finalImg, width=300)
            plwimg2 = Image.fromarray(image3)
            imgplw2 = ImageTk.PhotoImage(plwimg2)
        if aa == 'luv':
            image3 = cv2.cvtColor(image, cv2.COLOR_BGR2LUV)
            image3 = imutils.resize(image3, width=300)
            plwimg2 = Image.fromarray(image3)
            imgplw2 = ImageTk.PhotoImage(plwimg2)
        if aa == 'xyz':
            image3 = cv2.cvtColor(image, cv2.COLOR_BGR2XYZ)
            image3 = imutils.resize(image3, width=300)
            plwimg2 = Image.fromarray(image3)
            imgplw2 = ImageTk.PhotoImage(plwimg2)
        if aa == 'yuv':
            image3 = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
            image3 = imutils.resize(image3, width=300)
            plwimg2 = Image.fromarray(image3)
            imgplw2 = ImageTk.PhotoImage(plwimg2)
        if panelB is None:
            panelB = Label(image=imgplw2)
            panelB.image = imgplw2
            panelB.grid(row=2, column=2, columnspan=4)
        else:
            panelB.configure(image=imgplw2)
            panelB.image = imgplw2

    n.set('')

    btn2 = Button(root, text='convert', command=convert_img)
    btn2.grid(row=1, column=2, sticky='w')

    slt = Combobox(root, width=25, textvariable=n)
    slt['values'] = ('gray',
                     'rgb',
                     'canny',
                     'pancil',
                     'luv',
                     'xyz',
                     'yuv')

    slt.grid(column=3, row=1, padx=20, sticky='w')
    slt.current(0)


panelA = None
panelB = None
n = StringVar()
btn = Button(root, text='choose img', command=open_img)
btn.grid(row=1, sticky='w')
root.mainloop()