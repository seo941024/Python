import random as rd

#핀, 스코어 2배 카운트, 최종 점수를 정수로 선언
pin = 0
final_score = 0
score_2x_count = 0

round = 1 #라운드(초기화 하면 안됨)

#스코어 2배 카운트를 주고, 카운트적용시 1회 차감하는 식으로 점수를 곱함.
#스페어는 스코어 2배 카운트의 값이 1, 스트라이크는 2로
#스페어는 처음 1타만 2배, 스트라이크는 다음에 치는 횟수 전부 2배

#라운드 시작 (9라운드 까지의 룰)
while round < 10:

     #핀의 개수 지정 및 초기화
    pin = 10
    #핀을 쓰러트리는 랜덤 함수 및 초기화
    rand_num = rd.randint(0, 10)
    #처음 공을 던짐
    remain_num = pin-rand_num
    #남은 핀
    final_num = rd.randint(0,remain_num)

    #2배 카운트로 score에 2배의 스코어를 저장.
    #한번 사용 시, 1씩 줄어들며 0이 되면 그냥 점수로 들어간다.
    #잘못된 계산법
    #그냥 2회의 투구의 점수를 return해서 처음 스트라이크 던진 값에 더하는 것이였음
    def apply_score(score):
        global final_score, score_2x_count
        if score_2x_count > 0:
            final_score += score * 2
            score_2x_count -= 1
        else:
            final_score += score

    # 스트라이크
    if remain_num == 0:
        print("Gratz! You hit Strike")

        #점수 보드판에 기록

        apply_score(rand_num)

        #다음 라운드로 가고, 다음 던지는 2회 점수 2배
        score_2x_count = 2
        round += 1

        print("[ X    ]")
        print(f"Score : {final_score+rand_num}\n")

    else:
        score = rand_num + final_num

        # 스페어
        if remain_num - final_num == 0:
            print("Gratz! You hit Spare")

            apply_score(score)

            score_2x_count = 1
            round += 1

            print(f"[ {rand_num}  / ]")
            print(f"Score : {final_score}\n")

        else:
            print("Nice!")

            apply_score(score)

            score_2x_count = 0
            round += 1

            print(f"[ {rand_num}  {final_num} ]")
            print(f"Score : {final_score}\n")


#라운드 10 특별 라운드

#일단 2회의 기능만 추가
#2회의 기회에서 한번이라도 clean이 될 시, 마지막 기회가 제공됨. 단, 점수는 그대로 합산이 되기 때문에 덜 복잡.

if round == 10:
    while True:

        pin = 10
        rand_num = rd.randint(0, 10)
        remain_num = pin - rand_num
        final_num = rd.randint(0, remain_num)

        def apply_score(score):
            global final_score, score_2x_count
            if score_2x_count > 0:
                final_score += score * 2
                score_2x_count -= 1
            else:
                final_score += score

        if rand_num == 10:
            apply_score(rand_num)

            rand_num1 = rd.randint(0, 10)

            if rand_num1 == 10:
                print("Gratz! You hit Strike")
                apply_score(rand_num1)

                rand_num2 = rd.randint(0, 10)
                apply_score(rand_num2)

                print(f"[ X  X  {'X' if rand_num2==10 else rand_num2} ]")
                print(f"Score : {final_score}\n")
                break

            else:
                print("Nice")
                apply_score(rand_num1)

                rand_num4 = rd.randint(0, 10)
                apply_score(rand_num4)

                print(f"[ X  {rand_num1}  { 'X' if rand_num4==10 else rand_num4 } ]")
                print(f"Score : {final_score}\n")
                break

        else:
            if remain_num - final_num == 0:
                print("Gratz! You hit Spare")

                apply_score(rand_num + final_num)

                rand_num3 = rd.randint(0, 10)
                apply_score(rand_num3)

                print(f"[ {rand_num}  /  { 'X' if rand_num3==10 else rand_num3 } ]")
                print(f"Score : {final_score}\n")
                break

            else:
                print("Nice!")

                apply_score(rand_num + final_num)

                print(f"[ {rand_num}  {final_num} ]")
                print(f"Score : {final_score}\n")
                break

print(f"최종 점수 : {final_score}")