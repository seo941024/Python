import flet as ft


class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_all_results(self):
        if not self.numbers:
            return "No numbers provided"

        results = {}

        results["add"] = sum(self.numbers)

        sub = self.numbers[0]
        for n in self.numbers[1:]:
            sub -= n
        results["subtract"] = sub

        mul = 1
        for n in self.numbers:
            mul *= n
        results["multiply"] = mul

        div = self.numbers[0]
        for n in self.numbers[1:]:
            if n == 0:
                div = "Cannot divide by zero"
                break
            div /= n
        results["divide"] = div

        results["average"] = sum(self.numbers) / len(self.numbers)
        results["max"] = max(self.numbers)
        results["min"] = min(self.numbers)

        return results


def main(page: ft.Page):
    page.title = "Calculator"
    page.window_width = 400
    page.window_height = 600
    page.padding = 20
    page.bgcolor = "#f5f6fa"

    title = ft.Text(
        "Calculator",
        size=28,
        weight="bold",
        color="#2f3640"
    )

    input_field = ft.TextField(
        label="숫자 입력 (쉼표로 구분)",
        border_radius=10,
        filled=True,
        bgcolor="white"
    )

    result_text = ft.Text(size=16, color="#2f3640")

    result_box = ft.Container(
        content=result_text,
        padding=15,
        border_radius=10,
        bgcolor="white",
        shadow=ft.BoxShadow(
            blur_radius=10,
            color="#dcdde1"
        )
    )

    def run_calc(e):
        try:
            nums = list(map(int, input_field.value.split(",")))
            calc = Calculator(nums)
            r = calc.get_all_results()

            if isinstance(r, dict):
                result_text.value = (
                    f"덧셈: {r['add']}\n"
                    f"뺄셈: {r['subtract']}\n"
                    f"곱셈: {r['multiply']}\n"
                    f"나눗셈: {r['divide']}\n\n"
                    f"평균값: {r['average']:.2f}\n"
                    f"최대값: {r['max']}\n"
                    f"최소값: {r['min']}"
                )
            else:
                result_text.value = r

        except:
            result_text.value = "정수를 쉼표로 구분해서 입력하세요"

        page.update()

    calc_button = ft.ElevatedButton(
        "결과 보기",
        on_click=run_calc,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=15,
        ),
        width=200
    )

    page.add(
        ft.Column(
            [
                title,
                input_field,
                calc_button,
                result_box
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=20
        )
    )


ft.app(target=main)