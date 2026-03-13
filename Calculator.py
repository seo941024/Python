from tkinter import *

def calc(event):
    label.config(text="Total: "+str(eval(entry.get())))

root = Tk()

root.title("PYTHON GUI") #이름 설정
root.geometry("640x480+100+100") #창 크기 및 위치
root.resizable(True, True) #창 크기 변경 허용 여부

label = Label(root, text="0") #레이블 생성
label.pack() #화면에 배치

entry = Entry(root, width=30)
entry.bind("<Return>", calc)
entry.pack()

root.mainloop() #메인화면에 표시