# import tkinter module
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *

# creating main tkinter window/toplevel
master = Tk()

# this will create a label widget
l1 = Label(master, text = "Height")
l2 = Label(master, text = "Width")

# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2.grid(row = 1, column = 0, sticky = W, pady = 2)

# entry widgets, used to take entry from user
e1 = Entry(master)
e2 = Entry(master)

# this will arrange entry widgets
e1.grid(row = 0, column = 1, pady = 2)
e2.grid(row = 1, column = 1, pady = 2)

# checkbutton widget
c1 = Checkbutton(master, text = "Preserve")
c1.grid(row = 2, column = 0, sticky = W, columnspan = 2)

filename=askopenfilename()
print(filename)


# adding image (remember image should be PNG and not JPG)
img = PhotoImage(file = filename).subsample(10,10)
#img1 = img.subsample(10,10)

# setting image with the help of label
#image = img1
Label(master, image = img).grid(row = 0, column = 2,
	columnspan = 2, rowspan = 2, padx = 5, pady = 5)

# button widget
b1 = Button(master, text = "Zoom in")
b2 = Button(master, text = "Zoom out")

# arranging button widgets
b1.grid(row = 2, column = 2, sticky = E)
b2.grid(row = 2, column = 3, sticky = E)

# infinite loop which can be terminated
# by keyboard or mouse interrupt
mainloop()
