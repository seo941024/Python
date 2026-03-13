from tkinter import *

root = Tk()
root.title("Text Box")
root.geometry("640x480+0+0")
root.resizable(True, True)

text= Text(root)
text.insert(INSERT, "Hello World\n")
text.insert(END, "Pyhon GUI Tkinter")
text.pack()

root.mainloop()
