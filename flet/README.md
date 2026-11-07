# flet · Flet 응용 프로그램과 화면 구성

Flet으로 만든 화면 프로그램과 화면 배치 연습 파일을 모은 폴더.
화면 없이 동작하는 로또 콘솔 프로그램과 tkinter 기초 예제 두 개도 함께 포함.

## 목차

1. [응용 프로그램](#1-응용-프로그램)
   - [상점 관리](#상점-관리)
   - [전화번호부](#전화번호부)
   - [다중 숫자 계산기](#다중-숫자-계산기)
   - [볼링 점수 화면](#볼링-점수-화면)
   - [로또 번호 추첨](#로또-번호-추첨)
2. [화면 구성 연습](#2-화면-구성-연습)
   - [라벨 겹침 상자](#라벨-겹침-상자)
   - [음향 분석 모니터](#음향-분석-모니터)
   - [tkinter 기초](#tkinter-기초)

---

## 1. 응용 프로그램

### 상점 관리

[`market.py`](market.py) · [`import random.py`](import%20random.py) · 함수 `main`

왼쪽에 재고 부족 목록, 오른쪽에 할인 목록을 두고 가운데에서 장바구니와 구매를 처리하는 Flet 상점 화면. 두 파일은 화면 제목 `Simple Market`과 세 칸 배치가 같고 장바구니·구매 처리 흐름도 같은 상점 화면의 작성본. `market.py`는 여기에 파일 저장과 관리자 모드가 더해진 형태. 아래 함수 표는 `market.py` 기준.

| 함수 | 동작 |
|---|---|
| `find(name)` | 입력 이름과 저장된 이름의 앞뒤 공백을 지우고 비교해 상품 번호와 정보 반환 |
| `load_danger()` | 재고 오름차순으로 정렬해 재고 5개 이하 상품만 왼쪽 목록에 표시 |
| `load_discount()` | 모든 가격을 원래 가격으로 되돌린 뒤 무작위 상품 5개만 10% 할인 |
| `add_cart(e)` | 입력값과 재고를 확인한 뒤 재고를 줄이고 장바구니와 장바구니 목록 화면에 추가, `market.json` 저장 |
| `buy(e)` | 장바구니로 영수증 문자열을 만들어 `receipt.txt`에 이어 쓰고 오늘 매출에 누적 |
| `toggle_admin(e)` | 관리자 모드 켜기와 끄기 |
| `update_item(e)` | 관리자 모드일 때만 가격 수정과 재고 추가, 가격을 고치면 `original_price`도 함께 변경 |
| `save_data()` | 상품 사전 `market`을 `market.json`에 들여쓰기 4칸으로 저장 |

핵심 코드

```python
def load_discount():
    discount_view.controls.clear()
    for v in market.values():
        v["price"] = v["original_price"]

    for k in random.sample(list(market.keys()), 5):
        v = market[k]
        old = v["original_price"]
        new_price = int(old * 0.9)
        v["price"] = new_price
```

작성본 비교

| 구분 | `import random.py` | `market.py` |
|---|---|---|
| 상품 이름 | `상품1`부터 `상품100`까지 자동 생성 | 생활용품과 식품 이름 목록 |
| 상품 데이터 | 실행마다 새로 생성하고 파일에 저장하지 않음 | `market.json`이 있으면 불러오고 없으면 생성 |
| 상품 번호 | 정수 | `str()`로 바꾼 문자열 |
| 가격 필드 | `price` 하나 | `price`와 `original_price` |
| 할인 상품 선택 | `random.choice`를 5번 호출하고 중복이면 건너뛰어 5개 미만 가능 | `random.sample`로 서로 다른 5개 |
| 할인 갱신 | 시작 시 한 번 | 시작 시 한 번과 `할인 갱신` 버튼 |
| 할인 목록 생성 후 `page.update()` | 호출 없음 | 호출 |
| 재고 경고 순서 | 사전에 들어간 순서 | 재고 오름차순 |
| 영수증 기록 | `"w"` 모드로 덮어쓰기 | `"a"` 모드로 이어 쓰기 |
| 상품 정보 저장 | 없음 | 상품 정보가 바뀌거나 구매할 때 `market.json` 저장 |
| 관리자 모드 | 없음 | 가격 수정과 재고 추가 |
| 화면 금액 표시 | 숫자 그대로 | 천 단위 쉼표 |

데이터 파일

| 파일 | 읽고 쓰는 프로그램 | 형식 |
|---|---|---|
| [`market.json`](market.json) | `market.py`가 시작 시 읽고, 상품 정보가 바뀌거나 구매할 때마다 전체를 다시 씀 | 상품 번호 문자열을 키로 하는 JSON 객체 |
| [`receipt.txt`](receipt.txt) | `market.py`는 구매마다 이어 쓰고 `import random.py`는 구매마다 덮어씀 | 구매 한 번에 영수증 한 묶음인 텍스트 |

`market.json` 상품 하나의 필드

| 필드 | 뜻 |
|---|---|
| `name` | 상품 이름 |
| `stock` | 재고 수량 |
| `price` | 현재 판매가, 할인 상품이면 할인가 |
| `original_price` | 할인 전 가격 |

`market.json`에 저장된 할인 상품 예. `price`가 `original_price`의 90%로 기록된 상태.

```json
"68884": {
    "name": "휴지",
    "stock": 22,
    "price": 6660,
    "original_price": 7400
},
```

`receipt.txt`에 `market.py`가 남긴 영수증 예.

```text
=== 영수증 ===
참기름 x1 = 1710원
소금 x3 = 25920원
파스타 x5 = 40500원

이번 구매: 68130원
오늘 총 매출: 68130원
```

구현 포인트
- 할인가가 `price`에 들어간 채 `market.json`에 저장돼도 다음 실행의 `load_discount()`가 먼저 `original_price`로 되돌리므로 할인이 겹치지 않음.
- 재고는 구매 시점이 아니라 장바구니에 담는 시점에 줄이고 곧바로 `market.json`에 저장.
- 화면 상태 값은 `main` 안의 지역 변수로 두고 중첩 함수에서 `nonlocal`로 변경. 오늘 매출은 파일에 저장하지 않아 다시 실행하면 0부터 시작.
- 새 상품 번호는 1부터 100000 사이 난수로 만들고, 이미 있는 번호면 `continue`로 다시 뽑음.

수정 이력
- `market.py`의 장바구니 목록 영역 `cart_view`에 품목을 추가하는 코드가 없어 담은 상품이 화면에 표시되지 않음. 담을 때 `품목 x수량 = 금액` 행을 추가하고 구매 후 목록을 비우도록 수정

### 전화번호부

[`Call.py`](Call.py) · 함수 `load_data`, `save_data`, `main`

연락처를 카드 목록으로 보여 주고 관리하는 Flet 화면. 왼쪽은 입력 영역, 오른쪽은 카드 목록이며 목록이 바뀔 때마다 `people.csv` 전체를 다시 저장. 저장 항목은 `keys` 리스트에 정한 네 개로, CSV 열 순서와 같음.

| 함수 | 동작 |
|---|---|
| `load_data()` | `people.csv`가 있으면 `csv.DictReader`로 읽어 사전 리스트 반환, 없으면 빈 리스트 |
| `save_data(people)` | `csv.DictWriter`로 머리글 행과 전체 목록을 덮어씀 |
| `create_card(p, index)` | 한 사람의 정보를 카드로 만들고 수정·삭제 버튼에 목록 위치를 연결 |
| `refresh_list(data=None)` | `(전체 목록 위치, 사람)` 쌍으로 카드를 다시 그림. 인자가 없으면 전체 목록, 있으면 검색 결과 |
| `add_person(e)` | 입력칸 네 개의 값을 사전으로 묶어 추가하고 저장 |
| `load_edit(index)` | 선택한 사람의 정보를 입력칸에 채우고 위치를 기억 |
| `update_person(e)` | 기억한 위치의 정보를 입력칸 값으로 바꾸고 저장 |
| `delete_person(index)` | 위치가 범위 안일 때만 삭제하고 저장. 수정 중인 사람의 위치도 삭제에 맞춰 조정 |
| `search(e)` | 한 사람의 네 항목을 이어 붙인 문자열에서 대소문자 구분 없이 검색어 포함 여부 확인. 결과에 전체 목록 기준 위치를 함께 저장 |

핵심 코드

```python
def load_data():
    data = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    return data
```

데이터 파일

[`people.csv`](people.csv)는 `Call.py`가 시작 시 읽고 목록이 바뀔 때마다 전체를 다시 쓰는 CSV 파일. 첫 행은 머리글이고 파일 앞에 UTF-8 BOM이 붙어 있음.

```text
이름,이메일,전화번호,직장명
가나디,123@naver.com,010-1111-1234,카카오
```

구현 포인트
- 읽기와 쓰기 모두 `encoding="utf-8-sig"`를 써서 BOM이 있는 파일에서도 첫 열 이름을 `이름` 그대로 인식.
- 쓰기는 `newline=""`로 열어 `csv` 모듈이 줄바꿈을 처리하게 함.
- 카드 버튼은 `lambda e, i=index: load_edit(i)`처럼 기본 인자로 위치를 고정해 반복문의 마지막 값이 아닌 카드별 위치를 넘김.
- 수정 중인 위치를 `selected_index = {"value": None}` 사전에 담아 `nonlocal` 선언 없이 중첩 함수에서 바꿈.

수정 이력
- 검색 결과 카드가 검색 결과 안의 순서를 위치로 넘겨, 검색 후 수정·삭제 시 전체 목록의 다른 사람이 바뀌거나 지워짐. 검색 결과에 전체 목록 기준 위치를 함께 담아 카드에 전달하도록 수정
- 수정 중에 앞쪽 사람을 삭제하면 기억한 위치가 한 칸 어긋남. 삭제 위치에 맞춰 수정 중인 위치를 조정
- 확인: 화면 없이 이벤트 처리 함수를 호출하는 검사로 검색 후 삭제, 검색 후 수정, 수정 중 삭제 세 경우의 저장 결과 확인

### 다중 숫자 계산기

[`calculator_flet.py`](calculator_flet.py) · 클래스 `Calculator`, 함수 `main`

쉼표로 구분한 정수 여러 개를 받아 사칙연산과 통계값을 한 번에 보여 주는 Flet 화면. 계산은 `Calculator` 클래스, 입력 변환과 결과 문자열 구성은 화면 함수 `run_calc`가 담당.

| 결과 키 | 계산 방식 |
|---|---|
| `add` | `sum()`으로 전체 합 |
| `subtract` | 첫 수에서 나머지 수를 차례로 뺌 |
| `multiply` | 1에서 시작해 모든 수를 차례로 곱함 |
| `divide` | 첫 수를 나머지 수로 차례로 나눔 |
| `average` | 합을 개수로 나눔 |
| `max` | `max()` |
| `min` | `min()` |

핵심 코드

```python
div = self.numbers[0]
for n in self.numbers[1:]:
    if n == 0:
        div = "Cannot divide by zero"
        break
    div /= n
results["divide"] = div
```

구현 포인트
- 0 검사는 나누는 수인 두 번째 수부터 적용. 0을 만나면 반복을 멈추고 나눗셈 자리에만 오류 문자열을 넣어 나머지 결과는 그대로 표시.
- 입력은 `split(",")` 뒤 `int`로 변환하므로 정수만 허용. 변환에 실패하면 `except`에서 `정수를 쉼표로 구분해서 입력하세요` 안내.
- 결과가 사전이면 항목별 문자열로, 문자열이면 그대로 표시하도록 `isinstance`로 분기.
- 평균만 `:.2f`로 소수 둘째 자리까지 표시.

### 볼링 점수 화면

[`flet_bowling.py`](flet_bowling.py) · 클래스 `BowlingGame`, 함수 `main`

투구마다 쓰러뜨린 핀 수를 입력받아 프레임 표기와 누적 점수를 다시 계산하는 Flet 화면. 투구 기록 리스트 하나만 저장하고 점수와 표기는 매번 이 기록에서 새로 계산.

| 메서드·함수 | 동작 |
|---|---|
| `add_throw(pins)` | 핀 수를 `throw_list` 끝에 추가 |
| `calculate_live_scores()` | 프레임별 누적 점수 리스트 반환. 보너스에 필요한 투구가 아직 없으면 그 프레임에서 계산 중단 |
| `format_frames()` | 프레임별 표기 문자열 반환. 10프레임은 남은 투구를 모두 이어 표시 |
| `update()` | 화면 함수 안에서 두 메서드 결과로 프레임 줄과 점수를 갱신하고 투구 기록을 `DEBUG:` 줄로 표시 |
| `add_throw(e)` | 입력이 0부터 10 사이 정수일 때만 기록하고 `update()` 호출 |

| 프레임 상태 | 표기 |
|---|---|
| 스트라이크 | `X` |
| 스페어 | `5/` |
| 두 투구 합이 10 미만 | `7-2` |
| 첫 투구만 한 상태 | `7` |
| 투구 전 | 공백 |

핵심 코드

```python
for _ in range(10):
    if i >= len(self.throw_list):
        break

    if self.throw_list[i] == 10:
        if i+2 >= len(self.throw_list):
            break
        total += 10 + self.throw_list[i+1] + self.throw_list[i+2]
        scores.append(total)
        i += 1
```

구현 포인트
- 프레임 구조를 따로 저장하지 않고 투구 기록과 인덱스 `i`로 프레임 경계를 계산. 스트라이크면 `i += 1`, 그 밖에는 `i += 2`.
- 스트라이크는 다음 두 투구, 스페어는 다음 한 투구가 있어야 점수를 더하고, 없으면 `break`로 멈춰 확정된 프레임까지만 누적 점수 반환.
- 10프레임 보너스 투구를 위한 분기가 없음. 열 번째 반복이 스트라이크·스페어 보너스로 뒤 투구를 더하는 계산이 10프레임 점수 규칙과 같은 결과.
- 화면의 `최종 점수`는 `scores[-1]`, 즉 지금까지 확정된 마지막 누적 점수.

### 로또 번호 추첨

[`import random as rand.py`](import%20random%20as%20rand.py) · 함수 없이 반복문과 조건문으로 작성한 콘솔 프로그램

1부터 43 사이 번호 6개를 입력받아 무작위 추첨 번호와 비교하고 등수를 출력. 화면 없이 콘솔에서 동작.

| 입력 | 처리 |
|---|---|
| 숫자가 아닌 값 | `숫자만 입력하세요.` 출력 후 다시 입력 |
| 1~43 밖의 숫자 | `1 ~ 43 사이 숫자만 입력하세요` 출력 후 다시 입력 |
| 이미 입력한 숫자 | `중복된 숫자입니다.` 출력 후 다시 입력 |
| 유효한 숫자 | `user_nums`에 추가, 6개가 모이면 추첨 |

| 등수 | 조건 |
|---|---|
| 1등 | 6개 일치 |
| 2등 | 5개 일치와 보너스 번호 일치 |
| 3등 | 5개 일치 |
| 4등 | 4개 일치 |
| 5등 | 3개 일치 |
| 꽝 | 2개 이하 일치 |

핵심 코드

```python
lotto = rd.sample(range(1, 44), 7)


main_lotto = lotto[:6]
bonus = lotto[6]
```

구현 포인트
- `rd.sample`로 중복 없는 7개를 한 번에 뽑아 앞 6개는 당첨 번호, 마지막 1개는 보너스 번호로 사용. 보너스 번호가 당첨 번호와 겹칠 수 없음.
- 일치 개수는 `len(set(user_nums) & set(main_lotto))`처럼 두 번호 묶음의 교집합 크기로 계산.
- 보너스 번호는 5개 일치일 때만 등수에 반영. 아래 실행에서도 보너스 번호 30만 맞아 꽝.
- 출력 전에 두 번호 묶음을 `sorted()`로 정렬해 비교하기 쉽게 표시.

실행 결과

`abc`, `44`, `7`, `7`, `3`, `15`, `22`, `30`, `41`을 표준 입력으로 차례로 넣은 결과. 입력값은 출력에 나타나지 않음.

```text
번호를 입력하세요 (1~43): 숫자만 입력하세요.
번호를 입력하세요 (1~43): 1 ~ 43 사이 숫자만 입력하세요
번호를 입력하세요 (1~43): 번호를 입력하세요 (1~43): 중복된 숫자입니다.
번호를 입력하세요 (1~43): 번호를 입력하세요 (1~43): 번호를 입력하세요 (1~43): 번호를 입력하세요 (1~43): 번호를 입력하세요 (1~43): 당첨 번호: [4, 20, 21, 26, 34, 42] + 보너스 [30]
내 번호: [3, 7, 15, 22, 30, 41]
꽝
```

---

## 2. 화면 구성 연습

기능 없이 화면 배치만 연습한 파일. Flet 두 개와 tkinter 두 개.

### 라벨 겹침 상자

[`flet_title.py`](flet_title.py) · 함수 `main`

`ft.Stack`으로 테두리 상자 위에 제목 라벨을 겹쳐, 테두리 선 위에 제목이 걸친 묶음 상자를 만든 Flet 화면. 상자 위에는 입력창과 확인 버튼 배치.

핵심 코드

```python
# 라벨 (위에 떠있는 효과)
ft.Container(
    content=ft.Text(" 아이템 박스 ", size=12, weight="bold"),
    bgcolor="white",
    padding=5,
    left=20,
    top=0
)
```

구현 포인트
- 테두리 상자에 `margin=ft.margin.only(top=10)`을 줘 라벨이 걸칠 자리를 위쪽에 확보.
- 라벨 `Container`에 흰 배경을 깔아 라벨 뒤를 지나는 테두리 선을 가림.
- 입력창의 `on_submit`과 버튼의 `on_click`에 같은 함수를 연결해 Enter와 버튼 모두 입력창을 비움.

### 음향 분석 모니터

[`Text.py`](Text.py) · 함수 `main` 안의 `create_card`

음향 센서로 굴착과 누출 같은 이벤트를 감지하는 관제 대시보드를 가정한 화면 시안. 화면의 수치와 이벤트 목록은 모두 코드에 고정한 값이며 버튼에는 동작을 연결하지 않음.

| 영역 | 구성 |
|---|---|
| 상단 | 제목과 시스템 상태 표시 |
| 왼쪽 | 센서 위치 맵과 반복문으로 만든 센서 상태 목록 |
| 가운데 | 스펙트로그램 모형과 감도 조절 `Slider` 패널 |
| 오른쪽 | 감지 이벤트 목록 |

핵심 코드

```python
def create_card(title, content, expand=False):
    return ft.Container(
        content=ft.Column([
            ft.Text(title, size=12, weight=ft.FontWeight.BOLD, color="#5B626A"),
            content
        ], spacing=10),
        bgcolor="#1A1D23",
        padding=15,
        border=ft.border.all(1, "#2D323A"),
        border_radius=0, # 완전 플랫
        expand=expand
    )
```

구현 포인트
- 모든 영역을 `create_card()` 하나로 감싸 카드 스타일을 통일. `expand` 인자로 가운데 스펙트로그램 카드만 남은 높이를 채움.
- 센서 맵과 스펙트로그램은 `ft.Stack` 안에서 위치 인자로 아이콘과 막대 자리를 지정.
- 이벤트 항목은 `ft.border.only(left=...)`로 왼쪽에만 색 띠를 두고 이벤트 종류마다 색을 다르게 지정.
- `ft.icons.WAVES`, `ft.alignment.center` 같은 이전 Flet 문법으로 작성. Flet 0.82.2에는 이 두 속성과 `Container`의 `min_height` 인자가 없음.

### tkinter 기초

이 폴더에 함께 들어 있는 tkinter 창 예제. 두 파일 모두 `geometry`로 창 크기와 위치를 정하고 `resizable(True, True)`로 크기 변경 허용.

| 파일 | 위젯 | 연습한 내용 |
|---|---|---|
| [`PYTHON GUI EXAMPLE.py`](PYTHON%20GUI%20EXAMPLE.py) | `Label` | `bitmap="warning"` 기본 이미지와 글자를 `compound="top"`으로 함께 표시, `relief="groove"` 테두리 |
| [`Text2.py`](Text2.py) | `Text` | `insert`로 두 줄 입력 후 `tag_add`로 `"행.열"` 범위에 태그를 붙이고 `tag_config`로 배경색과 글자색 지정 |

핵심 코드

```python
text.tag_add("here", "1.0", "1.5")
text.tag_add("start", "1.10", "1.17")
text.tag_config("here", background="yellow", foreground="red")
text.tag_config("start", background="black", foreground="white")
```

나머지 tkinter 위젯 연습은 [`Python GUI`](../Python%20GUI/README.md) 폴더에 정리.
