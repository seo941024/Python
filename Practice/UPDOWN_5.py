import flet as ft
import random

def ran_num_imp():
    return random.randint(1, 100)

# 메인 애플리케이션 함수
def main(page: ft.Page):
    
    # 페이지 설정
    page.title = "Up Down Game"
    ran_num = ran_num_imp()
    
    # 남은 기회
    a = 5

    result_text = ft.Text("1 ~ 100 사이 숫자를 입력해주세요.")

    # 남은 기회 표시
    chance_text = ft.Text(f"남은 기회 : {a}")

    # 숫자 입력창
    input_box = ft.TextField(label="숫자 입력", width=200)

    # 게임을 다시 시작하는 함수

    def restart_game(e):
        nonlocal ran_num, a

        ran_num = ran_num_imp()   # 새로운 랜덤 숫자 생성
        a = 5                # 기회 초기화

        result_text.value = "새 게임 시작!"
        chance_text.value = f"남은 기회 : {a} 번 입니다. "
        input_box.value = ""

        page.update()

    
    # 숫자 확인 함수
    
    def check_number(e):
        nonlocal ran_num, a

        try:
            n = int(input_box.value)  # 입력 숫자
        except:
            result_text.value = "숫자를 입력해주세요."
            page.update()
            return

        # 정답 맞춘 경우
        if n == ran_num:
            result_text.value = "정답입니다."
            chance_text.value = "다시 시작 버튼을 눌러주세요."

        else:
            a -= 1

            if n > ran_num:
                result_text.value = "더 낮은 숫자입니다."

            else:
                result_text.value = "더 높은 숫자입니다."

            chance_text.value = f"남은 기회 : {a}"

            # 기회를 모두 소진한 경우
            if a < 1:
                result_text.value = f"실패하였습니다. 정답은 {ran_num} 입니다."
                chance_text.value = "다시 시작 버튼을 눌러주세요."

        input_box.value = ""  # 입력창 초기화
        page.update()

    # 숫자 확인 버튼
    check_button = ft.ElevatedButton(
        "확인",
        on_click=check_number
    )

    # 게임 다시 시작 버튼
    restart_button = ft.ElevatedButton(
        "다시 시작",
        on_click=restart_game
    )

    # 화면에 요소 배치
    page.add(
        ft.Column(
            [
                ft.Text("Up Down Game", size=30),
                result_text,
                chance_text,
                input_box,
                check_button,
                restart_button
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )



# Flet 앱 실행
ft.app(target=main)