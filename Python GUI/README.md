# Python GUI · tkinter 위젯

tkinter 기본 위젯을 파일 하나에 하나씩 띄워 옵션과 이벤트를 익힌 파일과 콘솔 가위바위보 게임을 모은 폴더.
tkinter `Label`과 `Text` 예제는 [`flet`](../flet/README.md#tkinter-기초) 폴더에 있음.

## 목차

1. [tkinter 위젯](#1-tkinter-위젯)
2. [콘솔 게임](#2-콘솔-게임)
   - [가위바위보](#가위바위보)

---

## 1. tkinter 위젯

모든 파일은 `from tkinter import *`로 시작해 `Tk()` 창을 만들고 `pack()`으로 위젯을 배치한 뒤 `mainloop()`로 창을 띄움.

| 위젯 | 파일 | 연습한 옵션·이벤트 |
|---|---|---|
| `Button` | [`GUIBUTTON.py`](GUIBUTTON.py) | `command`에 plus·minus 함수를 연결하고 `global count`를 바꾼 뒤 `label.config(text=...)`로 숫자 갱신 |
| `Checkbutton` | [`CheckButton.py`](CheckButton.py) | `variable`에 연결한 `IntVar`로 체크 상태 0과 1을 읽고 `messagebox.showinfo`로 표시. `select()`와 `deselect()`로 전체 선택·해제 버튼 구성 |
| `Frame` | [`Frame.py`](Frame.py) | `relief="solid"`, `bd=2` 테두리 프레임 두 개를 `pack(side=..., fill="both", expand=True)`로 좌우에 나누고 각각 `Label` 배치 |
| `Listbox` | [`Listbox.py`](Listbox.py) · [`Listbox_2.py`](Listbox_2.py) · [`Listbox_3.py`](Listbox_3.py) · [`Listbox_4.py`](Listbox_4.py) | 항목 삽입과 선택 항목 삭제, `Entry` 입력 추가. 작성본별 차이는 아래 표 |
| `Message` | [`Message.py`](Message.py) | `width=320`으로 정한 폭에서 여러 줄 문자열 표시, `relief="solid"` 테두리 |
| `Scale` | [`Scale.py`](Scale.py) | `orient="horizontal"`과 `tickinterval=10`으로 0부터 100까지 눈금 슬라이더 구성. `command`에서 `scale.get()` 값을 `Label`에 표시 |
| `Scrollbar` | [`Scrollbar.py`](Scrollbar.py) | `Listbox`의 `yscrollcommand=scrollbar.set`과 `scrollbar["command"] = listbox.yview`로 두 위젯을 양방향 연결 |

`Listbox` 작성본 비교

| 파일 | 달라진 내용 |
|---|---|
| [`Listbox.py`](Listbox.py) | `insert(0, ...)`로 항목을 맨 앞에 넣어 입력 역순으로 표시. `selectmode="extended"`로 여러 항목 선택, `height=0`으로 항목 수만큼 높이 조정 |
| [`Listbox_2.py`](Listbox_2.py) | 파이썬 리스트 `items`로 목록을 채우고 `Delete` 버튼 추가. `curselection()`으로 얻은 선택 위치의 항목을 리스트와 위젯에서 함께 삭제 |
| [`Listbox_3.py`](Listbox_3.py) | `Entry`를 추가하고 `bind("<Return>", add)`로 Enter 키를 누르면 입력값을 리스트와 위젯에 추가 |
| [`Listbox_4.py`](Listbox_4.py) | Enter 키 바인딩 대신 `Insert` 버튼의 `command=add`로 추가. `add(event=None)`으로 기본 인자를 둬 인자 없는 버튼 호출에 대응 |

핵심 코드 `Listbox_2.py`

```python
def delete():
    global items
    selection = listbox.curselection()
    if(len(selection) == 0):
        return

    value = listbox.get(selection[0])
    ind = items.index(value)
    del items[ind]
    listbox.delete(selection[0])
    print(items)
```

구현 포인트
- `Listbox` 작성본은 화면 목록과 파이썬 리스트 `items`를 함께 고쳐 두 목록을 같은 상태로 유지. 삭제 후 `print(items)`로 리스트 상태를 콘솔에 출력.
- 선택 항목이 없으면 `curselection()`이 빈 튜플을 돌려주므로 길이 검사 후 바로 반환. `selectmode="extended"`에서 여러 개를 골라도 첫 선택 항목만 삭제.
- `Scrollbar.py`는 두 위젯을 `Frame` 하나에 담아 스크롤바는 오른쪽, 목록은 왼쪽에 배치.

---

## 2. 콘솔 게임

### 가위바위보

[`RSPQuiz.py`](RSPQuiz.py) · 함수 없이 반복문과 조건문으로 작성한 콘솔 프로그램

컴퓨터는 `random.randint(0, 2)`로 수를 내고 사용자는 0·1·2 중 하나를 입력. 무승부를 포함해 5판 안에 3점을 먼저 얻는 쪽이 승리.

| 경우 | 처리 |
|---|---|
| 같은 수 | 무승부. 남은 횟수 `count`만 1 감소 |
| 사용자·컴퓨터가 `0·1`, `1·2`, `2·0` | 사용자 승. `u_score` 1 증가 |
| 그 밖의 조합 | 컴퓨터 승. `c_score` 1 증가 |
| 한쪽이 3점 도달 | 승리 문구 출력 후 종료 |
| 남은 횟수 0 | 점수 비교 없이 `횟수가 전부 소모 되었습니다.` 출력 후 종료 |

핵심 코드

```python
if u_score >= 3 :
    print("축하합니다. 유저의 승리입니다!")
    break

elif c_score >= 3 :
    print("컴퓨터가 승리했습니다.")
    break

elif count == 0 and (c_score < 3 and u_score < 3) :
    print("횟수가 전부 소모 되었습니다.")
    break
```

구현 포인트
- 입력 숫자를 `com_ran = ["Rock", "Scissors", "Paper"]`의 인덱스로 그대로 써서 수 이름 출력. 번호 순서상 각 수가 다음 번호의 수를 이기므로 사용자 승 조합 세 가지는 `computer == (user + 1) % 3`과 같은 뜻.
- 무승부도 한 판으로 세어 `count`를 줄임.
- 판마다 바깥 `while`에서 3점 도달을 먼저 확인하고 횟수 소진은 마지막에 확인. 5판째에 3점이 되면 소진 문구가 아니라 승리 문구 출력.
- 안쪽 `while True`는 모든 분기가 `break`로 끝나 한 판에 한 번만 실행.

실행 결과

`0`, `1`, `2`, `0`, `1`을 표준 입력으로 넣은 결과. 컴퓨터의 수는 실행마다 달라지며 입력값은 출력에 나타나지 않음.

3점 선승으로 끝난 경우

```text
0.Rock , 1.Scissors, 2.Paper input your number on 0,1,2 : 컴퓨터는  Scissors ,유저는  Rock 입니다.
유저의 승리입니다. 승점 1점을 획득하셨습니다. 
총 승점  1 점 입니다.
횟수는  4 회 남았습니다.
0.Rock , 1.Scissors, 2.Paper input your number on 0,1,2 : 컴퓨터는  Paper ,유저는  Scissors 입니다.
유저의 승리입니다. 승점 1점을 획득하셨습니다. 
총 승점  2 점 입니다.
횟수는  3 회 남았습니다.
0.Rock , 1.Scissors, 2.Paper input your number on 0,1,2 : 컴퓨터는  Rock ,유저는  Paper 입니다.
유저의 승리입니다. 승점 1점을 획득하셨습니다. 
총 승점  3 점 입니다.
횟수는  2 회 남았습니다.
축하합니다. 유저의 승리입니다!
```

5판을 모두 쓴 경우

```text
0.Rock , 1.Scissors, 2.Paper input your number on 0,1,2 : 컴퓨터는  Rock ,유저는  Rock 입니다.
무승부 입니다.
횟수는  4 회 남았습니다.
0.Rock , 1.Scissors, 2.Paper input your number on 0,1,2 : 컴퓨터는  Paper ,유저는  Scissors 입니다.
유저의 승리입니다. 승점 1점을 획득하셨습니다. 
총 승점  1 점 입니다.
횟수는  3 회 남았습니다.
0.Rock , 1.Scissors, 2.Paper input your number on 0,1,2 : 컴퓨터는  Paper ,유저는  Paper 입니다.
무승부 입니다.
횟수는  2 회 남았습니다.
0.Rock , 1.Scissors, 2.Paper input your number on 0,1,2 : 컴퓨터는  Paper ,유저는  Rock 입니다.
컴퓨터의 승리입니다. 
총 승점  1 점 입니다.
횟수는  1 회 남았습니다.
0.Rock , 1.Scissors, 2.Paper input your number on 0,1,2 : 컴퓨터는  Scissors ,유저는  Scissors 입니다.
무승부 입니다.
횟수는  0 회 남았습니다.
횟수가 전부 소모 되었습니다.
```
