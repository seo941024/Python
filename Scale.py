from tkinter import *

root = Tk()
root.title("Scale")
root.geometry("640x480+0+0")
root.resizable(True, True)

def select(event) :
    value = "값 : " + str(scale.get())
    label.config(text = value)

    #str 숫자를 문자열로 변환, scale.get() 슬라이더 현재값 가져오기

var1 = IntVar()

scale = Scale(root, variable=var1, orient="horizontal", showvalue=True, tickinterval=10, to=100, length=200, command=select)
scale.pack()

label = Label(root, text='0')
label.pack()

root.mainloop()