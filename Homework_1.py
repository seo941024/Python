import tkinter

import random

def random_num():
    return random.randint(1,100)
target=random_num()
print(target)

window=tkinter.Tk()
window.title("Up Down Game")
window.geometry("640x480+0+0")
window.resizable(True, True)

tkinter.Label(window, text="1부터 100까지 중 숫자를 입력해 주세요!!!", width=500, relief="solid").pack()
answer_entry = tkinter.Entry(window)
answer_entry.pack()

result_label=tkinter.Label(window, text="")
result_label.pack()

submit = tkinter.Button(window, text = "submit")
submit.pack()

restart = tkinter.Button(window, text = "Restart")
restart.pack()

while True:
    n=int(entry.get(("1~100 number Enter : ")))
    
    if n==target :
        label.config(text="정답인",text=target,text="입니다")

        while True:
            repeat = input("한번 더 하고싶다면 Y를, 종료하고 싶다면 N을 누르세요.")
            if repeat in ['y','Y','n','N']:
                break
            else :
                print("잘못된 입력입니다.")

        if repeat in ['n','N']:
            print("프로그램이 종료됩니다.")
            break

    elif n < target :
        print("더 큰 숫자를 입력하세요.")

    elif n > target : 
        print("더 작은 숫자를 입력하세요.")

#updown game
'''정수를 입력.
    그 숫자가 1,100사이의 숫자인지 확인.
    맞을 시, 입력된 값이 random 수보다 높으면 Down하세요.
    낮으면 Up 하세요.출력
    정답이면 정답입니다! 와 함께, 한 번 더 할거면 Y, 아니면 N 입력
    Y 누를시 다시 1로 돌아감. 아니면 break.    '''
#지금 해야할 것 > 이걸 함수로 정의한다.

window.mainloop()