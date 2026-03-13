from tkinter import *

root = Tk()

root.title("PYTHON GUI") #이름 설정
root.geometry("640x480+100+100") #창 크기 및 위치
root.resizable(True, True) #창 크기 변경 허용 여부

label = Label(root, text='PYTHON GUI', width=100, height=50, fg="orange", relief="groove", bitmap="warning", compound="top") #레이블 생성
#bitmap - 라벨에 포함할 기본 이미지, compound - 라벨에 문자열과 이미지를 동시에 표시할 때 이미지의 위치

label.pack() #화면에 배치

root.mainloop() #메인화면에 표시