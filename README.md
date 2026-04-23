## 🎯 확률 시뮬레이터 (가챠 뽑기 분석)

이 프로젝트는 **가챠(뽑기) 시스템에서 특정 아이템(펫)을 획득할 확률**을 시뮬레이션으로 계산하는 Python 프로그램입니다.  
단순한 수식 계산이 아닌 **Monte Carlo 시뮬레이션**을 통해 실제 뽑기와 유사한 결과를 제공합니다.

---

### 📌 제작 목적
- “몇 번 뽑으면 몇 개 정도 얻을 수 있을까?”를 직관적으로 확인하기 위해 제작
- 확률이 낮은 이벤트에서 **체감 확률과 실제 확률의 차이**를 확인

---

### ⚙️ 작동 방식
- 1회 뽑기 = 11번 시도
- 각 시도마다 **2% 확률로 당첨**
- 총 `11 × n`번 반복 수행
- 이를 **1,000,000번 반복**하여 통계적으로 안정된 결과 생성

---

### 📊 결과 해석 방법
- 각 숫자는 “펫을 해당 개수만큼 얻을 확률”을 의미
- 예: `3개 | 25%` → 전체 시도 중 약 25% 확률로 3개 획득
- 기대값뿐 아니라 **분포(운이 좋을/나쁠 확률)**까지 확인 가능
---

### 📓 작성 코드
```python
import random

trials = 1000000
max_pet = 8 #최대 계산하는 당첨 마릿수
single_prob = 0.02 #뽑기 당첨 확률

# 11회 뽑기 횟수 입력
n = int(input("뽑기 횟수 입력 (1회 시도마다 11번 도전): "))

counts = [0] * (max_pet + 1)

for _ in range(trials):
    pets = 0

    # 총 뽑기 횟수 = 11 * n
    for _ in range(n * 11):
        if pets < max_pet and random.random() < single_prob:
            pets += 1

    counts[pets] += 1

# 확률 계산
probabilities = [c / trials * 100 for c in counts]

print("\n==============================")
print("      🎯 확률 분석 결과")
print("==============================")

print("획득 개수 | 확률(%)")
print("------------------------")

for i in range(max_pet + 1):
    print(f"{i}개      | {probabilities[i]:.2f}%")

print("==============================\n")
```
---

### 📷 실행 결과
> 아래 이미지는 실제 실행 결과 예시입니다.

![preview](https://raw.githubusercontent.com/seo941024/Python/master/Practice/petcalc.png)

---

### 🛠 사용 기술
- Python
- Monte Carlo Simulation

---

### 💡 활용 예시
- 게임 가챠 확률 분석
- 확률 분포 이해 및 학습
- 뽑기 횟수 대비 기대 결과 예측
