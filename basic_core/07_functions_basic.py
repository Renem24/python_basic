"""
07. 함수 기초 (Functions - Basics)

이 파일에서 다루는 것:
- 함수(function)란 무엇인가
- 표준 함수(built-in function): 파이썬이 미리 만들어 둔 함수
- 사용자 정의 함수(user-defined function): 내가 직접 만드는 함수
- 리턴 값(return value): 함수가 결과를 돌려주는 방법

함수(function): 입력(input)을 받아서 처리한 뒤 결과(output)를 돌려주는
"코드 묶음". 한 번 만들어 두면 이름만으로 여러 번 재사용할 수 있습니다.
   예) 자판기: 동전(입력) → 음료(출력)
"""

# ============================================================
# 1. 표준 함수 / 내장 함수 (Built-in Functions)
# ============================================================
# 파이썬에 기본으로 포함되어 있어서 import 없이 바로 쓸 수 있는 함수들.

# --- 입출력 (input / output) ---
print("Hello, Python!")              # 화면에 출력
# name = input("이름을 입력하세요: ")  # 사용자 입력 받기 (대화형 실행 시)

# --- 타입 / 변환 (type / casting) ---
print(type(42))      # <class 'int'>   타입 확인
print(len("Hello"))  # 5               길이
print(int("42"))     # 42              문자열 → 정수
print(str(100))      # "100"           숫자 → 문자열

# --- 수학 (math) ---
print(abs(-7))           # 7      절댓값
print(round(3.14159, 2)) # 3.14   반올림
print(min(3, 1, 4))      # 1      최솟값
print(max(3, 1, 4))      # 4      최댓값
print(sum([1, 2, 3]))    # 6      합계

# --- 반복/순회 도우미 ---
print(list(range(5)))            # [0, 1, 2, 3, 4]
print(sorted([3, 1, 2]))         # [1, 2, 3]   정렬된 새 리스트
print(list(reversed([1, 2, 3]))) # [3, 2, 1]   역순

# ============================================================
# 2. 사용자 정의 함수 (User-defined Functions)
# ============================================================
# def 키워드(keyword)로 함수를 정의(define)합니다.
#
# 형태:
#   def 함수이름(매개변수):
#       실행할 코드
#       return 결과값

# --- 입력 없는 함수 ---
def greet():
    """인사말을 돌려주는 함수"""   # docstring: 함수 설명
    return "안녕하세요!"

print(greet())   # "안녕하세요!"

# --- 입력 1개를 받는 함수 ---
def greet_person(name):
    """이름을 받아 인사말을 만들어 돌려줌"""
    return f"안녕하세요, {name}님!"

print(greet_person("철수"))

# --- 입력 2개를 받는 함수 ---
def add(x, y):
    """두 수의 합을 돌려줌"""
    return x + y

print(add(3, 5))   # 8

# ============================================================
# 3. 리턴 값 (Return Values)
# ============================================================
# return: 함수가 만든 결과를 호출한 곳으로 돌려주는 명령(키워드).
# return 을 만나면 함수는 즉시 종료됩니다.

# --- 값 하나 돌려주기 ---
def square(n):
    return n ** 2

result = square(4)
print(f"4의 제곱: {result}")  # 16

# --- 값 여러 개 돌려주기 (튜플로 묶여서 반환됨) ---
def get_min_max(numbers):
    """리스트의 최솟값과 최댓값을 한 번에 돌려줌"""
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([3, 1, 4, 1, 5, 9])
print(f"최솟값: {minimum}, 최댓값: {maximum}")

# --- 조건에 따라 다른 값 돌려주기 ---
def classify_age(age):
    if age < 13:
        return "어린이"
    elif age < 20:
        return "청소년"
    else:
        return "성인"

print(classify_age(15))  # "청소년"

# --- return 이 없으면 None 이 반환됨 ---
# None: "값이 없음"을 나타내는 특수한 값
def say_hello(name):
    print(f"Hello, {name}!")
    # return 문이 없음

result = say_hello("Python")
print(f"반환값: {result}")  # None

# ============================================================
# 실행 (Run Examples)
# ============================================================
if __name__ == "__main__":
    print("\n=== 섭씨 → 화씨 변환 함수 ===")

    def celsius_to_fahrenheit(celsius):
        """섭씨(°C)를 화씨(°F)로 변환"""
        return celsius * 9 / 5 + 32

    for c in [0, 20, 37, 100]:
        f = celsius_to_fahrenheit(c)
        print(f"  {c}°C = {f:.1f}°F")
