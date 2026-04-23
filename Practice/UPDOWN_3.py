import random
ran_num = random.randint(1,100)
print(ran_num)
a=5

while True :
    n = int(input("1부터 100 사이의 숫자를 입력해주세요. : "))
    if n == ran_num :
        print("정답입니다.")
        break
    
    elif n > ran_num :
        print("더 낮은 숫자를 입력해주세요.")
    else :
        print("더 높은 숫자를 입력해주세요.")
    
    if n != ran_num :
        a -= 1
        print("기회가 ",a,"번 남으셨습니다.")

    if a < 1 :
        print("기회를 전부 소진하셨습니다.\n게임이 종료됩니다.")
        break

