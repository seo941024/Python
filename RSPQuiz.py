import random

com_ran = ["Rock", "Scissors", "Paper" ]

count=5
u_score=0
c_score=0

while True :
    computer = random.randint(0,2)
    
    while True :
        user = int(input("0.Rock , 1.Scissors, 2.Paper input your number on 0,1,2 : "))

        if (user == computer) :
            count -= 1
            print("컴퓨터는 ", com_ran[computer] ,",유저는 ", com_ran[user],"입니다.")
            print("무승부 입니다.\n횟수는 ", count, "회 남았습니다.")
            break

        elif (user == 0 and computer ==1) or (user == 1 and computer ==2) or (user == 2 and computer ==0):
            count -= 1
            u_score += 1
            print("컴퓨터는 ", com_ran[computer] ,",유저는 ", com_ran[user],"입니다.")
            print("유저의 승리입니다. 승점 1점을 획득하셨습니다. \n총 승점 ", u_score,"점 입니다."\
                  "\n횟수는 ", count, "회 남았습니다.")
            break

        else : 
            count -= 1
            c_score += 1
            print("컴퓨터는 ", com_ran[computer] ,",유저는 ", com_ran[user],"입니다.")
            print("컴퓨터의 승리입니다. \n총 승점 ", u_score,"점 입니다." \
                "\n횟수는 ", count, "회 남았습니다.")
            break

    if u_score >= 3 :
        print("축하합니다. 유저의 승리입니다!")
        break

    elif c_score >= 3 :
        print("컴퓨터가 승리했습니다.")
        break

    elif count == 0 and (c_score < 3 and u_score < 3) :
        print("횟수가 전부 소모 되었습니다.")
        break
