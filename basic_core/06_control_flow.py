"""
06. 프로그램 구성 - 제어문 (Control Flow)

이 파일에서 다루는 것:
- 프로그래밍 패러다임(programming paradigm) — 큰 그림 한 번
- 조건문(if statement): 상황에 따라 다른 코드 실행
- 중첩 제어문(nested control): if 안에 if, for 안에 for
- 반복문(for loop): 정해진 횟수/원소만큼 반복
- 반복문(while loop): 조건이 True인 동안 반복
- 루프 제어(loop control): break / continue

제어문(control flow): 코드의 "실행 흐름(흐름)"을 결정하는 문장.
파이썬은 들여쓰기(indentation)로 코드 블록(block)을 구분합니다 — 매우 중요!

프로그래밍 패러다임:
  - 절차적(procedural): 위에서 아래로 순서대로 실행 (이 파일 주제)
  - 객체지향(object-oriented, OOP): 클래스(class)와 객체(object)
  - 함수형(functional): 함수를 값처럼 전달
"""

# ============================================================
# 1. 조건문 (if Statement)
# ============================================================
# "만약 ~라면 A를 해라, 아니면 B를 해라"

# --- 기본 형태: if / elif / else ---
# elif = else if (else와 다른 if 를 합친 줄임말)
age = 17

if age < 13:
    category = "어린이"
elif age < 20:
    category = "청소년"
else:
    category = "성인"

print(f"나이 {age}세 → {category}")

# --- 조건 표현식 (conditional expression) — 한 줄짜리 if/else ---
score = 85
result = "합격" if score >= 60 else "불합격"
print(f"점수 {score} → {result}")

# ============================================================
# 2. 중첩 제어문 (Nested Control Statements)
# ============================================================
# if 블록 안에 또 다른 if 를 넣을 수 있습니다.

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("입장 가능합니다.")
    else:
        print("신분증을 지참해주세요.")
else:
    print("미성년자는 입장할 수 없습니다.")

# ============================================================
# 3. for 문 (for Loop) — 정해진 횟수만큼 반복
# ============================================================

# --- range(n): 0 부터 n-1 까지의 숫자 ---
print("\n--- range 반복 ---")
for i in range(5):         # 0, 1, 2, 3, 4
    print(i, end=" ")
print()

for i in range(2, 6):      # range(시작, 끝) — 끝은 미포함
    print(i, end=" ")      # 2, 3, 4, 5
print()

# --- 컬렉션 순회 (iteration) ---
print("\n--- 리스트 순회 ---")
fruits = ["사과", "바나나", "오렌지"]
for fruit in fruits:
    print(f"과일: {fruit}")

# --- enumerate(): 인덱스(index)와 값(value)을 동시에 ---
print("\n--- enumerate ---")
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# --- 딕셔너리 순회 — items() 로 키와 값을 함께 ---
print("\n--- 딕셔너리 순회 ---")
scores = {"국어": 90, "영어": 85, "수학": 95}
for subject, score in scores.items():
    print(f"{subject}: {score}점")

# --- 중첩 for 문 (구구단 2~3단) ---
print("\n--- 구구단 2~3단 ---")
for dan in range(2, 4):
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i:2d}", end="  ")
    print()

# ============================================================
# 4. while 문 (while Loop) — 조건이 True인 동안 반복
# ============================================================

print("\n--- 카운트다운 ---")
count = 5
while count > 0:
    print(count, end=" ")
    count -= 1   # 매 반복마다 1씩 줄임. 안 줄이면 무한 루프(infinite loop)!
print("발사!")

# ============================================================
# 5. 루프 제어 (Loop Control) — break / continue
# ============================================================

# break: 반복을 즉시 종료(escape)
print("\n--- break 예제 ---")
for i in range(10):
    if i == 5:
        break               # i가 5가 되면 종료
    print(i, end=" ")       # 0 1 2 3 4
print()

# continue: 이번 반복만 건너뛰고(skip) 다음으로
print("--- continue 예제 ---")
for i in range(10):
    if i % 2 == 0:
        continue            # 짝수면 건너뛰기
    print(i, end=" ")       # 1 3 5 7 9
print()

# ============================================================
# 종합 예제 (Run Examples)
# ============================================================
if __name__ == "__main__":
    print("\n=== 별 찍기 (삼각형) ===")
    for i in range(1, 6):
        print("*" * i)
