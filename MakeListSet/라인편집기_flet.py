import flet as ft
 
 
class FileIO:
    def __init__(self):
        self.filename = "text.txt"
        self.line_num = []
 
    def i(self, line_no, text):
        self.line_num = self.line_num[:line_no - 1] + [text] + self.line_num[line_no - 1:]
 
    def d(self, line_no):
        self.line_num = self.line_num[:line_no - 1] + self.line_num[line_no:]
 
    def r(self, line_no, text):
        self.line_num[line_no - 1] = text
 
    def l(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                for line in f:
                    self.line_num = self.line_num + [line]
        except FileNotFoundError:
            return "파일이 없습니다."
        return None
 
    def s(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            for line in self.line_num:
                f.write(line)
 
 
def main(page: ft.Page):
    page.title = "FileIO Editor"
    page.padding = 20
    page.bgcolor = "#1e1e2e"
    page.fonts = {"mono": "Courier New"}
 
    f = FileIO()
 
    line_field = ft.TextField(
        label="줄 번호",
        width=100,
        bgcolor="#2a2a3e",
        color="#cdd6f4",
        label_style=ft.TextStyle(color="#7f849c"),
        border_color="#45475a",
        focused_border_color="#89b4fa",
        text_align=ft.TextAlign.CENTER,
        keyboard_type=ft.KeyboardType.NUMBER,
    )
 
    text_field = ft.TextField(
        label="텍스트 입력",
        expand=True,
        bgcolor="#2a2a3e",
        color="#cdd6f4",
        label_style=ft.TextStyle(color="#7f849c"),
        border_color="#45475a",
        focused_border_color="#89b4fa",
    )
 
    # --- 출력 영역 ---
    output = ft.ListView(
        expand=True,
        spacing=4,
        padding=10,
    )
 
    status_text = ft.Text("", color="#a6e3a1", size=13)
 
    def refresh():
        output.controls.clear()
        if not f.line_num:
            output.controls.append(
                ft.Text("(내용 없음)", color="#585b70", italic=True, size=13)
            )
        else:
            for i, line in enumerate(f.line_num):
                output.controls.append(
                    ft.Text(
                        f"{i + 1}:  {line.rstrip()}",
                        color="#cdd6f4",
                        size=14,
                        font_family="mono",
                    )
                )
        page.update()
 
    def set_status(msg, color="#a6e3a1"):
        status_text.value = msg
        status_text.color = color
        page.update()
 
    def get_line_no():
        try:
            n = int(line_field.value)
            if n < 1:
                raise ValueError
            return n
        except (ValueError, TypeError):
            set_status("올바른 줄 번호를 입력하세요.", "#f38ba8")
            return None
 
    # --- 버튼 이벤트 ---
    def on_insert(e):
        n = get_line_no()
        if n is None:
            return
        text = text_field.value
        if not text:
            set_status("텍스트를 입력하세요.", "#f38ba8")
            return
        if n > len(f.line_num) + 1:
            set_status(f"줄 번호가 범위를 벗어났습니다. (최대 {len(f.line_num) + 1})", "#f38ba8")
            return
        f.i(n, text + "\n")
        text_field.value = ""
        refresh()
        set_status(f"{n}번째 줄에 삽입했습니다.")
 
    def on_replace(e):
        n = get_line_no()
        if n is None:
            return
        if n > len(f.line_num):
            set_status(f"줄 번호가 범위를 벗어났습니다. (최대 {len(f.line_num)})", "#f38ba8")
            return
        text = text_field.value
        if not text:
            set_status("텍스트를 입력하세요.", "#f38ba8")
            return
        f.r(n, text + "\n")
        text_field.value = ""
        refresh()
        set_status(f"{n}번째 줄을 수정했습니다.")
 
    def on_delete(e):
        n = get_line_no()
        if n is None:
            return
        if n > len(f.line_num):
            set_status(f"줄 번호가 범위를 벗어났습니다. (최대 {len(f.line_num)})", "#f38ba8")
            return
        f.d(n)
        refresh()
        set_status(f"{n}번째 줄을 삭제했습니다.", "#fab387")
 
    def on_save(e):
        if not f.line_num:
            set_status("저장할 내용이 없습니다.", "#f38ba8")
            return
        f.s()
        set_status(f"'{f.filename}'에 저장했습니다.")
 
    def on_load(e):
        err = f.l()
        if err:
            set_status(err, "#f38ba8")
        else:
            refresh()
            set_status(f"'{f.filename}'을 불러왔습니다.")
 
    # Flet 0.80부터 창 닫기는 page.window.destroy() 비동기 메서드
    async def on_quit(e):
        await page.window.destroy()
 
    # --- 버튼 스타일 헬퍼 ---
    def make_btn(label, color, handler):
        return ft.ElevatedButton(
            label,
            on_click=handler,
            bgcolor=color,
            color="#1e1e2e",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
            ),
        )
 
    btn_row = ft.Row(
        controls=[
            make_btn("삽입", "#89b4fa", on_insert),
            make_btn("수정", "#a6e3a1", on_replace),
            make_btn("삭제", "#f38ba8", on_delete),
            make_btn("저장", "#f9e2af", on_save),
            make_btn("불러오기", "#cba6f7", on_load),
            make_btn("종료", "#585b70", on_quit),
        ],
        wrap=True,
        spacing=8,
    )
 
    # --- 레이아웃 조립 ---
    page.add(
        ft.Text("FileIO Editor", size=22, weight=ft.FontWeight.BOLD, color="#cdd6f4"),
        ft.Divider(color="#313244"),
        ft.Row([line_field, text_field], spacing=10),
        btn_row,
        status_text,
        ft.Divider(color="#313244"),
        ft.Text("파일 내용", size=13, color="#7f849c"),
        ft.Container(
            content=output,
            bgcolor="#181825",
            border_radius=10,
            expand=True,
            padding=5,
        ),
    )
 
    refresh()
 
 
ft.app(target=main)
 
