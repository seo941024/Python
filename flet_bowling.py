import flet as ft


# ================= GAME LOGIC =================
class BowlingGame:
    def __init__(self):
        self.throw_list = []

    def add_throw(self, pins):
        self.throw_list.append(pins)

    def calculate_live_scores(self):
        scores = []
        total = 0
        i = 0

        for _ in range(10):
            if i >= len(self.throw_list):
                break

            if self.throw_list[i] == 10:
                if i+2 >= len(self.throw_list):
                    break
                total += 10 + self.throw_list[i+1] + self.throw_list[i+2]
                scores.append(total)
                i += 1

            else:
                if i+1 >= len(self.throw_list):
                    break

                if self.throw_list[i] + self.throw_list[i+1] == 10:
                    if i+2 >= len(self.throw_list):
                        break
                    total += 10 + self.throw_list[i+2]
                else:
                    total += self.throw_list[i] + self.throw_list[i+1]

                scores.append(total)
                i += 2

        return scores

    # ================= VIEW (UI용 변환) =================
    def format_frames(self):
        frames = []
        i = 0

        for frame in range(10):
            if i >= len(self.throw_list):
                frames.append(" ")

            elif frame == 9:
                result = []
                while i < len(self.throw_list):
                    if self.throw_list[i] == 10:
                        result.append("X")
                        i += 1
                    else:
                        if i+1 < len(self.throw_list):
                            a = self.throw_list[i]
                            b = self.throw_list[i + 1]

                            if a+b == 10:
                                result.append(f"{a}/")
                            else:
                                result.append(f"{a}-{b}")

                            i += 2
                        else:
                            result.append(str(self.throw_list[i]))
                            i += 1

                frames.append(" ".join(result))

            else:
                if self.throw_list[i] == 10:
                    frames.append("X")
                    i += 1
                else:
                    if i+1 < len(self.throw_list):
                        a = self.throw_list[i]
                        b = self.throw_list[i + 1]

                        if a+b == 10:
                            frames.append(f"{a}/")
                        else:
                            frames.append(f"{a}-{b}")

                        i += 2
                    else:
                        frames.append(str(self.throw_list[i]))
                        i += 1

        return frames


# ================= UI =================
def main(page: ft.Page):
    page.title = "🎳 Bowling Alley"
    page.window_width = 700

    game = BowlingGame()

    input_box = ft.TextField(label="핀 수 (0~10)", width=200)
    frame_view = ft.Text()
    score_view = ft.Text(size=18)
    raw_view = ft.Text()

    def update():
        frames = game.format_frames()
        scores = game.calculate_live_scores()

        frame_view.value = " | ".join(frames)
        score_view.value = f"최종 점수: {scores[-1] if scores else 0}"
        raw_view.value = f"DEBUG: {game.throw_list}"

        page.update()

    def add_throw(e):
        if input_box.value and input_box.value.isdigit():
            val = int(input_box.value)

            if 0 <= val <= 10:
                game.add_throw(val)
                input_box.value = ""
                update()

    page.add(
        ft.Text("🎳 REAL BOWLING GAME", size=22),
        input_box,
        ft.ElevatedButton("투구!", on_click=add_throw),
        ft.Text("프레임"),
        frame_view,
        score_view,
        raw_view
    )


ft.app(target=main)