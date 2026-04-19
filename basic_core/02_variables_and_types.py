"""
02. 변수와 자료형 (Variables and Data Types)

이 파일에서 다루는 것:
- 변수(variable)에 값(value)을 담는 방법
- 숫자형(number): 정수(int)와 실수(float)
- 논리형(boolean): True / False
- 자료형(data type) 확인과 변환(conversion)

변수(variable): 값을 담아두는 "이름표". `name = "Alice"` 라고 쓰면
"Alice"라는 값에 name이라는 이름표를 붙입니다. 이후 name을 부르면 그 값이 나옵니다.

자료형(data type): 값의 종류. 숫자인지, 문자인지, 참/거짓인지 등.
"""

# ============================================================
# 1. 숫자형 (Number Types)
# ============================================================

# --- 정수 (int = integer) ---
a = 10
b = -3

# --- 실수 (float = floating-point number) — 소수점이 있는 수 ---
pi = 3.14
temperature = -0.5

# --- 산술 연산자 (arithmetic operators) ---
print(10 + 3)   # 13     덧셈 (addition)
print(10 - 3)   # 7      뺄셈 (subtraction)
print(10 * 3)   # 30     곱셈 (multiplication)
print(10 / 3)   # 3.33   나눗셈 (division) — 결과는 항상 float
print(10 // 3)  # 3      몫(quotient) — 정수 나눗셈
print(10 % 3)   # 1      나머지(remainder)
print(2 ** 3)   # 8      거듭제곱 (power)

# --- 자주 쓰는 수학 함수 (built-in math functions) ---
print(abs(-5))          # 5      절댓값 (absolute value)
print(round(3.7))       # 4      반올림 (round)
print(round(3.14159, 2))  # 3.14  소수점 둘째 자리까지
print(min(3, 1, 2))     # 1      최솟값 (minimum)
print(max(3, 1, 2))     # 3      최댓값 (maximum)
print(sum([1, 2, 3]))   # 6      합계 (sum)

# ============================================================
# 2. 논리형 (Boolean Type)
# ============================================================

# True(참) 또는 False(거짓), 둘 중 하나만 가집니다.
# 첫 글자가 대문자입니다 (true/false 아님!)
is_active = True
is_deleted = False

# --- 참 같은 값 / 거짓 같은 값 (Truthy / Falsy) ---
# 다음 값들은 if 문에서 False처럼 취급됩니다 (Falsy):
#   0, 0.0, "", [], None, False
# 그 외 나머지는 True처럼 취급됩니다 (Truthy).

print(bool(0))       # False
print(bool(42))      # True
print(bool(""))      # False  (빈 문자열)
print(bool("hi"))    # True
print(bool([]))      # False  (빈 리스트)

# ============================================================
# 3. 자료형 확인과 변환 (Type Checking & Conversion)
# ============================================================

# --- 타입 확인: type() ---
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("Hello"))  # <class 'str'>   문자열 (string)
print(type(True))     # <class 'bool'>

# --- 타입 변환 (type casting): 한 타입 → 다른 타입 ---
print(int("42"))      # 42     문자열 → 정수
print(float("3.14"))  # 3.14   문자열 → 실수
print(str(42))        # "42"   숫자 → 문자열
print(int(3.9))       # 3      실수 → 정수 (소수점 이하 버림)

# ============================================================
# 4. 변수 할당 (Variable Assignment)
# ============================================================

# --- 기본 할당 (=) ---
# 오른쪽 값을 왼쪽 이름에 담습니다.
name = "Alice"
age = 25
height = 5.6

# --- 한 번에 여러 변수 (parallel assignment) ---
x, y = 10, 20
print(f"x={x}, y={y}")  # x=10, y=20

# 값 교환 (swap) — 다른 언어에서는 임시 변수가 필요한 작업이 한 줄로!
x, y = y, x
print(f"교환 후: x={x}, y={y}")  # x=20, y=10

# --- 복합 할당 연산자 (augmented assignment) ---
# counter += 1 은 counter = counter + 1 의 줄임 표현입니다.
counter = 0
counter += 1   # 1이 됨
counter += 1   # 2가 됨
counter *= 3   # 6이 됨
print(f"counter: {counter}")  # 6

# ============================================================
# 실행 (Run Examples)
# ============================================================
if __name__ == "__main__":
    print("\n=== 변수와 타입 확인 ===")
    score = 85
    print(f"score 값: {score}, 타입: {type(score)}")
