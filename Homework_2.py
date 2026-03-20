import random

def random_num():
    return random.randint(1,100)
target=random_num()

while True:
    target=random_num()
    
    while True:
        n=int(input("1~100 number Enter : "))
        
        if n==target :
            print("정답인",target,"입니다")

            while True:
                repeat = input("한번 더 하고싶다면 Y를, 종료하고 싶다면 N을 누르세요.")
                if repeat in ['y','Y','n','N']:
                    break
                else :
                    print("잘못된 입력입니다.")

            if repeat in ['n','N']:
                print("프로그램이 종료됩니다.")
                break
            else :
                target=random_num()
                
        elif n < target :
            print("더 큰 숫자를 입력하세요.")

        elif n > target : 
            print("더 작은 숫자를 입력하세요.")

#up down 게임 구동장치