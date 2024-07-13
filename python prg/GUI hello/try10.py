from tkinter import *

root = Tk()
root.geometry('500x500')
root.configure(bg='#AAAAAA')

def popup(event):
    try:
        my_menu.tk_popup(event.x_root, event.y_root)
    finally:
        my_menu.grab_release()

def New():
    pass

my_menu=Menu(root,tearoff=False)
my_menu.add_command(label='new',command=New)
my_menu.add_separator()
my_menu.add_command(label='exit',command=root.quit)


root.bind("<Button-3>", popup)


root.mainloop()