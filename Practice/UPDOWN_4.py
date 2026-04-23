import random

def ran_num_imp():
    return(random.randint(1,100))

ran_num=ran_num_imp()
a=5

while True :

    print(ran_num)
    n = int(input("숫자를 입력해주세요. : "))

    if n == ran_num :
        print("정답입니다.")
        
        while True :
            n = input("다시 시작하려면 y,n")
            if n in ['n','N','y','Y']:
                break
            else : 
                print("y나 n을 눌러주세요.")

        if n in ['n','N']:
            print("프로그램이 종료됩니다.")
            break

        else :
            ran_num=ran_num_imp()
            a = 5
            continue
    
    else :
        a -= 1
        if n > ran_num :
            print ("더 낮은 숫자를 입력해주세요. ")

        else :
            print ("더 높은 숫자를 입력해주세요. ")

        print("기회가 ",a,"번 남으셨습니다.")

        if a < 1 :
            print("기회를 전부 소진하셨습니다.")
            
            while True :
                n = input("다시 시작하려면 y,n")
                if n in ['n','N','y','Y']:
                    break
                else : 
                    print("y나 n을 눌러주세요.")

            if n in ['n','N']:
                print("프로그램이 종료됩니다.")
                break
            else :
                ran_num = ran_num_imp()
                a = 5
                continue