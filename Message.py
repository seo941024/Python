from tkinter import *

root = Tk()
root.title("Message")
root.geometry("640x480+0+0")
root.resizable(True, True)

message = Message(root, text="메세지 내용1\n메세지 내용2", width=320, relief="solid")
message.pack()

root.mainloop()