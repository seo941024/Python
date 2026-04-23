### 🐍 Python 프로젝트 (대표 프로젝트)
👉 https://github.com/seo941024/Python-GUI  

#### 💻 핵심 코드

```python
import random

trials = 1000000
max_pet = 8 #최대 계산하는 당첨 마릿수
single_prob = 0.03 #뽑기 당첨 확률

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
#### 📸 프로젝트 실행화면

![preview](https://raw.githubusercontent.com/seo941024/Python-GUI/master/result.png)

**📌 설명**  
- Python을 활용한 다양한 연습 프로젝트 진행  
- GUI 프로그램 제작 및 사용자 입력 처리 구현  
- 확률 기반 자석펫 뽑기 시뮬레이션 구현  

**⚙️ 사용 기술**  
- Python  
- random 모듈  
- Monte Carlo Simulation  

**💻 핵심 기능**
- GUI 기본 구조 구현  
- 게임 확률 시뮬레이션  
- 반복 실험 기반 결과 분석  

**🧠 배운 점**  
- 이벤트 기반 처리 흐름 이해  
- 확률 시뮬레이션 구조 학습  
- 랜덤 기반 모델링 경험  
