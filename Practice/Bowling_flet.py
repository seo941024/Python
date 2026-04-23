from bowling_func import BowlingGame
import flet as ft

def main(page: ft.Page):
    page.title = "Professional Bowling System"
    page.bgcolor = "#0A192F"  # 어두운 볼링장 배경색
    page.padding = 30
    
    game = BowlingGame()
    
    # 이 컨테이너가 '통합 점수판' 역할을 합니다.
    scoreboard_row = ft.Row(spacing=0, alignment=ft.MainAxisAlignment.CENTER)

    def render_board():
        # 데이터 갱신
        frames_data = game.get_display_data()
        scores = game.calculate_live_scores()
        
        scoreboard_row.controls.clear()

        for i in range(10):
            is_10th = (i == 9)
            frame_width = 150 if is_10th else 100
            
            # 1. 프레임 내 투구 표시 (상단 작은 칸들)
            shots = frames_data[i] if i < len(frames_data) else []
            num_slots = 3 if is_10th else 2
            
            shot_boxes = []
            for s_idx in range(num_slots):
                val = shots[s_idx] if s_idx < len(shots) else ""
                shot_boxes.append(
                    ft.Container(
                        content=ft.Text(val, size=18, weight="bold", color="white"),
                        width=frame_width / num_slots,
                        height=45,
                     
                        border=ft.border.all(1, "#334756")
                    )
                )

            # 2. 프레임 전체 구성 (번호 + 투구 + 점수를 하나의 수직 칼럼으로)
            frame_column = ft.Container(
                width=frame_width,
                border=ft.border.all(2, "#334756"),
                bgcolor="#16213E",
                content=ft.Column(
                    [
                        # 프레임 번호 (제일 위)
                        ft.Container(
                            content=ft.Text(str(i+1), size=12, color="#999999"),
                            alignment=ft.alignment.center,
                            height=25,
                            bgcolor="#0F3460"
                        ),
                        # 투구 점수 (중간)
                        ft.Row(shot_boxes, spacing=0),
                        # 누적 점수 (제일 아래)
                        ft.Container(
                            content=ft.Text(
                                str(scores[i]) if i < len(scores) else "",
                                size=28, weight="heavy", color="#E94560"
                            ),
                            height=65,
                            alignment=ft.alignment.center,
                        )
                    ],
                    spacing=0
                )
            )
            scoreboard_row.controls.append(frame_column)
        
        page.update()

    # --- 입력창 ---
    input_field = ft.TextField(
        label="PIN", width=100, text_align="center", 
        color="white", border_color="#E94560",
        on_submit=lambda _: do_roll()
    )

    def do_roll():
        if input_field.value:
            game.throw_list.append(int(input_field.value))
            input_field.value = ""
            render_board()

    # 초기 화면 구성
    render_board()

    page.add(
        ft.Column([
            ft.Text("🎳 LANE 02 - PLAYER 1", size=32, weight="bold", color="white"),
            ft.Divider(height=20, color="transparent"),
            # 여기가 핵심: 한 줄로 연결된 점수판
            ft.Container(
                content=scoreboard_row,
                border_radius=10,
                padding=10
            ),
            ft.Divider(height=40, color="transparent"),
            ft.Row([
                input_field, 
                ft.ElevatedButton("GO!", on_click=lambda _: do_roll(), bgcolor="#E94560", color="white")
            ], alignment="center")
        ], horizontal_alignment="center")
    )

if __name__ == "__main__":
    ft.app(target=main)