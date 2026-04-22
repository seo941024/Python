import flet as ft
import random
import json
import os


def main(page: ft.Page):
    page.title = "Simple Market"
    page.bgcolor = "white"

    items = [
        "비누", "치약", "샴푸", "린스", "바디워시", "폼클렌징", "칫솔", "수건",
        "휴지", "물티슈", "세탁세제", "섬유유연제", "주방세제", "수세미", "고무장갑",
        "쌀", "라면", "햇반", "생수", "우유", "계란", "두부", "콩나물", "시금치",
        "양파", "감자", "고구마", "사과", "바나나", "오렌지", "귤", "토마토",
        "김치", "된장", "고추장", "간장", "식용유", "참기름", "소금", "설탕",
        "커피", "차", "과자", "빵", "젤리", "초콜릿", "음료수", "맥주", "소주",
        "고기(돼지고기)", "고기(소고기)", "닭고기", "생선", "오징어", "새우", "게",
        "쌀국수", "파스타", "잼", "버터", "치즈", "요거트", "아이스크림", "통조림",
        "냉동만두", "어묵", "햄", "소시지", "김", "미역", "다시마", "멸치",
        "밀가루", "부침가루", "튀김가루", "빵가루", "식초", "소스", "향신료",
        "양초", "성냥", "건전지", "전구", "쓰레기봉투", "지퍼백", "호일", "랩"
    ]

    # 데이터 로드 or 생성

    if os.path.exists("market.json"):
        with open("market.json", "r", encoding="utf-8") as f:
            market = json.load(f)
    else:
        market = {}
        x = 0

        while x < len(items):
            mid = str(random.randint(1, 100000)) 

            if mid in market:
                continue

            price = random.randint(10, 100) * 100

            market[mid] = {
                "name": items[x],
                "stock": random.randint(1, 50),
                "price": price,
                "original_price": price
            }
            x += 1

    # 저장 함수
    def save_data():
        with open("market.json", "w", encoding="utf-8") as f:
            json.dump(market, f, ensure_ascii=False, indent=4)

    cart = []
    total_cash = 0
    today_total = 0
    admin_mode = False

    # -------------------------
    # UI
    # -------------------------
    name_input = ft.TextField(label="상품 이름")
    qty_input = ft.TextField(label="수량")

    admin_name_input = ft.TextField(label="상품 이름")

    price_input = ft.TextField(label="가격 수정")
    stock_input = ft.TextField(label="재고 추가")

    output = ft.Text(color="black")
    total_text = ft.Text("총 금액: 0원", size=16, weight="bold", color="black")
    today_text = ft.Text("오늘 총 매출: 0원", size=14, weight="bold", color="black")
    admin_text = ft.Text("관리자 모드 OFF", color="black")

    cart_view = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)
    danger_view = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)
    discount_view = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)


    def find(name):
        name = name.strip()
        for k, v in market.items():
            if v["name"].strip() == name:
                return k, v
        return None, None

    def load_danger():
        danger_view.controls.clear()
        for v in sorted(market.values(), key=lambda x: x["stock"]):
            if v["stock"] <= 5:
                danger_view.controls.append(
                    ft.Container(
                        content=ft.Text(f"{v['name']} | 재고:{v['stock']}"),
                        padding=8,
                        border_radius=8,
                        bgcolor="#fff4f4",
                        border=ft.border.all(2, "#ad2727")
                    )
                )
        page.update()

    def load_discount():
        discount_view.controls.clear()
        for v in market.values():
            v["price"] = v["original_price"]

        for k in random.sample(list(market.keys()), 5):
            v = market[k]
            old = v["original_price"]
            new_price = int(old * 0.9)
            v["price"] = new_price

            discount_view.controls.append(
                ft.Container(
                    content=ft.Text(f"{v['name']}  {old} → {new_price}"),
                    padding=8,
                    border_radius=8,
                    bgcolor="#FFFCF2",
                    border=ft.border.all(2, "#ffe082")
                )
            )
        page.update()

    def add_cart(e):
        nonlocal total_cash
        name = name_input.value.strip()
        qty = qty_input.value

        if not name or not qty or not qty.isdigit():
            output.value = "입력 오류"
            page.update()
            return

        qty = int(qty)
        k, v = find(name)

        if not v:
            output.value = "상품 없음"
            page.update()
            return

        if v["stock"] < qty:
            output.value = "재고 부족"
            page.update()
            return

        price = v["price"] * qty
        v["stock"] -= qty

        cart.append((k, v["name"], qty, price))

        total_cash += price
        total_text.value = f"총 금액: {total_cash:,}원"

        output.value = "추가 완료"

        name_input.value = ""
        qty_input.value = ""

        load_danger()
        save_data() 
        page.update()

    def buy(e):
        nonlocal total_cash, today_total

        receipt = "=== 영수증 ===\n"

        for k, name, qty, price in cart:
            receipt += f"{name} x{qty} = {price}원\n"

        today_total += total_cash

        receipt += f"\n이번 구매: {total_cash}원"
        receipt += f"\n오늘 총 매출: {today_total}원"

        with open("receipt.txt", "a", encoding="utf-8") as f:
            f.write(receipt + "\n\n")

        cart.clear()
        total_cash = 0

        total_text.value = "총 금액: 0원"
        today_text.value = f"오늘 총 매출: {today_total:,}원"

        output.value = "구매 완료"

        save_data()
        page.update()

    def toggle_admin(e):
        nonlocal admin_mode
        admin_mode = not admin_mode
        admin_text.value = "관리자 모드 ON" if admin_mode else "관리자 모드 OFF"
        page.update()

    def update_item(e):
        if not admin_mode:
            output.value = "관리자만 가능"
            page.update()
            return

        name = admin_name_input.value.strip()

        if name == "":
            output.value = "상품 이름 먼저 입력"
            page.update()
            return

        k, v = find(name)

        if v is None:
            output.value = "상품 없음"
            page.update()
            return

        if price_input.value.isdigit():
            v["price"] = int(price_input.value)
            v["original_price"] = v["price"]

        if stock_input.value.isdigit():
            v["stock"] += int(stock_input.value)

        output.value = "수정 완료"

        admin_name_input.value = ""
        price_input.value = ""
        stock_input.value = ""

        load_danger()
        save_data() 
        page.update()

    # -------------------------
    # UI
    # -------------------------
    page.add(
        ft.Row(
            expand=True,
            controls=[

                ft.Container(
                    width=250,
                    padding=10,
                    border_radius=10,
                    bgcolor="#ffffff",
                    border=ft.border.all(2, "#ad2727"),
                    content=ft.Column(
                        expand=True,
                        controls=[
                            ft.Text("🚨 재고 부족 🚨", size=20,
                            weight=ft.FontWeight.BOLD,
                            color="black"),
                            ft.Container(content=danger_view, expand=True)
                        ]
                    )
                ),

                ft.Container(
                    expand=True,
                    padding=20,
                    bgcolor="#ffffff",
                    border_radius=14,
                    border=ft.border.all(2, "#3e91d4"),
                    content=ft.Column(
                        expand=True,
                        scroll=ft.ScrollMode.AUTO,
                        controls=[
                            ft.Text("Market",  size=20,
                            weight=ft.FontWeight.BOLD,
                            color="black"),
                            name_input,
                            qty_input,
                            ft.Row([
                                ft.OutlinedButton("장바구니", on_click=add_cart),
                                ft.OutlinedButton("구매", on_click=buy),
                            ]),
                            ft.Divider(),
                            ft.Container(content=cart_view, height=200),
                            total_text,
                            today_text,
                            ft.Divider(),
                            admin_text,
                            ft.Row([
                                ft.OutlinedButton("관리자 토글", on_click=toggle_admin),
                                ft.OutlinedButton("상품 수정", on_click=update_item),
                                ft.OutlinedButton("할인 갱신", on_click=lambda e: load_discount()),
                            ]),
                            admin_name_input,
                            price_input,
                            stock_input,
                            output
                        ]
                    )
                ),

                ft.Container(
                    width=250,
                    padding=10,
                    border_radius=10,
                    bgcolor="white",
                    border=ft.border.all(2, "#ffe082"),
                    content=ft.Column(
                        expand=True,
                        controls=[
                            ft.Text("🎁 할인 목록 🎁",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color="black"),
                            ft.Container(content=discount_view, expand=True)
                        ]
                    )
                )

            ]
        )
    )

    load_danger()
    load_discount()


ft.app(target=main)