# BFS(너비 우선 탐색) 미로 탐색 - Flet GUI 버전
# BFS는 큐를 사용해서 시작점과 가까운 칸부터 차례로 탐색합니다.
# 노란색 = 탐색 중인 칸 / 파란색 = 최단 경로 칸

import flet as ft
import asyncio


class BFSVisualMazeSolver:

    def __init__(self, page: ft.Page):
        self.page = page
        self.size = 6

        # 미로 맵 ('1'=벽, '0'=길, 'e'=시작, 'x'=출구)
        self.maze = [
            ['1', '1', '1', '1', '1', '1'],
            ['e', '0', '0', '0', '0', '1'],
            ['1', '0', '1', '0', '1', '1'],
            ['1', '1', '1', '0', '0', 'x'],
            ['1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1'],
        ]

        # 방문 여부 배열
        self.visited = [[False] * self.size for _ in range(self.size)]

        # 경로 역추적용 부모 딕셔너리
        self.parent = {}

        # 현재 탐색 중인지 나타내는 플래그
        self.is_solving = False

        # 화면에 표시될 셀(칸) 2차원 배열
        self.cells = []

        # 화면 상단에 표시될 상태 메시지
        self.status_text = ft.Text("시작 버튼을 눌러 BFS 탐색을 시작하세요.", size=18, weight=ft.FontWeight.BOLD)

        # 버튼 정의
        self.solve_btn = ft.ElevatedButton("탐색 시작 (BFS)", on_click=self.solve, icon="play_arrow")
        self.reset_btn = ft.ElevatedButton("초기화", on_click=self.reset, icon="refresh")

    def build_ui(self):
        # 미로 격자 UI를 만드는 함수
        grid_column = ft.Column(spacing=2)

        for r in range(self.size):
            row_controls = []
            row_cells = []

            for c in range(self.size):
                value = self.maze[r][c]

                # 셀 배경색 설정 (벽=어두운 회색, 길=밝은 회색)
                if value == '1':
                    bg_color = ft.Colors.GREY_800
                else:
                    bg_color = ft.Colors.GREY_200

                # 시작점과 출구는 특별한 색으로 표시
                label = ""
                if value == 'e':
                    bg_color = ft.Colors.GREEN_500
                    label = "S"
                elif value == 'x':
                    bg_color = ft.Colors.RED_500
                    label = "E"

                # 하나의 칸(Container)을 만듭니다
                cell = ft.Container(
                    width=50,
                    height=50,
                    bgcolor=bg_color,
                    border_radius=5,
                    alignment=ft.Alignment.CENTER,
                    content=ft.Text(
                        label,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE
                    )
                )

                row_cells.append(cell)
                row_controls.append(cell)

            self.cells.append(row_cells)
            grid_column.controls.append(
                ft.Row(row_controls, spacing=2, alignment=ft.MainAxisAlignment.CENTER)
            )

        # 전체 레이아웃 구성
        return ft.Column(
            controls=[
                ft.Row([self.status_text], alignment=ft.MainAxisAlignment.CENTER),
                ft.Container(height=10),
                grid_column,
                ft.Container(height=20),
                ft.Row([self.solve_btn, self.reset_btn], alignment=ft.MainAxisAlignment.CENTER),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def reset(self, e=None):
        # 탐색 중에는 초기화 불가
        if self.is_solving:
            return

        # 방문 배열과 부모 딕셔너리 초기화
        self.visited = [[False] * self.size for _ in range(self.size)]
        self.parent = {}

        # 모든 셀을 원래 색으로 되돌리기
        for r in range(self.size):
            for c in range(self.size):
                value = self.maze[r][c]

                if value == '1':
                    self.cells[r][c].bgcolor = ft.Colors.GREY_800
                elif value == '0':
                    self.cells[r][c].bgcolor = ft.Colors.GREY_200
                    self.cells[r][c].content.value = ""
                elif value == 'e':
                    self.cells[r][c].bgcolor = ft.Colors.GREEN_500
                elif value == 'x':
                    self.cells[r][c].bgcolor = ft.Colors.RED_500

        self.status_text.value = "초기화 완료. 다시 탐색을 시작하세요."
        self.status_text.color = ft.Colors.WHITE
        self.page.update()

    def find_start_and_exit(self):
        # 미로에서 시작점과 출구 위치를 찾아 반환
        start = None
        exit_pos = None

        for r in range(self.size):
            for c in range(self.size):
                if self.maze[r][c] == 'e':
                    start = (r, c)
                elif self.maze[r][c] == 'x':
                    exit_pos = (r, c)

        return start, exit_pos

    def get_path(self, start, exit_pos):
        # 부모 딕셔너리를 따라 출구에서 시작점까지 역추적
        path = []
        current = exit_pos

        while current != start:
            path.append(current)
            current = self.parent[current]

        path.append(start)
        path.reverse()  # 시작 → 출구 순서로 뒤집기

        return path

    async def solve(self, e):
        # 이미 탐색 중이면 중복 실행 방지
        if self.is_solving:
            return

        self.is_solving = True
        self.solve_btn.disabled = True
        self.reset_btn.disabled = True
        self.page.update()

        start, exit_pos = self.find_start_and_exit()

        if start is None or exit_pos is None:
            self.status_text.value = "시작점(e) 또는 출구(x)가 없습니다."
            self.status_text.color = ft.Colors.RED_400
            self.page.update()
            self.finish_solve()
            return

        # BFS 큐 초기화 - 시작점을 먼저 넣음
        queue = []
        queue.append(start)
        self.visited[start[0]][start[1]] = True

        while len(queue) > 0:

            # 큐 맨 앞에서 꺼내기 (FIFO)
            current = queue.pop(0)
            r = current[0]
            c = current[1]

            # 탐색 중인 칸을 노란색으로 표시
            if self.maze[r][c] not in ('e', 'x'):
                self.cells[r][c].bgcolor = ft.Colors.YELLOW_400

            self.status_text.value = f"BFS 탐색 중... 현재 위치: ({r}, {c})"
            self.page.update()

            # 화면 업데이트를 보여주기 위해 잠시 대기
            await asyncio.sleep(0.35)

            # 출구에 도달한 경우
            if (r, c) == exit_pos:
                # 최단 경로를 파란색으로 표시
                path = self.get_path(start, exit_pos)
                for pr, pc in path:
                    if self.maze[pr][pc] not in ('e', 'x'):
                        self.cells[pr][pc].bgcolor = ft.Colors.BLUE_400
                        self.cells[pr][pc].content.value = "·"

                self.status_text.value = f"출구 도착! 최단 경로 길이: {len(path)}칸"
                self.status_text.color = ft.Colors.GREEN_400
                self.page.update()
                self.finish_solve()
                return

            # 이미 탐색한 칸은 파란 점으로 표시
            if self.maze[r][c] not in ('e', 'x'):
                self.cells[r][c].bgcolor = ft.Colors.BLUE_200
                self.cells[r][c].content.value = "·"
            self.page.update()

            # 상하좌우 네 방향 탐색
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < self.size and 0 <= nc < self.size:
                    if not self.visited[nr][nc] and self.maze[nr][nc] in ('0', 'x'):
                        self.visited[nr][nc] = True
                        self.parent[(nr, nc)] = (r, c)  # 부모 기록
                        queue.append((nr, nc))

        self.status_text.value = "출구를 찾지 못했습니다."
        self.status_text.color = ft.Colors.RED_400
        self.page.update()
        self.finish_solve()

    def finish_solve(self):
        # 탐색 완료 후 버튼 다시 활성화
        self.is_solving = False
        self.solve_btn.disabled = False
        self.reset_btn.disabled = False
        self.page.update()


def main(page: ft.Page):
    page.title = "BFS 미로 탐색 (너비 우선 탐색)"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    app = BFSVisualMazeSolver(page)
    page.add(app.build_ui())


if __name__ == "__main__":
    ft.run(main)
