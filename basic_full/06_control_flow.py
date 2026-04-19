"""
06. 프로그램 구성 - 제어문 (Control Flow) - 심화

이 파일에서 다루는 것:
- 프로그래밍 패러다임(programming paradigm) 정리
- if 심화: 조건 표현식, match-case (Python 3.10+)
- 중첩 제어문과 들여쓰기 함정
- for 심화: enumerate, zip, reversed 활용
- while 심화: while True + break / 무한 루프 방지
- 루프 제어: break / continue / pass
- for-else, while-else 절 (잘 안 쓰이지만 알아두면 좋음)
- 종합 예제: 소수 찾기

💡 basic_core/06 을 먼저 보세요.

제어문(control flow): 코드의 실행 흐름을 결정하는 문장.
파이썬은 들여쓰기(indentation)로 블록을 구분합니다 — 매우 중요!
"""

# ============================================================
# 0. 프로그래밍 패러다임 (Programming Paradigms) — 큰 그림
# ============================================================
#
# 패러다임: "코드를 어떤 식으로 조직할 것인가"의 큰 틀.
# 파이썬은 여러 패러다임을 지원합니다 (multi-paradigm).
#
# - 절차적 프로그래밍 (procedural): 위에서 아래로 명령을 순서대로 실행
#     이 파일의 주제. C, 옛날 BASIC 등이 대표적.
#
# - 객체지향 프로그래밍 (object-oriented, OOP): 데이터(속성)와 동작(메서드)을
#     클래스(class)로 묶음. Java, C# 등.
#
# - 함수형 프로그래밍 (functional): 함수를 값처럼 다루고 부수효과(side effect)를
#     줄임. Haskell, Lisp 계열. 파이썬에선 map/filter/lambda 가 그 흔적.
#
# 입문 단계는 절차적 → 함수 → 객체지향 순서가 자연스럽습니다.

# ============================================================
# 1. if 심화 (Conditional Statements)
# ============================================================

# --- 기본 (basic_core 복습) ---
age = 17
if age < 13:    category = "어린이"
elif age < 20:  category = "청소년"
else:           category = "성인"
print(category)

# --- 조건 표현식 (conditional expression / ternary) ---
score = 85
result = "합격" if score >= 60 else "불합격"
print(result)

# 중첩도 가능하지만 가독성 떨어짐 — 길어지면 if/elif 사용
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(grade)

# --- match-case (Python 3.10+) — 다중 분기 ---
# 다른 언어의 switch-case 와 유사. 단순 값 매칭부터 패턴 매칭까지 가능.
def http_status(code):
    match code:
        case 200:               return "OK"
        case 301 | 302:         return "Redirect"     # | 로 여러 값
        case 404:               return "Not Found"
        case n if n >= 500:     return "Server Error"  # 가드(guard)
        case _:                 return "Unknown"        # _ 는 와일드카드

print(http_status(200))    # OK
print(http_status(503))    # Server Error
print(http_status(999))    # Unknown

# ============================================================
# 2. 중첩 제어문과 들여쓰기 (Nested Control & Indentation)
# ============================================================

# 들여쓰기로 블록을 구분하므로 정확하게! 4칸 스페이스(권장).
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
print(f"점수 {score} → 등급 {grade}")

# ⚠️ 들여쓰기 함정: 탭과 스페이스를 섞으면 IndentationError 또는
#    TabError 가 발생합니다. 에디터에서 "탭을 스페이스로 변환" 설정 권장.

# ============================================================
# 3. for 문 심화 (For Loops)
# ============================================================

# --- range() 패턴 ---
for i in range(5):          print(i, end=" ")    # 0 1 2 3 4
print()
for i in range(2, 6):       print(i, end=" ")    # 2 3 4 5
print()
for i in range(0, 10, 2):   print(i, end=" ")    # 0 2 4 6 8
print()
for i in range(10, 0, -1):  print(i, end=" ")    # 10 9 ... 1  (역순)
print()

