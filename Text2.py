from tkinter import *

root = Tk()
root.title("Text Box")
root.geometry("640x480+0+0")
root.resizable(True, True)

text= Text(root)
text.insert(INSERT, "Hello World\n")
text.insert(END, "Pyhon GUI Tkinter")
text.pack()

text.tag_add("here", "1.0", "1.5")
text.tag_add("start", "1.10", "1.17")
text.tag_config("here", background="yellow", foreground="red")
text.tag_config("start", background="black", foreground="white")

root.mainloop()
