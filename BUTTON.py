from tkinter import *

root = Tk()

root.title("PYTHON GUI") #이름 설정
root.geometry("640x480+100+100") #창 크기 및 위치
root.resizable(True, True) #창 크기 변경 허용 여부

count = 0

def countplus(): #def - 함수정의, #countplus - 함수이름, () - 매개변수, : - 시작
    global count #global
    count += 1
    label.config(text=str(count))

def countminus():
    global count
    count -= 1
    label.config(text=str(count))

label = Label(root, text="0") #레이블 생성
label.pack()

button1 = Button(root, width=10, text="plus", overrelief="sunken", command=countplus)
button1.pack()

button2 = Button(root, width=10, text="minus", overrelief="sunken", command=countminus)
button2.pack()

root.mainloop() #메인화면에 표시