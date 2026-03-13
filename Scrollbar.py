from tkinter import*

root = Tk()
root.title("Scrollbar")
root.geometry("640x480")
root.resizable(True, True)

frame = Frame(root)

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox =  Listbox(frame, yscrollcommand=scrollbar.set)
for i in range(0, 100):
    listbox.insert(i, str(i+1))
listbox.pack(side="left")

scrollbar["command"] = listbox.yview


frame.pack()
root.mainloop()