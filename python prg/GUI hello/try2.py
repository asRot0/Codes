from tkinter import *


# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to GeekForGeeks")
root.geometry('350x200')
root.iconbitmap(r'pic_icon/VIRUS3.ico')
# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

# adding a label to the root window
lbl = Label(root, text = "Are you a Geek?")
lbl.grid()


# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =1, row =0)


# function to display user text when



# button is clicked
def clicked():
	def clicked():
		top = Toplevel()
		top.title('top')
		top.geometry('200x100')

		res = "You wrote " + txt.get()

		lbl2=Label(top, text='')
		lbl2.grid()
		#str(txt.get())

		#if aaa==NONE:
		#	lbl2.configure(text=res)
		lbl2.configure(text=res)
		top.resizable(0,0)
	Button(command=clicked())




# button widget with red color text inside
btn = Button(root, text = "Click me" ,
			fg = "red", command=clicked)

btn.grid(column=2, row=0)
root.mainloop()
