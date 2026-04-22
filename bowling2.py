'''
볼링 핀 10개.

count를 지정
random 모듈로 랜덤한 첫번째 숫자 구함. > n, 
그다음은 k = randint(1,10-n), k의 값이 0일때 아닐때로 스페어/일반공 판단.

던질 때 마다 count+=1, count가 1,2 일 때 기준으로 다른 조건으로 시작.
던지기 직전 count==0 으로 초기화.

일반 공/ 스페어 / 스트라이크
일반 공 count > 기본 2회
스트라이크 > 즉시 종료, 다음 공 점수 2회 2배.
스페어 > 다음 공 점수 1회 2배.

1~9 라운드.

다음 공이 스트라이크가 아닐시, 두배 적용 후 합산> 나머지 공 던지기
나머지 공 스페어 > 다음 공 점수 2배

모든 공을 던져서 score[i] = 10, score[i+1], score[i+2] 의 값을 score[i]에 저장해서 점수계산.
score[i]!=10

i=0
score[0]=10, >> 20

score[1]=5
score[2]=5, 스페어 >> 20+10+5 // 35

score[3]=5
score[4]=2, 35 + 7 

score[5]=8
score[6]=1

score[7]= 

i값의 변동으로는 스코어 기준을 잡을 수 없음.

i는 순차적으로 증가하고있음.

[[10,0] ,[2,8], [1,5], [0,10]]

2중 for로 안쪽까지 돌린다고 가정할 시ㅡ,
[i][0] = 10 일때
[i+1][j], [i+1][j+1]를

[i]에 더해서, 출력

[i][0]+[i][1] 즉 두 리스트의 합이 = 10 일때
[i+1][0] 의 값만 [i]의 합에 더 함
> sum(items) 그 리스트의 합을 구해줌.

10 라운드.
일반공은 2회가 끝. 스트라이크,스페어,시 3회째 기회가 주어짐.

최종 점수 산출 : 
'''

class BowlingGame:
    def __init__(self):
        self.throw_list = []

    # ================= 점수 계산 =================
    def calculate_live_scores(self):
        scores = []
        total = 0
        i = 0

        for _ in range(10):
            if i >= len(self.throw_list):
                break

            # 스트라이크
            if self.throw_list[i] == 10:
                if i + 2 >= len(self.throw_list):
                    break
                total += 10 + self.throw_list[i+1] + self.throw_list[i+2]
                scores.append(total)
                i += 1

            # 스페어 / 일반
            else:
                if i + 1 >= len(self.throw_list):
                    break

                if self.throw_list[i] + self.throw_list[i+1] == 10:
                    if i + 2 >= len(self.throw_list):
                        break
                    total += 10 + self.throw_list[i+2]
                else:
                    total += self.throw_list[i] + self.throw_list[i+1]

                scores.append(total)
                i += 2

        return scores

    # ================= 화면 출력 =================
    def show_display(self):
        display_score = []
        i = 0

        for frame in range(10):
            if i >= len(self.throw_list):
                display_score.append(" ")
                continue

            # 마지막 프레임
            if frame == 9:
                result = []

                while i < len(self.throw_list):
                    # 스트라이크
                    if self.throw_list[i] == 10:
                        result.append("❌")
                        i += 1

                    else:
                        # 두 번째 공 존재할 때
                        if i+1 < len(self.throw_list):
                            first = self.throw_list[i]
                            second = self.throw_list[i+1]

                            if first + second == 10:
                                result.append(str(first))
                                result.append("/")
                            else:
                                result.append(str(first))
                                result.append(str(second))

                            i += 2
                        else:
                            result.append(str(self.throw_list[i]))
                            i += 1

                display_score.append(" ".join(result))

            # 일반 프레임
            else:
                if self.throw_list[i] == 10:
                    display_score.append("❌")
                    i += 1
                else:
                    if i+1 < len(self.throw_list) and self.throw_list[i] + self.throw_list[i+1] == 10:
                        display_score.append(f"{self.throw_list[i]} /")
                    elif i+1 < len(self.throw_list):
                        display_score.append(f"{self.throw_list[i]} {self.throw_list[i+1]}")
                    else:
                        display_score.append(str(self.throw_list[i]))
                    i += 2

        return display_score

    # ================= 보드 출력 =================
    def print_live_board(self):
        frames = self.show_display()
        scores = self.calculate_live_scores()

        print("\n======================================")
        print("프레임:", " | ".join(frames))

        score_line = []
        for i in range(10):
            if i < len(scores):
                score_line.append(f"{scores[i]:3}")
            else:
                score_line.append("   ")

        print("점수  :", " | ".join(score_line))
        print("======================================\n")

    # ================= 투구 추가 =================
    def add_throw(self, pins):
        self.throw_list.append(pins)
        self.print_live_board()
        
# 1~9 프레임
game = BowlingGame()

for i in range(9):
    pin = 10

    first = int(input(f"{i+1}라운드 첫 투구 (0부터 {pin}사이의 숫자를 입력하세요): "))
    game.add_throw(first)

    if first != 10:
        second = int(input(f"{i+1}라운드 두 번째 투구 (0부터 {pin-first}사이의 숫자를 입력하세요): "))
        game.add_throw(second)

# 10프레임
first = int(input("10라운드 첫 투구 (0부터 10사이의 숫자를 입력하세요): "))
game.add_throw(first)

second = int(input(f"10라운드 두 번째 투구 (0부터 {10 if first == 10 else 10 - first}사이의 숫자를 입력하세요): "))
game.add_throw(second)
if first == 10 or first + second == 10:
    third = int(input("10라운드 보너스 투구 (0부터 10사이의 숫자를 입력하세요): "))
    game.add_throw(third)

# ================= 최종 점수 =================
final_scores = game.calculate_live_scores()
print(f"최종 점수 : {final_scores[-1]}점")
#중간에 5를 계속 입력하면 10프레임에 전부 스페어 모양으로 처리되는데 해결을 못했습니다