"""
05. 연산자 (Operators)

이 파일에서 다루는 것:
- 비교 연산자(comparison operator): 두 값을 비교해서 True/False 결과
- 논리 연산자(logical operator): True/False 값들을 조합 (and / or / not)
- 멤버십 연산자(membership operator): in / not in
- 비트 연산자(bitwise operator): 참고용 (입문 단계에선 자주 쓰지 않음)

연산자(operator): 값에 어떤 작업을 시키는 기호. + 도 연산자고, == 도 연산자입니다.
"""

# ============================================================
# 1. 비교 연산자 (Comparison Operators)
# ============================================================
# 두 값을 비교해서 결과로 True 또는 False 를 돌려줍니다.

x, y = 10, 20

print(x == y)   # False   같다 (equal)
print(x != y)   # True    같지 않다 (not equal)
print(x < y)    # True    작다 (less than)
print(x <= y)   # True    작거나 같다 (less than or equal)
print(x > y)    # False   크다 (greater than)
print(x >= y)   # False   크거나 같다 (greater than or equal)

# 주의: = 와 == 는 다릅니다!
#   =  : 할당 (assignment) — 값을 넣는다
#   == : 비교 (equality)  — 같은지 묻는다

# --- None 비교는 == 가 아니라 is 를 씁니다 (관례) ---
value = None
print(value is None)      # True
print(value is not None)  # False

# ============================================================
# 2. 멤버십 연산자 (Membership Operators) — in / not in
# ============================================================
# 어떤 값이 컬렉션 안에 있는지(in) 없는지(not in) 검사합니다.

fruits = ["사과", "바나나", "오렌지"]
print("사과" in fruits)       # True   포함됨
print("포도" not in fruits)   # True   포함 안 됨
print("Py" in "Python")      # True   문자열 안에서도 검사 가능

# ============================================================
# 3. 논리 연산자 (Logical Operators) — and / or / not
# ============================================================
# True/False 값들을 조합합니다.

age = 25
has_license = True
is_weekend = False
is_holiday = True

# and: 둘 다 True여야 True
if age >= 18 and has_license:
    print("운전 가능!")

# or: 하나라도 True면 True
if is_weekend or is_holiday:
    print("오늘은 쉬는 날!")

# not: True/False 반전 (negation)
is_raining = False
if not is_raining:
    print("밖에 나갈 수 있어요.")

# ============================================================
# 4. 비트 연산자 (Bitwise Operators) — 참고용
# ============================================================
#
# 숫자를 2진수(binary)로 보고 비트 단위로 연산하는 연산자입니다.
# 입문 단계에서는 거의 쓸 일이 없으니 "이런 게 있다" 정도만 알아두세요.
#
#   &   비트 AND   (둘 다 1이면 1)
#   |   비트 OR    (하나라도 1이면 1)
#   ^   비트 XOR   (서로 다르면 1)
#   ~   비트 NOT   (반전)
#   <<  왼쪽 시프트 (× 2)
#   >>  오른쪽 시프트 (÷ 2)

a = 0b1010  # 10  (앞에 0b는 2진수 표기)
b = 0b1100  # 12

print(f"{a} & {b} = {a & b}")   # 8
print(f"{a} | {b} = {a | b}")   # 14
print(f"{a} << 1 = {a << 1}")   # 20  (왼쪽으로 1칸 = 2배)

# ============================================================
# 실행 (Run Examples)
# ============================================================
if __name__ == "__main__":
    print("\n=== 자주 쓰는 연산자 우선순위 (높은 것부터) ===")
    print("1. **                       (거듭제곱)")
    print("2. *, /, //, %              (곱셈/나눗셈)")
    print("3. +, -                     (덧셈/뺄셈)")
    print("4. ==, !=, <, <=, >, >=, in (비교)")
    print("5. not")
    print("6. and")
    print("7. or")
    print("\n괄호 ( )를 쓰면 우선순위를 명확하게 만들 수 있습니다.")
