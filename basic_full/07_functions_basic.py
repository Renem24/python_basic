"""
07. 함수 기초 (Functions - Basics)

이 파일에서 다루는 내용:
- 표준 함수 (내장 함수)
- 사용자 정의 함수
- 리턴 값

참고: Real Python Pocket Reference
"""

# ============================================================
# 1. 표준 함수 / 내장 함수 (Built-in Functions)
# ============================================================

# --- 입출력 ---
print("Hello, Python!")              # 출력
# name = input("이름을 입력하세요: ")  # 입력 (대화형 실행 시)

# --- 타입/변환 ---
print(type(42))          # <class 'int'>   타입 확인
print(len("Hello"))      # 5               길이
print(int("42"))         # 42              정수 변환
print(float("3.14"))     # 3.14            실수 변환
print(str(100))          # "100"           문자열 변환

# --- 수학 ---
print(abs(-7))           # 7               절댓값
print(round(3.14159, 2)) # 3.14            반올림
print(min(3, 1, 4))      # 1               최솟값
print(max(3, 1, 4))      # 4               최댓값
print(sum([1, 2, 3]))    # 6               합계
print(pow(2, 10))        # 1024            거듭제곱

# --- 반복/순회 ---
print(list(range(5)))                # [0, 1, 2, 3, 4]
print(sorted([3, 1, 2]))            # [1, 2, 3]     정렬
print(list(reversed([1, 2, 3])))    # [3, 2, 1]     역순
print(list(enumerate(["a", "b"])))  # [(0, 'a'), (1, 'b')]
print(list(zip([1, 2], ["a", "b"])))  # [(1, 'a'), (2, 'b')]

# --- map / filter ---
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"map 결과: {squared}")         # [1, 4, 9, 16, 25]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"filter 결과: {evens}")        # [2, 4]

# --- 유틸리티 함수 ---
print(callable(print))  # True   호출 가능한 객체인지 확인
print(id(42))           # 객체의 고유 식별자
print(repr("hello"))    # "'hello'"  디버그용 문자열 표현
# dir(list)             # list의 모든 속성과 메서드 목록

# ============================================================
# 2. 사용자 정의 함수 (User-defined Functions)
# ============================================================

# --- 기본 함수 정의 ---
def greet():
    """인사말을 반환하는 함수"""
    return "안녕하세요!"

print(greet())  # "안녕하세요!"

# --- 매개변수가 있는 함수 ---
def greet_person(name):
    """이름을 받아 인사말을 반환"""
    return f"안녕하세요, {name}님!"

print(greet_person("철수"))  # "안녕하세요, 철수님!"

# --- 여러 매개변수 ---
def add(x, y):
    """두 수의 합을 반환"""
    return x + y

print(add(3, 5))  # 8

# ============================================================
# 3. 리턴 값 (Return Values)
# ============================================================

# --- 하나의 값을 반환 ---
def square(n):
    return n ** 2

result = square(4)
print(f"4의 제곱: {result}")  # 16

# --- 여러 값을 반환 (튜플) ---
def get_min_max(numbers):
    """리스트에서 최솟값과 최댓값을 반환"""
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([3, 1, 4, 1, 5, 9])
print(f"최솟값: {minimum}, 최댓값: {maximum}")  # 1, 9

# --- 조건에 따른 반환 ---
def classify_age(age):
    """나이에 따른 분류를 반환"""
    if age < 13:
        return "어린이"
    elif age < 20:
        return "청소년"
    else:
        return "성인"

print(classify_age(15))  # "청소년"

# --- None 반환 (명시적 return이 없는 경우) ---
def say_hello(name):
    print(f"Hello, {name}!")
    # return 문이 없으면 None을 반환

result = say_hello("Python")  # "Hello, Python!" 출력
print(f"반환값: {result}")     # None

# ============================================================
# 실행 (Run Examples)
# ============================================================
if __name__ == "__main__":
    print("\n=== 함수 활용 종합 예제 ===")

    # 온도 변환 함수
    def celsius_to_fahrenheit(celsius):
        """섭씨를 화씨로 변환"""
        return celsius * 9 / 5 + 32

    def fahrenheit_to_celsius(fahrenheit):
        """화씨를 섭씨로 변환"""
        return (fahrenheit - 32) * 5 / 9

    temps_c = [0, 20, 37, 100]
    print("섭씨 → 화씨 변환:")
    for c in temps_c:
        f = celsius_to_fahrenheit(c)
        print(f"  {c}°C = {f:.1f}°F")
