"""
05. 연산자 (Operators) - 심화

이 파일에서 다루는 것:
- 비교 연산자 + 체이닝(chaining): 18 <= age < 65
- 동등성(==) vs 동일성(is) — 객체 정체성(identity) 개념
- 논리 연산자 + 단축 평가(short-circuit evaluation)
- 멤버십 연산자 (in, not in)
- 비트 연산자 전체 + 권한 플래그 패턴
- 연산자 우선순위(precedence) 정리

💡 basic_core/05 를 먼저 보세요.

연산자(operator): 값에 어떤 작업을 수행하는 기호.
"""

# ============================================================
# 1. 비교 연산자 + 체이닝 (Comparison + Chaining)
# ============================================================

x, y = 10, 20
print(x == y, x != y, x < y, x <= y, x > y, x >= y)

# --- 체이닝 (chained comparison) — 수학 표기처럼 작성 가능 ---
age = 25
print(18 <= age < 65)           # True (수학에서 18 ≤ age < 65 와 동일)
print(1 < 2 < 3 < 4)            # True

# 위는 다음과 동일:
print(18 <= age and age < 65)

# ⚠️ 체이닝은 짧고 명확할 때만. 길어지면 and 로 풀어쓰는 게 더 읽기 쉽습니다.

# ============================================================
# 2. 동등성 vs 동일성 (Equality vs Identity) — == vs is
# ============================================================
#
# == : 값이 같은가? (값 비교 — equality)
# is : 같은 객체인가? (메모리상 같은 위치 — identity)
#
# 모든 객체는 고유한 id 를 가집니다. is 는 그 id 를 비교합니다.

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)        # True   값이 같다
print(a is b)        # False  서로 다른 객체 (id가 다름)
print(a is c)        # True   c = a 했으니 같은 객체를 가리킴

print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")    # 다름
print(f"id(c) = {id(c)}")    # a와 같음

# --- 작은 정수와 짧은 문자열은 캐싱(caching) 됨 ---
# CPython 구현 디테일: -5~256 범위 정수와 짧은 문자열은 미리 만들어 둠.
x, y = 100, 100
print(x is y)        # True   (같은 객체 재사용)

x, y = 1000, 1000
print(x is y)        # False (보통 다른 객체)
# 그래서 값 비교에는 절대 is 를 쓰면 안 됩니다!

# --- None 비교는 is 가 관례 ---
value = None
print(value is None)         # ✓ 권장
print(value == None)         # 동작은 하지만 비권장 (PEP 8)

# 정리:
#   - 값 비교: ==
#   - None / True / False / 싱글톤(singleton) 비교: is

# ============================================================
# 3. 논리 연산자 + 단축 평가 (Short-circuit Evaluation)
# ============================================================
#
# and / or 는 결과가 확정되면 나머지를 평가하지 않습니다.
#   - and: 첫 번째가 False면 두 번째 평가 안 함 (어차피 False니까)
#   - or:  첫 번째가 True면 두 번째 평가 안 함  (어차피 True니까)

# 예시: print 함수는 호출 시 출력하는데, 단축 평가로 호출 자체가 안 됨.
result = 0 and print("이건 출력 안 됨")    # 0 (Falsy) → 뒤 평가 X
result = 1 or  print("이것도 출력 안 됨")  # 1 (Truthy) → 뒤 평가 X
print("위 두 줄은 아무것도 출력 안 됨")

# --- 활용 1: 기본값 패턴 ---
username = ""
display = username or "익명"
print(display)               # "익명"  (username이 빈 문자열=Falsy니까 뒤가 채택)

# --- 활용 2: 안전한 호출 ---
data = None
# data.upper()  # ✗ AttributeError
result = data and data.upper()   # None  (None이 Falsy라 뒤를 평가 안 함 — 안전)
print(result)

# ⚠️ 주의: and/or 의 결과는 True/False 가 아니라 평가가 멈춘 그 값입니다!
print(3 and 5)         # 5  (둘 다 Truthy, 마지막 값)
print(0 and 5)         # 0  (첫 번째가 Falsy, 그 값)
print(0 or 5)          # 5  (첫 번째가 Falsy, 두 번째가 결과)
print(3 or 5)          # 3  (첫 번째가 Truthy, 그 값)

# ============================================================
# 4. 멤버십 연산자 (Membership) — in / not in
# ============================================================

print(3 in [1, 2, 3])           # True
print("Py" in "Python")         # True
print("name" in {"name": "A"})  # True (dict 는 키에 대해 검사)
print(1 in (1, 2, 3))           # True

