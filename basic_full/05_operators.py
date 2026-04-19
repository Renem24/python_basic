"""
05. 연산자 (Operators)

이 파일에서 다루는 내용:
- 비교 연산자
- 논리 연산자
- 비트 연산자

참고: Real Python Pocket Reference
"""

# ============================================================
# 1. 비교 연산자 (Comparison Operators)
# ============================================================

x, y = 10, 20

print(x == y)   # False   같다
print(x != y)   # True    같지 않다
print(x < y)    # True    작다
print(x <= y)   # True    작거나 같다
print(x > y)    # False   크다
print(x >= y)   # False   크거나 같다

# --- 체이닝 (chained comparison) ---
age = 25
print(18 <= age < 65)   # True   (18 <= age and age < 65)와 동일
print(1 < 2 < 3 < 4)    # True

# --- 동등성(==) vs 동일성(is) ---
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)    # True   값이 같다
print(a is b)    # False  서로 다른 객체
print(a is c)    # True   같은 객체를 참조

# None 비교는 is를 사용하는 것이 관례
value = None
print(value is None)      # True (권장)
print(value is not None)  # False

# --- 멤버십 연산자 (in) ---
fruits = ["사과", "바나나", "오렌지"]
print("사과" in fruits)       # True   포함됨
print("포도" not in fruits)   # True   포함 안 됨
print("Py" in "Python")      # True   문자열에서도 사용 가능

# ============================================================
# 2. 논리 연산자 (Logical Operators)
# ============================================================

age = 25
has_license = True
is_weekend = False
is_holiday = True

# and: 둘 다 True여야 True
if age >= 18 and has_license:
    print("운전 가능!")

# or: 하나만 True여도 True
if is_weekend or is_holiday:
    print("오늘은 쉬는 날!")

# not: True/False 반전
is_raining = False
if not is_raining:
    print("밖에 나갈 수 있어요.")

# --- 단축 평가 (Short-circuit evaluation) ---
# and: 첫 번째가 False면 두 번째는 평가하지 않음
# or:  첫 번째가 True면 두 번째는 평가하지 않음

result = 0 and print("이건 출력 안 됨")    # 0이 Falsy → 뒤를 평가 안 함
result = 1 or print("이것도 출력 안 됨")   # 1이 Truthy → 뒤를 평가 안 함

# 실용적 활용: 기본값 설정
username = ""
display_name = username or "익명 사용자"
print(f"표시 이름: {display_name}")  # "익명 사용자"

# ============================================================
# 3. 비트 연산자 (Bitwise Operators)
# ============================================================

a = 0b1010  # 10 (2진수)
b = 0b1100  # 12 (2진수)

# AND: 둘 다 1인 비트만 1
print(f"{a} & {b} = {a & b}")        # 8
print(f"  {bin(a)} & {bin(b)} = {bin(a & b)}")  # 0b1000

# OR: 하나라도 1이면 1
print(f"{a} | {b} = {a | b}")        # 14
print(f"  {bin(a)} | {bin(b)} = {bin(a | b)}")  # 0b1110

# XOR: 서로 다르면 1
print(f"{a} ^ {b} = {a ^ b}")        # 6
print(f"  {bin(a)} ^ {bin(b)} = {bin(a ^ b)}")  # 0b0110

# NOT: 비트 반전
print(f"~{a} = {~a}")               # -11 (2의 보수)

# 왼쪽 시프트: 비트를 왼쪽으로 이동 (× 2)
print(f"{a} << 1 = {a << 1}")        # 20
print(f"  {bin(a)} << 1 = {bin(a << 1)}")  # 0b10100

# 오른쪽 시프트: 비트를 오른쪽으로 이동 (÷ 2)
print(f"{a} >> 1 = {a >> 1}")        # 5
print(f"  {bin(a)} >> 1 = {bin(a >> 1)}")  # 0b101

# --- 비트 연산 활용 예시: 권한 플래그 ---
READ = 0b100    # 4
WRITE = 0b010   # 2
EXECUTE = 0b001 # 1

# 권한 부여 (OR)
permission = READ | WRITE     # 읽기 + 쓰기 = 6 (0b110)

# 권한 확인 (AND)
can_read = bool(permission & READ)     # True
can_execute = bool(permission & EXECUTE)  # False
print(f"읽기 권한: {can_read}, 실행 권한: {can_execute}")

# ============================================================
# 실행 (Run Examples)
# ============================================================
if __name__ == "__main__":
    print("\n=== 연산자 우선순위 (높은 것부터) ===")
    print("1. ~        (비트 NOT)")
    print("2. **       (거듭제곱)")
    print("3. *, /, //, %")
    print("4. +, -")
    print("5. <<, >>   (비트 시프트)")
    print("6. &        (비트 AND)")
    print("7. ^        (비트 XOR)")
    print("8. |        (비트 OR)")
    print("9. ==, !=, <, <=, >, >=, is, in")
    print("10. not")
    print("11. and")
    print("12. or")
