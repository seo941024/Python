import random
import flet as ft

choices = ["바위", "가위", "보"]

def main(page: ft.Page):
    page.title = "가위 바위 보🌸"
    page.window_width = 400
    page.window_height = 500
    page.bgcolor = "#ffe6f0"

    u_score = 0
    c_score = 0

    set_u = 0
    set_c = 0

    # UI
    result_text = ft.Text("버튼을 눌러 시작하세요!", size=20)
    info_text = ft.Text("", size=16)
    score_text = ft.Text("현재 스코어 0 : 0", size=16)
    set_text = ft.Text("세트 스코어 0 : 0", size=16)

    # 게임 진행
    def play(user_choice):
        nonlocal u_score, c_score, set_u, set_c

        computer = random.randint(0, 2)

        info_text.value = f"컴퓨터: {choices[computer]}, 유저: {choices[user_choice]}"

        if user_choice == computer:
            result = "무승부"

        elif (user_choice == 0 and computer == 1) or \
             (user_choice == 1 and computer == 2) or \
             (user_choice == 2 and computer == 0):
            result = "유저 승리"
            u_score += 1

        else:
            result = "컴퓨터 승리"
            c_score += 1

        result_text.value = result

        if u_score == 3:
            set_u += 1
            result_text.value = f"유저가 승리하였습니다. (현재 {set_u}:{set_c})"
            u_score = 0
            c_score = 0

        elif c_score == 3:
            set_c += 1
            result_text.value = f"컴퓨터가 승리하였습니다. (현재 {set_u}:{set_c})"
            u_score = 0
            c_score = 0

        score_text.value = f"현재 스코어 {u_score} : {c_score}"
        set_text.value = f"세트 스코어 {set_u} : {set_c}"

        if set_u == 3:
            result_text.value = "유저가 승리하였습니다."
            disable_buttons()

        elif set_c == 3:
            result_text.value = "컴퓨터가 승리하였습니다."
            disable_buttons()

        page.update()

    # 버튼 제어
    def disable_buttons():
        for b in buttons.controls:
            b.disabled = True

    def enable_buttons():
        for b in buttons.controls:
            b.disabled = False

    # 리셋
    def reset_game(e):
        nonlocal u_score, c_score, set_u, set_c

        u_score = 0
        c_score = 0
        set_u = 0
        set_c = 0

        result_text.value = "다시 시작!"
        info_text.value = ""
        score_text.value = "현재 스코어 0 : 0"
        set_text.value = "세트 스코어 0 : 0"

        enable_buttons()
        page.update()

    # 버튼
    buttons = ft.Row(
    controls=[
        ft.ElevatedButton("바위", bgcolor="#ffb6c1", color="white", on_click=lambda e: play(0)), #전부 화이트+벚꽃
        ft.ElevatedButton("가위", bgcolor="#ffb6c1", color="white", on_click=lambda e: play(1)),
        ft.ElevatedButton("보", bgcolor="#ffb6c1", color="white", on_click=lambda e: play(2)),
    ],
    alignment=ft.MainAxisAlignment.CENTER
)

    reset_btn = ft.ElevatedButton("다시 시작", bgcolor="#ffb6c1", color="white", on_click=reset_game)

    # 화면 구성
    page.add(
        ft.Column(
            [
                ft.Text("가위 바위 보 게임🌸", size=24, weight="bold"),
                result_text,
                info_text,
                score_text,
                set_text,
                buttons,
                reset_btn
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)