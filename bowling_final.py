# ================= 점수 계산 =================
def calculate_live_scores(throw_list):
    scores = []
    total = 0
    i = 0

    for _ in range(10):
        if i >= len(throw_list):
            break

        # 스트라이크
        if throw_list[i] == 10:
            if i + 2 >= len(throw_list):
                break
            total += 10 + throw_list[i+1] + throw_list[i+2]
            scores.append(total)
            i += 1

        # 스페어 / 일반
        else:
            if i + 1 >= len(throw_list):
                break

            if throw_list[i] + throw_list[i+1] == 10:
                if i + 2 >= len(throw_list):
                    break
                total += 10 + throw_list[i+2]
            else:
                total += throw_list[i] + throw_list[i+1]

            scores.append(total)
            i += 2

    return scores


# ================= 화면 출력 =================
def show_display(throw_list):
    display_score = []
    i = 0

    for frame in range(10):
        if i >= len(throw_list):
            display_score.append(" ")
            continue

        # 마지막 프레임
        if frame == 9:
            result = []

            # 10프레임은 throw_list 끝까지 읽되 "같은 프레임만" 처리
            while i < len(throw_list):

                val = throw_list[i]

                # 스트라이크
                if val == 10:
                    result.append("❌")
                    i += 1
                    continue

                # 스페어 판단 (다음 공이 같은 프레임이면)
                if i + 1 < len(throw_list):
                    next_val = throw_list[i + 1]

                    if val + next_val == 10:
                        result.append(str(val))
                        result.append("/")
                        i += 2
                        continue

                # 일반
                result.append("-" if val == 0 else str(val))
                i += 1

            display_score.append(" ".join(result))

        # 일반 프레임
        else:
            if throw_list[i] == 10:
                display_score.append("❌")
                i += 1
            else:
                if i+1 < len(throw_list) and throw_list[i] + throw_list[i+1] == 10:
                    display_score.append(f"{throw_list[i]} /")
                elif i+1 < len(throw_list):
                    a = "-" if throw_list[i] == 0 else throw_list[i]
                    b = "-" if throw_list[i+1] == 0 else throw_list[i+1]

                    display_score.append(f"{a} {b}")
                    
                else:
                    display_score.append(f"{fmt(throw_list[i])} —")
                i += 2

    return display_score
# 안전한 입력값을 위한 함수 (LLM 참조)
def fmt(val):
    if val is None:
        return " "
    if val == 10:
        return "❌"
    if val == 0:
        return "-"
    return str(val)

# ================= 실시간 보드 출력 =================
def print_live_board(throw_list):
    frames = show_display(throw_list)
    scores = calculate_live_scores(throw_list)

    print("\n======================================")
    print("프레임:", " | ".join(frames))

    score_line = []
    for i in range(10):
        if i < len(scores):
            score_line.append(f"{scores[i]:3}")
        else:
            score_line.append(" — ")  # 아직 미확정

    print("점수  :", " | ".join(score_line))
    print("======================================\n")


# ================= 입력 =================
throw_list = []

# 1~9 프레임
for i in range(9):
    pin = 10

    first = int(input(f"{i+1}라운드 첫 투구 (0부터 {pin}까지의 숫자를 입력하세요): "))
    throw_list.append(first)
    print_live_board(throw_list)

    if first != 10:
        second = int(input(f"{i+1}라운드 두 번째 투구 (0부터 {pin-first}까지의 숫자를 입력하세요): "))
        throw_list.append(second)
        print_live_board(throw_list)


# 10프레임
first = int(input("10라운드 첫 투구 (0부터 10까지의 숫자를 입력하세요): "))
throw_list.append(first)
print_live_board(throw_list)

second = int(input(f"10라운드 두 번째 투구 (0부터 {10 if first == 10 else 10-first}까지의 숫자를 입력하세요): "))
throw_list.append(second)
print_live_board(throw_list)

if first == 10 or first + second == 10:
    third = int(input("10라운드 보너스 투구 (0부터 10까지의 숫자를 입력하세요): "))
    throw_list.append(third)
    print_live_board(throw_list)


# ================= 최종 =================
final_scores = calculate_live_scores(throw_list)
print(f"최종 점수: {final_scores[-1]}", final_scores)