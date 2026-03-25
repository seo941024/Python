from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Python GUI - CheckButton")
root.geometry("640x480+0+0")
root.resizable(True, True)

def show():
    print("item1: %d, \nitem2: %d, \nitem3: %d\m" % (variety1.get(),\
                        variety2.get(), variety3.get()))
    messagebox.showinfo("Button Clicked", "item1: {0},\nitem2: {1},\
                        \nitem3: {2}\n".format(variety1.get(), variety2.get(), variety3.get()))

variety1 = IntVar()
variety2 = IntVar()
variety3 = IntVar()    

bt1 = Checkbutton(root, text="item1", variable=variety1)
bt2 = Checkbutton(root, text="item2", variable=variety2)
bt3 = Checkbutton(root, text="item3", variable=variety3)

bt1.pack()
bt2.pack()
bt3.pack()

button = Button(root, width=10, text="show", overrelief="solid", command=show)
button.pack()

def selcetall():
    bt1.select()
    bt2.select()
    bt3.select()

def deselectall():
    bt1.deselect()
    bt2.deselect()
    bt3.deselect()

buttonSelectall = Button(root, width=10, text="select all", \
    overrelief="solid", command=selcetall)
buttonDeselectall = Button(root, width=10, text="deselect all", \
    overrelief="solid", command=deselectall)
buttonSelectall.pack()
buttonDeselectall.pack()

root.mainloop()