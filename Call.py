import flet as ft
import csv
import os

FILE_NAME = "people.csv"

keys = ["이름", "이메일", "전화번호", "직장명"]

#  데이터 불러오기
def load_data():
    data = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    return data


#  데이터 저장
def save_data(people):
    with open(FILE_NAME, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(people)


def main(page: ft.Page):
    page.title = "전화번호부"
    page.window_width = 800
    page.window_height = 500

    people = load_data()

    inputs = {
        k: ft.TextField(label=k, width=180, filled=True, bgcolor="white")
        for k in keys
    }

    search_field = ft.TextField(label="검색", width=180, filled=True, bgcolor="white")

    list_column = ft.Column(scroll="auto", expand=True)

    selected_index = {"value": None}

    #  카드 UI
    def create_card(p, index):
        return ft.Container(
            content=ft.Column([
                ft.Text(f"👤 {p['이름']}", weight="bold"),
                ft.Text(f"📧 {p['이메일']}"),
                ft.Text(f"📞 {p['전화번호']}"),
                ft.Text(f"🏢 {p['직장명']}"),
                ft.Row([
                    ft.TextButton("수정", on_click=lambda e, i=index: load_edit(i)),
                    ft.TextButton("삭제", on_click=lambda e, i=index: delete_person(i))
                ])
            ]),
            padding=10,
            border_radius=10,
            bgcolor="white",
            shadow=ft.BoxShadow(blur_radius=5, color="#cccccc")
        )

    #  리스트 갱신
    def refresh_list(data=None):
        list_column.controls.clear()
        target = data if data is not None else people

        for i, p in enumerate(target):
            list_column.controls.append(create_card(p, i))

        page.update()

    #  추가
    def add_person(e):
        person = {k: inputs[k].value.strip() for k in keys}
        people.append(person)
        save_data(people)

        for f in inputs.values():
            f.value = ""

        refresh_list()

    #  삭제
    def delete_person(index):
        if 0 <= index < len(people):
            people.pop(index)
            save_data(people)

        refresh_list()

    #  수정 불러오기
    def load_edit(index):
        selected_index["value"] = index
        p = people[index]

        for k in keys:
            inputs[k].value = p[k]

        page.update()

    #  수정 저장
    def update_person(e):
        idx = selected_index["value"]

        if idx is None:
            return

        people[idx] = {k: inputs[k].value.strip() for k in keys}
        selected_index["value"] = None

        save_data(people)
        refresh_list()

    #  검색
    def search(e):
        keyword = search_field.value.strip().lower()
        result = []

        for p in people:
            full_text = " ".join(p.values()).lower()
            if keyword in full_text:
                result.append(p)

        refresh_list(result)

    #  버튼
    btn_add = ft.ElevatedButton("추가", on_click=add_person)
    btn_update = ft.ElevatedButton("수정 저장", on_click=update_person)
    btn_search = ft.ElevatedButton("검색", on_click=search)

    #  왼쪽 패널
    left_panel = ft.Column([
        ft.Text("신규 등록 및 수정", size=18, weight="bold"),
        *inputs.values(),
        ft.Row([btn_add, btn_update]),
        ft.Divider(),
        search_field,
        btn_search
    ], width=220)

    #  오른쪽 패널
    right_panel = ft.Container(
        content=ft.Column([
            ft.Text("전화번호부", size=18, weight="bold"),
            list_column
        ]),
        expand=True,
        padding=10
    )

    page.add(
        ft.Row([
            left_panel,
            ft.VerticalDivider(),
            right_panel
        ], expand=True)
    )

    #  시작 시 데이터 표시
    refresh_list()


ft.app(target=main)