"""
06. 프로그램 구성 - 제어문 (Control Flow)

이 파일에서 다루는 내용:
- 프로그래밍 패러다임 개요
- if 문 (조건문)
- 중첩 제어문
- for 문 (반복문)
- while 문 (반복문)

참고: Real Python Pocket Reference

프로그래밍 패러다임 (Programming Paradigms):
  파이썬은 여러 패러다임을 지원하는 멀티 패러다임 언어입니다.
  - 절차적(Procedural): 함수와 제어문으로 순서대로 실행
  - 객체지향(OOP): 클래스와 객체로 데이터와 동작을 묶어서 구성
  - 함수형(Functional): 함수를 값처럼 전달 (map, filter, lambda 등)
  이 파일에서는 절차적 프로그래밍의 핵심인 제어문을 다룹니다.
"""

# ============================================================
# 1. if 문 (Conditional Statements)
# ============================================================

# --- 기본 if / elif / else ---
age = 17

if age < 13:
    category = "어린이"
elif age < 20:
    category = "청소년"
else:
    category = "성인"

print(f"나이 {age}세 → {category}")  # 청소년

# --- 조건 표현식 (삼항 연산자) ---
score = 85
result = "합격" if score >= 60 else "불합격"
print(f"점수 {score} → {result}")  # 합격

# ============================================================
# 2. 중첩 제어문 (Nested Control Statements)
# ============================================================

# if 안에 if
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("입장 가능합니다.")
    else:
        print("신분증을 지참해주세요.")
else:
    print("미성년자는 입장할 수 없습니다.")

# 성적 등급 판별 (중첩 조건)
score = 78

if score >= 90:
    if score >= 95:
        grade = "A+"
    else:
        grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"점수 {score} → 등급 {grade}")  # C

# ============================================================
# 3. for 문 (For Loops)
# ============================================================

# --- range() 사용 ---
print("\n--- range 반복 ---")
for i in range(5):         # 0, 1, 2, 3, 4
    print(i, end=" ")
print()

for i in range(2, 6):      # 2, 3, 4, 5 (시작, 끝)
    print(i, end=" ")
print()

for i in range(0, 10, 3):  # 0, 3, 6, 9 (시작, 끝, 간격)
    print(i, end=" ")
print()

# --- 컬렉션 순회 ---
print("\n--- 컬렉션 순회 ---")
fruits = ["사과", "바나나", "오렌지"]
for fruit in fruits:
    print(f"과일: {fruit}")

# --- enumerate() 사용: 인덱스와 값을 동시에 ---
print("\n--- enumerate ---")
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# --- 딕셔너리 순회 ---
print("\n--- 딕셔너리 순회 ---")
scores = {"국어": 90, "영어": 85, "수학": 95}
for subject, score in scores.items():
    print(f"{subject}: {score}점")

# --- 중첩 for 문 ---
print("\n--- 구구단 (2~3단) ---")
for dan in range(2, 4):
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i:2d}", end="  ")
    print()  # 단이 바뀔 때 줄바꿈

# ============================================================
# 4. while 문 (While Loops)
# ============================================================

# --- 기본 while ---
print("\n--- 카운트다운 ---")
count = 5
while count > 0:
    print(count, end=" ")
    count -= 1
print("발사!")

# --- while True + break ---
# (input 사용 시 실제 대화형 실행 필요)
# while True:
#     user_input = input("'quit' 입력 시 종료: ")
#     if user_input == "quit":
#         break
#     print(f"입력: {user_input}")

# ============================================================
# 5. 루프 제어 (Loop Control)
# ============================================================

# --- break: 루프 즉시 종료 ---
print("\n--- break 예제 ---")
for i in range(10):
    if i == 5:
        break           # i가 5이면 종료
    print(i, end=" ")   # 0 1 2 3 4
print()

# --- continue: 현재 반복 건너뛰기 ---
print("--- continue 예제 ---")
for i in range(10):
    if i % 2 == 0:
        continue        # 짝수면 건너뛰기
    print(i, end=" ")   # 1 3 5 7 9
print()

# --- break + continue 조합 ---
print("--- break + continue ---")
for i in range(10):
    if i == 3:
        continue  # 3은 건너뛰기
    if i == 7:
        break     # 7에서 중단
    print(i, end=" ")  # 0 1 2 4 5 6
print()

# ============================================================
# 6. 중첩 제어문 종합 예제
# ============================================================

if __name__ == "__main__":
    print("\n=== 종합: 소수 찾기 (2~30) ===")
    for num in range(2, 31):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break  # 나누어지면 소수가 아님 → 내부 루프 탈출
        if is_prime:
            print(num, end=" ")
    print()

    print("\n=== 종합: 별 찍기 (삼각형) ===")
    for i in range(1, 6):
        print("*" * i)
