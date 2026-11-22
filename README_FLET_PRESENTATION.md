# Python Flet GUI 프로그래밍 발표

> **서지섭**  
> 자료구조 + GUI 프로그래밍 프로젝트 발표

---

## 📌 목차

1. [Flet이란?](#-flet이란)
2. [프로젝트 구성](#-프로젝트-구성)
3. [MakeListSet — 자료구조 + GUI](#-makelistset--자료구조--gui)
   - [수식 계산기](#1-수식-계산기-수식계산기_fletpy)
   - [DFS 미로 탐색](#2-dfs-미로-탐색-미로탐색_깊이우선_fletpy)
   - [라인 편집기](#3-라인-편집기-라인편집기_fletpy)
4. [flet — 응용 GUI 프로그램](#-flet--응용-gui-프로그램)
   - [숫자 계산기](#4-숫자-계산기-calculator_fletpy)
   - [마켓 관리 시스템](#5-마켓-관리-시스템-marketpy)
5. [핵심 Flet 개념 정리](#-핵심-flet-개념-정리)
6. [배운 점 & 느낀 점](#-배운-점--느낀-점)

---

## 🧩 Flet이란?

**Flet**은 Python으로 데스크탑·웹·모바일 GUI 앱을 만들 수 있는 프레임워크입니다.  
Flutter(Google)의 렌더링 엔진을 사용하므로 **빠르고 예쁜 UI**를 Python 코드만으로 구현할 수 있습니다.

```python
import flet as ft

def main(page: ft.Page):
    page.title = "Hello Flet"
    page.add(ft.Text("Hello, World!", size=30))

ft.app(target=main)
```

| 특징 | 설명 |
|------|------|
| 언어 | Python |
| 렌더링 | Flutter 기반 |
| 지원 플랫폼 | Windows / macOS / Linux / 웹 |
| 설치 | `pip install flet` |

---

## 📁 프로젝트 구성

```
Python/
├── MakeListSet/          # 자료구조 알고리즘 + Flet GUI
│   ├── 수식계산기_flet.py         ← 스택 기반 수식 계산
│   ├── 미로탐색_깊이우선_flet.py  ← DFS 시각화
│   └── 라인편집기_flet.py         ← 리스트 기반 파일 편집기
│
└── flet/                 # 응용 GUI 프로그램
    ├── calculator_flet.py         ← 다중 숫자 계산기
    └── market.py                  ← 마켓 관리 시스템
```

---

## 📚 MakeListSet — 자료구조 + GUI

### 1. 수식 계산기 (`수식계산기_flet.py`)

#### 개요
괄호를 포함한 중위 표기식을 **후위 표기식으로 변환**하고 계산하는 GUI 계산기입니다.

#### 적용 자료구조
- **스택(Stack)** — 괄호 검사, 연산자 우선순위 처리, 후위 표기식 계산

#### 핵심 알고리즘

```
중위 표기식: 3 + ( 5 * 2 )
후위 표기식: 3 5 2 * +
계산 결과:   13
```

```python
class calculate:
    def check_brackets(self, expr):      # 스택으로 괄호 짝 검사
    def infix_to_postfix(self, expr):    # 중위 → 후위 변환
    def evaluate_postfix(self, expr):    # 후위 표기식 계산
```

#### Flet UI 구성

```python
# 버튼 생성 헬퍼 함수
def make_btn(label, val=None, color="#f0f0f0", ...):
    return ft.ElevatedButton(label, on_click=btn_click(val), ...)

# 버튼을 Row/Column으로 배치
button_pad = ft.Column([
    ft.Row([make_btn("7"), make_btn("8"), make_btn("9"), make_btn("/")]),
    ft.Row([make_btn("4"), ...]),
    ...
])
```

#### 실행 화면 설명
- 상단 입력창에 식을 타이핑하거나 버튼으로 입력
- `계산` 버튼 클릭 시 괄호 오류 검사 후 결과 출력
- `⌫` (백스페이스), `C` (초기화) 버튼 지원

---

### 2. DFS 미로 탐색 (`미로탐색_깊이우선_flet.py`)

#### 개요
**깊이 우선 탐색(DFS)** 알고리즘으로 미로를 탐색하는 과정을 **실시간 시각화**합니다.

#### 적용 자료구조
- **스택(Stack)** — DFS 탐색 경로 관리

#### 미로 구조

```
■ ■ ■ ■ ■ ■
S □ □ □ □ ■
■ □ ■ □ ■ ■
■ ■ ■ □ □ E
■ ■ ■ ■ ■ ■
■ ■ ■ ■ ■ ■
```
`S` = 시작, `E` = 출구, `■` = 벽, `□` = 통로

#### 핵심 코드 — 비동기 탐색

```python
async def solve(self, e):          # async로 UI 멈춤 없이 진행
    self.stack.append(start)

    while self.stack:
        pos = self.stack.pop()     # 스택에서 꺼내기
        r, c = pos

        if self.visited[r][c]:
            continue

        self.visited[r][c] = True
        self.cells[r][c].bgcolor = ft.Colors.YELLOW_400  # 현재 위치 표시
        self.page.update()

        await asyncio.sleep(0.3)   # 0.3초 대기 → 탐색 과정 시각화

        # 상하좌우 이웃 셀을 스택에 추가
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            ...
            self.stack.append((nr, nc))
```

#### Flet 핵심 포인트
- `asyncio.sleep()` 으로 UI 블로킹 없이 애니메이션 구현
- `ft.Container` 의 `bgcolor` 변경으로 셀 색상 실시간 업데이트
- 탐색 중 버튼 비활성화(`disabled=True`)로 중복 실행 방지

#### 색상 의미
| 색상 | 의미 |
|------|------|
| 초록 | 시작점 (S) |
| 빨강 | 출구 (E) |
| 노랑 | 현재 탐색 위치 |
| 파랑 | 이미 방문한 경로 |
| 회색(진) | 벽 |

---

### 3. 라인 편집기 (`라인편집기_flet.py`)

#### 개요
텍스트 파일을 **줄 단위로 삽입·수정·삭제**할 수 있는 파일 편집기입니다.

#### 적용 자료구조
- **리스트(List)** — 줄 목록을 Python 리스트로 관리

#### 핵심 연산

```python
class FileIO:
    def i(self, line_no, text):    # 삽입 (Insert)
        self.line_num = self.line_num[:line_no-1] + [text] + self.line_num[line_no-1:]

    def d(self, line_no):          # 삭제 (Delete)
        self.line_num = self.line_num[:line_no-1] + self.line_num[line_no:]

    def r(self, line_no, text):    # 수정 (Replace)
        self.line_num[line_no-1] = text

    def l(self):                   # 파일 불러오기 (Load)
    def s(self):                   # 파일 저장 (Save)
```

#### Flet UI 구성
- `ft.ListView` — 파일 내용을 스크롤 가능한 목록으로 표시
- `ft.TextField` — 줄 번호와 텍스트 입력
- `ft.ElevatedButton` — 삽입 / 수정 / 삭제 / 저장 / 불러오기 / 종료
- 어두운 테마(`#1e1e2e`) 적용

---

## 🖥️ flet — 응용 GUI 프로그램

### 4. 숫자 계산기 (`calculator_flet.py`)

#### 개요
여러 숫자를 입력받아 **덧셈·뺄셈·곱셈·나눗셈·평균·최댓값·최솟값**을 한 번에 계산합니다.

#### 핵심 코드

```python
class Calculator:
    def get_all_results(self):
        results["add"]      = sum(self.numbers)
        results["subtract"] = ...   # 순차 빼기
        results["multiply"] = ...   # 순차 곱하기
        results["divide"]   = ...   # 0으로 나누기 예외 처리 포함
        results["average"]  = sum(self.numbers) / len(self.numbers)
        results["max"]      = max(self.numbers)
        results["min"]      = min(self.numbers)
        return results
```

#### Flet UI 구성
- 쉼표(`,`)로 숫자를 구분하여 입력 (`1,2,3,4,5`)
- `ft.BoxShadow` 로 결과 박스에 그림자 효과 적용
- 예외 처리: 빈 입력, 0으로 나누기, 정수가 아닌 입력

---

### 5. 마켓 관리 시스템 (`market.py`)

#### 개요
편의점/마트를 시뮬레이션한 **장바구니 + 재고 관리 + 할인 시스템** GUI 앱입니다.

#### 주요 기능

| 기능 | 설명 |
|------|------|
| 장바구니 | 상품명·수량 입력 후 장바구니에 추가 |
| 구매 | 영수증(`receipt.txt`) 자동 저장 |
| 재고 경고 | 재고 5개 이하 상품을 빨간 패널에 표시 |
| 할인 목록 | 랜덤 5개 상품 10% 할인 표시 |
| 관리자 모드 | 가격 수정, 재고 추가 가능 |
| 데이터 영속성 | `market.json`에 상품 데이터 저장/로드 |

#### 핵심 코드

```python
# 할인 상품 랜덤 선정
def load_discount():
    for k in random.sample(list(market.keys()), 5):
        v = market[k]
        v["price"] = int(v["original_price"] * 0.9)   # 10% 할인

# 구매 시 영수증 저장
def buy(e):
    with open("receipt.txt", "a", encoding="utf-8") as f:
        f.write(receipt + "\n\n")
```

#### Flet UI 레이아웃 — 3단 구성

```
┌─────────────┬──────────────────┬─────────────┐
│  🚨 재고 부족 │     Market        │  🎁 할인 목록 │
│  (빨간 패널) │  (메인 조작 영역)  │  (노란 패널) │
└─────────────┴──────────────────┴─────────────┘
```

```python
ft.Row([
    ft.Container(width=250, ...),   # 재고 부족 패널
    ft.Container(expand=True, ...),  # 메인 패널
    ft.Container(width=250, ...),   # 할인 목록 패널
])
```

---

## 💡 핵심 Flet 개념 정리

### Page & 기본 구조

```python
def main(page: ft.Page):
    page.title = "앱 제목"
    page.bgcolor = "#ffffff"
    page.add(ft.Text("Hello"))      # 컴포넌트 추가

ft.app(target=main)
```

### 자주 사용한 컴포넌트

| 컴포넌트 | 용도 |
|----------|------|
| `ft.Text` | 텍스트 표시 |
| `ft.TextField` | 사용자 입력 |
| `ft.ElevatedButton` | 버튼 |
| `ft.Row` | 가로 배치 |
| `ft.Column` | 세로 배치 |
| `ft.Container` | 스타일 래퍼 (배경색, 테두리, 패딩) |
| `ft.ListView` | 스크롤 가능한 목록 |
| `ft.Divider` | 구분선 |

### 이벤트 처리 패턴

```python
def on_click(e):
    # 상태 변경
    result_text.value = "결과"
    page.update()           # ← 반드시 호출해야 화면 갱신

button = ft.ElevatedButton("클릭", on_click=on_click)
```

### 비동기 UI 업데이트

```python
import asyncio

async def animate(e):
    for i in range(10):
        label.value = str(i)
        page.update()
        await asyncio.sleep(0.5)   # UI를 막지 않고 대기
```

---

## 🎯 배운 점 & 느낀 점

### 자료구조 → GUI 시각화
- 스택, 큐, 리스트 같은 **추상적인 자료구조**를 GUI로 시각화하니 동작 원리가 더욱 명확하게 이해됨
- 특히 DFS 미로 탐색은 스택이 어떻게 경로를 관리하는지 **눈으로** 확인할 수 있어 인상적

### Flet의 장점
- Python만으로 **빠르게** 데스크탑 GUI를 만들 수 있음
- `ft.Row`, `ft.Column`, `ft.Container`의 조합만으로 다양한 레이아웃 구현 가능
- `asyncio` 와의 결합으로 **애니메이션**도 구현 가능

### 어려웠던 점
- `page.update()` 를 빠뜨리면 화면이 갱신되지 않아 처음에 자주 실수
- 비동기(`async/await`) 개념이 생소해서 DFS 애니메이션 구현에 시간이 걸림
- 레이아웃 배치 시 `expand=True` 설정이 예상과 다르게 동작하는 경우가 있었음

---

## 🛠 실행 방법

```bash
# Flet 설치
pip install flet

# 각 파일 실행
python MakeListSet/수식계산기_flet.py
python MakeListSet/미로탐색_깊이우선_flet.py
python MakeListSet/라인편집기_flet.py
python flet/calculator_flet.py
python flet/market.py
```

---

*서지섭*
