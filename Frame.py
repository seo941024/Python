from tkinter import *

root = Tk()
root.title("Frame")
root.geometry("640x480+0+0")
root.resizable(True, True)

frame1 = Frame(root, relief="solid", bd=2)
frame1.pack(side="left", fill="both", expand=True)

frame2 = Frame(root, relief="solid", bd=2)
frame2.pack(side="right", fill="both", expand=True)

label1 = Label(frame1, text='A')
label1.pack()

label2 = Label(frame2, text='B')
label2.pack()

root.mainloop()