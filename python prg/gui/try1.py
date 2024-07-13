from tkinter import *
from tkinter import messagebox

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
top.title('try_1')

var= IntVar()
menubar=Menu(top)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label='Radio', command=radio, activeforeground='cyan')
filemenu.add_command(label="Save", command=donothing)
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

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

#label=Label(root)
#label.pack()
top.config(menu=menubar)
top.configure(bg='gray')
top.mainloop()