# --- enumerate(): 인덱스 + 값 ---
fruits = ["사과", "바나나", "오렌지"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# 시작 번호 지정
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}번 과일: {fruit}")

# --- zip(): 여러 시퀀스를 동시에 순회 ---
names = ["Alice", "Bob", "Charlie"]
ages  = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} ({age}세)")

# 길이가 다르면 짧은 쪽에 맞춤
print(list(zip([1, 2, 3], ["a", "b"])))    # [(1, 'a'), (2, 'b')]

# --- reversed(): 거꾸로 순회 ---
for fruit in reversed(fruits):
    print(fruit)

# --- 딕셔너리 순회 ---
scores = {"국어": 90, "영어": 85, "수학": 95}
for subject, score in scores.items():
    print(f"{subject}: {score}점")

# --- 중첩 for ---
print("\n--- 구구단 2~3단 ---")
for dan in range(2, 4):
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i:2d}", end="  ")
    print()

# ============================================================
# 4. while 문 심화 (While Loops)
# ============================================================

# --- 카운트다운 ---
count = 5
while count > 0:
    print(count, end=" ")
    count -= 1     # ⚠️ 안 줄이면 무한 루프(infinite loop)!
print("발사!")

# --- while True + break: 조건이 복잡할 때 ---
# (input 사용 예시 — 주석으로만)
# while True:
#     user_input = input("'quit'으로 종료: ")
#     if user_input == "quit":
#         break
#     print(f"입력: {user_input}")

# --- 무한 루프 방지 패턴 ---
attempts = 0
max_attempts = 5
while attempts < max_attempts:
    # ... 작업 ...
    attempts += 1
print(f"{attempts}번 시도 완료")

# ============================================================
# 5. 루프 제어 (Loop Control) — break / continue / pass
# ============================================================

# --- break: 즉시 종료 ---
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")    # 0 1 2 3 4
print()

# --- continue: 이번만 건너뛰기 ---
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")    # 1 3 5 7 9
print()

# --- pass: 아무것도 안 함 (자리 채우기) ---
# 문법상 블록이 비어있으면 안 될 때 사용.
for i in range(3):
    pass    # TODO: 나중에 채울 자리

if True:
    pass    # 빈 블록 표시

def not_yet_implemented():
    pass    # 함수 본문이 비어있으면 안 되니까

# --- 중첩 루프에서 break ---
# break 는 가장 가까운 루프 하나만 빠져나옵니다.
for i in range(3):
    for j in range(3):
        if j == 2:
            break       # 안쪽 for 만 종료
        print(f"({i},{j})", end=" ")
    print()

# 모든 루프를 한 번에 빠져나가려면 플래그(flag)나 함수로 감싸기.

# ============================================================
# 6. for-else / while-else (잘 안 쓰이지만 알아두기)
# ============================================================
#
# else 절은 "break 없이 정상 종료됐을 때" 실행됩니다.
# (이름이 헷갈려서 비추하는 사람도 있음)

# 검색 패턴: 찾으면 break, 못 찾으면 else
target = 7
for n in [1, 3, 5, 9, 11]:
    if n == target:
        print("찾았다!")
        break
else:
    print(f"{target} 없음")  # break 없이 끝났으니 실행됨

# ============================================================
# 7. 종합 예제 — 소수 찾기 (Prime Numbers)
# ============================================================

if __name__ == "__main__":
    print("\n=== 2~30 사이의 소수 ===")
    for num in range(2, 31):
        is_prime = True
        # √num 까지만 검사 (효율)
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
    print()

    print("\n=== 별 찍기 (피라미드) ===")
    height = 5
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

    print("\n=== FizzBuzz (1~20) ===")
    for n in range(1, 21):
        if n % 15 == 0:   print("FizzBuzz")
        elif n % 3 == 0:  print("Fizz")
        elif n % 5 == 0:  print("Buzz")
        else:             print(n)
