from tkinter import *

root = Tk()
root.title("List Box")
root.geometry("640x480+0+0")
root.resizable(True, True)

listbox = Listbox(root, height=0, selectmode="extended") #height - 리스트 박스의 높이, selectmode - 리스트 박스에서 항목을 선택하는 방법
listbox.insert(0, "Korean")
listbox.insert(0, "English")
listbox.insert(0, "Math")
listbox.insert(0, "Science")
listbox.pack()

root.mainloop()
