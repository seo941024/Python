import flet as ft
 
class calculate:
    def check_brackets(self, expr):
        stack = []
        match = {')': '(', ']': '[', '}': '{'}
 
        for ch in expr:
            if ch in '([{':
                stack.append(ch)
            elif ch in ')]}':
                if not stack or stack[-1] != match[ch]:
                    return "ERROR"
                stack.pop()
 
        return "OK" if not stack else "ERROR"
 
    def tokenize(self, expr):
        """공백 없이 붙여 쓴 식도 숫자·연산자·괄호 단위로 나눔"""
        tokens = []
        num = ''
        for ch in expr:
            if ch.isdigit() or ch == '.':
                num += ch
                continue
            # 식 맨 앞이나 연산자·여는 괄호 뒤의 -는 음수 부호
            prev = tokens[-1] if tokens else '('
            if ch == '-' and not num and prev in ('+', '-', '*', '/', '('):
                num = '-'
                continue
            if num:
                tokens.append(num)
                num = ''
            if not ch.isspace():
                tokens.append(ch)
        if num:
            tokens.append(num)
        return tokens
 
    def infix_to_postfix(self, expr):
        prec = {'+': 1, '-': 1, '*': 2, '/': 2}
        stack, result = [], []
 
        for token in self.tokenize(expr):
            if token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()
            elif token in prec:
                while stack and stack[-1] != '(' and prec.get(stack[-1], 0) >= prec[token]:
                    result.append(stack.pop())
                stack.append(token)
            else:
                result.append(token)
 
        while stack:
            result.append(stack.pop())
 
        return ' '.join(result)
 
    def evaluate_postfix(self, expr):
        stack = []
        tokens = expr.split()
 
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                # 연산자 앞에 숫자가 두 개 없으면 잘못된 식
                if len(stack) < 2:
                    raise ValueError("잘못된 수식입니다")
                b = stack.pop()
                a = stack.pop()
                if   token == '+': stack.append(a + b)
                elif token == '-': stack.append(a - b)
                elif token == '*': stack.append(a * b)
                elif token == '/': stack.append(float(a / b))
            else:
                stack.append(float(token))
 
        # 계산 후 숫자가 하나만 남아야 정상
        if len(stack) != 1:
            raise ValueError("잘못된 수식입니다")
        return stack[0]
 
    def evaluate_infix(self, expr):
        postfix = self.infix_to_postfix(expr)
        return self.evaluate_postfix(postfix)
    
 
 
def main(page: ft.Page):
    page.title = "수식 계산기(괄호를 포함한 수식)"
    page.padding = 20
    page.bgcolor = '#ffffff'
    page.fonts = {"mono": "Courier New"}
 
    c = calculate()
 
    text_field = ft.TextField(
        label="계산식 입력 공간",
        expand=True,
        bgcolor="#ffffff",
        color="#000000",
        border_radius=10,
        border_color="#af0000",
    )
    result_text = ft.Text("", size=20, color="#000000")
 
    def on_calculate(e):
        expr = text_field.value.strip()
        if not expr:
            return
 
        if c.check_brackets(expr) == "ERROR":
            result_text.value = "❌ 괄호 오류"
            result_text.color = "#af0000"
        else:
            try:
                result = c.evaluate_infix(expr)
                result_text.value = f"= {int(result) if result == int(result) else result}"
                result_text.color = "#000000"
            except Exception:
                result_text.value = "❌ 수식 오류"
                result_text.color = "#af0000"
 
        page.update()
 
    def on_clear(e):
        text_field.value = ""
        result_text.value = ""
        page.update()
 
    def on_backspace(e):
        # 마지막 한 글자 제거
        text_field.value = (text_field.value or "").rstrip()[:-1]
        page.update()
 
    def btn_click(val):
        def handler(e):
            # 공백 없이 이어 붙여 1, 2를 연속으로 누르면 12
            text_field.value = (text_field.value or "") + val
            page.update()
        return handler
 
    def make_btn(label, val=None, color="#f0f0f0", text_color="#000000", on_click=None):
        return ft.ElevatedButton(
            label,
            on_click=on_click if on_click else btn_click(val or label),
            bgcolor=color,
            color=text_color,
            width=70,
            height=55,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
        )
 
    calc_btn = ft.ElevatedButton(
        "계산",
        on_click=on_calculate,
        bgcolor="#af0000",
        color="#ffffff",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
    )
 
    # 버튼 패드
    button_pad = ft.Column(
        controls=[
            ft.Row([
                make_btn("7"), make_btn("8"), make_btn("9"),
                make_btn("/", color="#ffe0e0", text_color="#af0000"),
            ]),
            ft.Row([
                make_btn("4"), make_btn("5"), make_btn("6"),
                make_btn("*", color="#ffe0e0", text_color="#af0000"),
            ]),
            ft.Row([
                make_btn("1"), make_btn("2"), make_btn("3"),
                make_btn("-", color="#ffe0e0", text_color="#af0000"),
            ]),
            ft.Row([
                make_btn("0"),
                make_btn("(", color="#e8f0fe", text_color="#1a73e8"),
                make_btn(")", color="#e8f0fe", text_color="#1a73e8"),
                make_btn("+", color="#ffe0e0", text_color="#af0000"),
            ]),
            ft.Row([
                make_btn("⌫", color="#fff3e0", text_color="#e65100", on_click=on_backspace),
                make_btn("C", color="#fce4ec", text_color="#af0000", on_click=on_clear),
                calc_btn,
            ]),
        ],
        spacing=8,
    )
 
    page.add(
        ft.Row([text_field, calc_btn]),
        result_text,
        ft.Text("※ 버튼으로 입력하거나 직접 타이핑 (띄어쓰기 없이도 가능: 3+(5*2))",
                size=12, color="#888888"),
        ft.Divider(),
        button_pad,
    )
 
ft.app(target=main)