from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

def login():
    # Program to make a simple
    # login screen

    root = tk.Toplevel(top)
    root.title('Login ID')
    # setting the windows size
    root.geometry("300x200")

    # declaring string variable
    # for storing name and password
    name_var = tk.StringVar()
    passw_var = tk.StringVar()

    # defining a function that will
    # get the name and password and
    # print them on the screen
    def submit():
        name = name_entry.get()
        password = passw_entry.get()

        print("The name is : " + name)
        print("The password is : " + password)

        name_var.set("")
        passw_var.set("")

    # creating a label for
    # name using widget Label
    name_label = tk.Label(root, text='Username',
                          font=('calibre',
                                10, 'bold'))

    # creating a entry for input
    # name using widget Entry
    name_entry = tk.Entry(root,
                          textvariable=name_var, font=('calibre', 10, 'normal'))

    # creating a label for password
    passw_label = tk.Label(root,
                           text='Password',
                           font=('calibre', 10, 'bold'))

    # creating a entry for password
    passw_entry = tk.Entry(root,
                           textvariable=passw_var,
                           font=('calibre', 10, 'normal'),
                           show='*')

    # creating a button using the widget
    # Button that will call the submit function
    sub_btn = tk.Button(root, text='Submit',
                        command=submit)

    # placing the label and entry in
    # the required position using grid
    # method
    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1)
    passw_label.grid(row=1, column=0)
    passw_entry.grid(row=1, column=1)
    sub_btn.grid(row=2, column=0)

    # performing an infinite loop
    # for the window to display
    root.resizable(0,0)

def submit():

	month = monthchoosen.get()
	print(month)
	n.set('')


def donothing():
    #root=Toplevel(top)
    msg=messagebox.showwarning("Error", "Hello User, here is nothing.\n"
                                "press 'OK' button.")
    #msg.pack()
def radio():
    def sel():
        selection = "You selected the option " + str(var.get())
        label.config(text = selection)
        label.pack()

    #root = Tk()
    root=Toplevel(top)
    root.title('option')
    root.geometry('300x100')
    root.configure(bg='gray')
    root.resizable(0,0)
    #var = IntVar()

    R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
    command=sel,bg='gray')
    R1.pack( anchor = W)

    R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
    command=sel,bg='gray')
    R2.pack( anchor = W)

    R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
    command=sel,bg='gray')
    R3.pack( anchor = W)


    label = Label(root, relief=RAISED,bd=3,)
    #label.pack()
    #root.mainloop()

top= Tk()
top.title('try makE a GUI')
path=r'pic_icon\VIRUS4.ico'
top.iconbitmap(path)
top.geometry('1000x500')

var= IntVar()

menubar=Menu(top)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label='Radio', command=radio, activeforeground='cyan')
fileex = Menu(menubar, tearoff=0)
fileex.add_checkbutton(label="aa", onvalue=0)
fileex.add_checkbutton(label="as", onvalue=1)
fileex.add_checkbutton(label="ay", onvalue=0, offvalue=1)
fileex.add_command(label="exit", command=quit)

filemenu.add_cascade(label="Save", menu=fileex)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=top.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu)

menubar.add_cascade(label="Sign In", command=login)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

#label=Label(root)
#label.pack()
top.config(menu=menubar)

# Label
ttk.Label(top, text = "Select the Month :",
		font = ("Times New Roman", 10)).grid(column = 0,
		row = 15, padx = 10, pady = 25)

n = tk.StringVar()
monthchoosen = ttk.Combobox(top, width = 27,
							textvariable = n)

# Adding combobox drop down list
monthchoosen['values'] = (' January',
						' February',
						' March',
						' April',
						' May',
						' June',
						' July',
						' August',
						' September',
						' October',
						' November',
						' December')

monthchoosen.grid(column = 1, row = 15)
tk.Button(top,text='submit',command=submit).grid(column=0,row=16,padx=1,pady=3)

# Shows february as a default value
monthchoosen.current(0)
top.mainloop()