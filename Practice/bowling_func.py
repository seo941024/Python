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

            # ================= 10프레임 =================
            if frame == 9:
                result = []
                roll_in_frame = 0  # ⭐ 핵심

                while i < len(self.throw_list):
                    val = self.throw_list[i]

                    # 스트라이크
                    if val == 10:
                        result.append("❌")
                        i += 1
                        roll_in_frame += 1
                        continue

                    if i + 1 < len(self.throw_list):
                        nxt = self.throw_list[i + 1]

                        # ⭐ 2번째 투구일 때만 스페어 허용
                        if roll_in_frame == 1 and val + nxt == 10:
                            result.append(str(val))
                            result.append("/")
                            i += 2
                            roll_in_frame += 2
                            continue

                    # 일반
                    result.append("-" if val == 0 else str(val))
                    i += 1
                    roll_in_frame += 1

                display_score.append(" ".join(result))

            # ================= 일반 프레임 =================
            else:
                # 스트라이크
                if self.throw_list[i] == 10:
                    display_score.append("❌")
                    i += 1

                else:
                    if i + 1 < len(self.throw_list):

                        first = self.throw_list[i]
                        second = self.throw_list[i+1]

                        # 스페어
                        if first + second == 10:
                            a = "-" if first == 0 else str(first)
                            display_score.append(f"{a} /")
                        else:
                            a = "-" if first == 0 else str(first)
                            b = "-" if second == 0 else str(second)
                            display_score.append(f"{a} {b}")

                        i += 2
                    else:
                        display_score.append("-" if self.throw_list[i] == 0 else str(self.throw_list[i]))
                        i += 1

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