# ⚠️ 성능 차이:
# - list/tuple/str: O(n) — 처음부터 끝까지 훑음
# - set/dict:       O(1) — 해시로 즉시 확인 (대량 검색 시 set 권장)

# ============================================================
# 5. 비트 연산자 (Bitwise Operators) — 심화
# ============================================================
#
# 숫자를 2진수(binary)로 보고 비트 단위로 연산합니다.
#
#   &   AND   (둘 다 1 → 1)
#   |   OR    (하나라도 1 → 1)
#   ^   XOR   (서로 다르면 1)
#   ~   NOT   (반전: 0↔1, 부호도 바뀜)
#   <<  왼쪽 시프트  (×2 효과)
#   >>  오른쪽 시프트 (÷2 효과, 정수 나눗셈)

a = 0b1010   # 10
b = 0b1100   # 12

print(f"{a} & {b} = {a & b} = {bin(a & b)}")    # 8  = 0b1000
print(f"{a} | {b} = {a | b} = {bin(a | b)}")    # 14 = 0b1110
print(f"{a} ^ {b} = {a ^ b} = {bin(a ^ b)}")    # 6  = 0b0110
print(f"~{a} = {~a}")                            # -11 (2의 보수)
print(f"{a} << 1 = {a << 1}")                    # 20 (×2)
print(f"{a} >> 1 = {a >> 1}")                    # 5  (÷2)

# --- 실전 패턴: 권한 플래그 (permission flags) ---
# 파일 시스템(예: chmod)에서 흔히 쓰는 패턴.
READ    = 0b100   # 4
WRITE   = 0b010   # 2
EXECUTE = 0b001   # 1

# 권한 부여(grant): OR 로 합치기
permission = READ | WRITE          # 4 | 2 = 6  (읽기 + 쓰기)
print(f"권한: {bin(permission)}")  # 0b110

# 권한 확인(check): AND 로 마스킹(masking)
can_read    = bool(permission & READ)     # True
can_execute = bool(permission & EXECUTE)  # False
print(f"읽기: {can_read}, 실행: {can_execute}")

# 권한 추가/제거
permission |= EXECUTE      # 실행 권한 추가
permission &= ~WRITE       # 쓰기 권한 제거 (마스크 반전 후 AND)
print(f"수정 후: {bin(permission)}")

# 💡 비트 연산은 입문 단계에선 자주 안 씁니다.
#    네트워크 프로토콜, 임베디드, 그래픽스, 압축 등에서 등장.

# ============================================================
# 6. 연산자 우선순위 (Operator Precedence)
# ============================================================
#
# 우선순위 (높은 것 → 낮은 것):
#   1. **                       거듭제곱
#   2. +x, -x, ~x               단항 연산자
#   3. *, /, //, %              곱셈/나눗셈
#   4. +, -                     덧셈/뺄셈
#   5. <<, >>                   비트 시프트
#   6. &                        비트 AND
#   7. ^                        비트 XOR
#   8. |                        비트 OR
#   9. ==, !=, <, <=, >, >=, is, in   비교/멤버십
#  10. not
#  11. and
#  12. or
#
# 헷갈리면 괄호( )를 쓰세요. 가독성도 좋아집니다.

# 예시: 우선순위 함정
print(2 + 3 * 4)           # 14  (× 먼저)
print((2 + 3) * 4)         # 20  (괄호 먼저)

# 비트 vs 비교 함정 — 자주 실수하는 부분
# x & 1 == 1 은 (x & 1) == 1 이 아니라 x & (1 == 1) 로 평가됨!
# 비교(==)가 비트(&)보다 우선순위가 낮을 것 같지만 실제로는 더 높습니다.
x = 5
print(x & 1 == 1)          # x & (1 == 1) = x & True = 1  ← 의도와 다를 수 있음
print((x & 1) == 1)        # 명확하게 괄호 사용

# ============================================================
# 실행 (Run Examples)
# ============================================================
if __name__ == "__main__":
    print("\n=== 종합 예제: 사용자 권한 관리 ===")

    # 사용자별 권한
    users = {
        "admin": READ | WRITE | EXECUTE,
        "editor": READ | WRITE,
        "viewer": READ,
    }

    for name, perm in users.items():
        flags = []
        if perm & READ:    flags.append("R")
        if perm & WRITE:   flags.append("W")
        if perm & EXECUTE: flags.append("X")
        print(f"  {name:8s}: {''.join(flags) or '-'} ({bin(perm)})")
