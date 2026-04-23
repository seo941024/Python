import flet as ft
import random
from Bowlingfletcomplete_class import *

# Auto용
def get_max_pins(game):
    throws = game.throw_list

    if len(throws) == 0:
        return 10

    i = 0
    frame = 0

    while frame < 9 and i < len(throws):
        if throws[i] == 10:
            i += 1
        else:
            i += 2
        frame += 1

    if i < len(throws):
        first = throws[i]
        if first != 10:
            return 10 - first

    return 10


def main(page: ft.Page):
    page.title = "🎳 Bowling System"
    page.bgcolor = "#051622"
    page.padding = 40
    page.width = 1200
    page.height = 700

    game = BowlingGame()

    score_grid = ft.Column(spacing=0, tight=True)

    error_text = ft.Text("", color="red", size=16)
    info_text = ft.Text("", color="lightgreen", size=16)

    def build_grid():
        frames_data = game.get_display_data()
        live_scores = game.calculate_live_scores()

        header_row = ft.Row(spacing=0, alignment="center")
        shots_row = ft.Row(spacing=0, alignment="center")
        total_row = ft.Row(spacing=0, alignment="center")

        for i in range(10):
            is_10 = (i == 9)
            w = 150 if is_10 else 90

            highlight = "#FF6B00" if i == len(live_scores) else "#1A374D"

            # 프레임 번호
            header_row.controls.append(
                ft.Container(
                    content=ft.Text(str(i+1), color="white", weight="bold", size=18),
                    width=w,
                    height=40,
                    bgcolor=highlight,
                    alignment=ft.Alignment(0, 0),
                    border=ft.border.all(2, "#333333"),
                )
            )

            # 투구칸
            shots = frames_data[i]
            num_s = 3 if is_10 else 2
            shot_inner = ft.Row(spacing=0)

            for s_idx in range(num_s):
                val = shots[s_idx] if s_idx < len(shots) else ""

                shot_inner.controls.append(
                    ft.Container(
                        content=ft.Text(
                            val,
                            color="white",
                            size=24 if val == "X" else 20,
                            weight="bold",
                        ),
                        width=w / num_s,
                        height=55,
                        alignment=ft.Alignment(0, 0),
                        border=ft.border.all(1, "#333333"),
                        bgcolor="#0B2447",
                    )
                )

            shots_row.controls.append(ft.Container(content=shot_inner, width=w))

            # 점수칸
            curr_score = str(live_scores[i]) if i < len(live_scores) else ""

            total_row.controls.append(
                ft.Container(
                    content=ft.Text(
                        curr_score,
                        color="#FFD700",
                        size=30,
                        weight="bold",
                    ),
                    width=w,
                    height=95,
                    alignment=ft.Alignment(0, 0),
                    border=ft.border.all(1, "#333333"),
                    bgcolor="#124559",
                )
            )

        score_grid.controls = [header_row, shots_row, total_row]

        # 통계
        if live_scores:
            total = live_scores[-1]
            avg = round(total / len(live_scores), 2)
            strikes = game.throw_list.count(10)
            info_text.value = f"총점: {total} | 평균: {avg} | 스트라이크: {strikes}"

        page.update()

    input_box = ft.TextField(
        label="0~10 입력",
        width=150,
        text_align="center",
        bgcolor="white",
    )

    def do_roll(e):
        error_text.value = ""

        if game.is_game_over():
            error_text.value = "게임 끝!"
            page.update()
            return

        try:
            p = int(input_box.value)

            if not (0 <= p <= 10):
                raise ValueError

            if not game.is_valid_roll(p):
                error_text.value = "핀 합 10 초과!"
                page.update()
                return

            game.throw_list.append(p)
            input_box.value = ""
            build_grid()

        except:
            error_text.value = "숫자 입력!"
            page.update()

    input_box.on_submit = do_roll

    def reset_game(e):
        game.throw_list.clear()
        error_text.value = ""
        info_text.value = ""
        build_grid()

    def undo_roll(e):
        if game.throw_list:
            game.throw_list.pop()
            build_grid()

    def auto_roll(e):
        if game.is_game_over():
            return

        max_pins = get_max_pins(game)
        p = random.randint(0, max_pins)

        game.throw_list.append(p)
        build_grid()

    page.add(
        ft.Column(
            [
                ft.Text("🎳 Bowling Game 🎳", size=40, weight="bold", color="white"),
                ft.Container(height=20),

                score_grid,

                ft.Container(height=20),

                info_text,
                error_text,

                ft.Row(
                    [
                        input_box,
                        ft.ElevatedButton(
                            content=ft.Text("🎯 투구", weight=ft.FontWeight.BOLD),
                            on_click=do_roll,
                        ),
                        ft.ElevatedButton(
                            content=ft.Text("↩ 취소", weight=ft.FontWeight.BOLD),
                            on_click=undo_roll,
                        ),
                        ft.ElevatedButton(
                            content=ft.Text("🎲 자동", weight=ft.FontWeight.BOLD),
                            on_click=auto_roll,
                        ),
                        ft.ElevatedButton(
                            content=ft.Text("🔄 리셋", weight=ft.FontWeight.BOLD),
                            on_click=reset_game,
                        ),
                    ],
                    alignment="center",
                ),
            ],
            horizontal_alignment="center",
            alignment="center",
        )
    )

    build_grid()


if __name__ == "__main__":
    ft.app(target=main)