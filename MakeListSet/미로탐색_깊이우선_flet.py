import flet as ft
import asyncio  # 💡 time 대신 asyncio 사용!

class VisualMazeSolver:
    def __init__(self, page: ft.Page, size=6):
        self.page = page
        self.size = size
        self.maze = [
            ['1','1','1','1','1','1'],
            ['e','0','0','0','0','1'],
            ['1','0','1','0','1','1'],
            ['1','1','1','0','0','x'],
            ['1','1','1','1','1','1'],
            ['1','1','1','1','1','1'],
        ]
        
        self.visited = [[False]*size for _ in range(size)]
        self.stack = []
        self.path = []    # 시작부터 출구까지 경로
        self.parent = {}  # 각 칸의 이전 칸
        
        self.is_solving = False
        
        self.cells = []  
        self.status_text = ft.Text("시작 대기 중...", size=20, weight=ft.FontWeight.BOLD)
        self.solve_btn = ft.ElevatedButton("Solve (미로 찾기)", on_click=self.solve, icon="play_arrow")
        self.reset_btn = ft.ElevatedButton("Reset (초기화)", on_click=self.reset, icon="refresh")

    def build_ui(self):
        grid_column = ft.Column(spacing=2)
        
        for r in range(self.size):
            row_controls = []
            row_cells = []
            for c in range(self.size):
                val = self.maze[r][c]
                bgcolor = ft.Colors.GREY_800 if val == '1' else ft.Colors.GREY_200
                text = ""
                
                if val == 'e':
                    bgcolor = ft.Colors.GREEN_500
                    text = "S"
                elif val == 'x':
                    bgcolor = ft.Colors.RED_500
                    text = "E"

                cell = ft.Container(
                    width=50, 
                    height=50,
                    bgcolor=bgcolor,
                    border_radius=5,
                    alignment=ft.Alignment.CENTER, 
                    content=ft.Text(text, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE if val in ('1','e','x') else ft.Colors.BLACK)
                )
                row_cells.append(cell)
                row_controls.append(cell)
                
            self.cells.append(row_cells)
            grid_column.controls.append(ft.Row(row_controls, spacing=2, alignment=ft.MainAxisAlignment.CENTER))

        return ft.Column(
            controls=[
                ft.Row([self.status_text], alignment=ft.MainAxisAlignment.CENTER),
                ft.Container(height=10),
                grid_column,
                ft.Container(height=20),
                ft.Row([self.solve_btn, self.reset_btn], alignment=ft.MainAxisAlignment.CENTER)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def reset(self, e=None):
        if self.is_solving:
            return  

        self.visited = [[False]*self.size for _ in range(self.size)]
        self.stack = []
        self.path = []
        self.parent = {}
        
        for r in range(self.size):
            for c in range(self.size):
                val = self.maze[r][c]
                if val == '1':
                    self.cells[r][c].bgcolor = ft.Colors.GREY_800
                elif val == '0':
                    self.cells[r][c].bgcolor = ft.Colors.GREY_200
                    self.cells[r][c].content.value = ""
                elif val == 'e':
                    self.cells[r][c].bgcolor = ft.Colors.GREEN_500
                elif val == 'x':
                    self.cells[r][c].bgcolor = ft.Colors.RED_500

        self.status_text.value = "미로가 초기화되었습니다."
        self.status_text.color = ft.Colors.WHITE
        self.page.update()

    def _find_start_exit(self):
        start = exit_pos = None
        for r in range(self.size):
            for c in range(self.size):
                if self.maze[r][c] == 'e':
                    start = (r, c)
                elif self.maze[r][c] == 'x':
                    exit_pos = (r, c)
        return start, exit_pos

    # 💡 여기서부터 비동기(async)로 변경!
    async def solve(self, e):
        if self.is_solving:
            return
            
        self.is_solving = True
        self.solve_btn.disabled = True
        self.reset_btn.disabled = True
        self.page.update()

        start, exit_pos = self._find_start_exit()

        if not start or not exit_pos:
            self.status_text.value = "시작(e) 또는 출구(x)가 없습니다"
            self.status_text.color = ft.Colors.RED_400
            self.page.update()
            self._finish_solve()
            return

        self.stack.append((start, None))

        while self.stack:
            pos, prev = self.stack.pop()
            r, c = pos

            if self.visited[r][c]:
                continue
                
            self.visited[r][c] = True
            self.parent[pos] = prev

            if self.maze[r][c] not in ('e', 'x'):
                self.cells[r][c].bgcolor = ft.Colors.YELLOW_400
            self.status_text.value = f"탐색 중... 현재 위치: ({r}, {c})"
            self.page.update()
            
            # 💡 UI 렌더링을 막지 않고 0.3초 대기
            await asyncio.sleep(0.3) 

            if pos == exit_pos:
                # 출구에서 이전 칸을 거슬러 올라가 경로 복원
                while pos is not None:
                    self.path.append(pos)
                    pos = self.parent[pos]
                self.path.reverse()

                # 최종 경로만 진한 파란색으로 표시
                for pr, pc in self.path:
                    if self.maze[pr][pc] not in ('e', 'x'):
                        self.cells[pr][pc].bgcolor = ft.Colors.BLUE_400
                        self.cells[pr][pc].content.value = "·"

                self.status_text.value = f"🎉 출구 도착! 경로 길이: {len(self.path)}칸"
                self.status_text.color = ft.Colors.GREEN_400
                self.page.update()
                self._finish_solve()
                return

            # 방문한 칸은 연한 파란색, 경로 여부는 출구 도착 후 결정
            if self.maze[r][c] not in ('e', 'x'):
                self.cells[r][c].bgcolor = ft.Colors.BLUE_200
                self.cells[r][c].content.value = "·" 
            self.page.update()

            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r+dr, c+dc
                if (0 <= nr < self.size and
                    0 <= nc < self.size and
                    not self.visited[nr][nc] and
                    self.maze[nr][nc] in ('0', 'x')):
                    self.stack.append(((nr, nc), pos))

        self.status_text.value = "❌ 출구가 없습니다."
        self.status_text.color = ft.Colors.RED_400
        self.page.update()
        self._finish_solve()

    def _finish_solve(self):
        self.is_solving = False
        self.solve_btn.disabled = False
        self.reset_btn.disabled = False
        self.page.update()

def main(page: ft.Page):
    page.title = "DFS Maze Solver"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK 

    maze_app = VisualMazeSolver(page)
    page.add(maze_app.build_ui())

if __name__ == "__main__":
    ft.run(main)