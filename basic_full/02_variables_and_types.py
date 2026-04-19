"""
02. 변수와 자료형 (Variables and Data Types) - 심화

이 파일에서 다루는 것:
- 변수 이름 규칙 (naming rules) — PEP 8 컨벤션
- 숫자형 심화: 정수(int), 실수(float), 복소수(complex)
- 숫자 리터럴 표현 (1_000_000, 0xFF, 0b1010, 2.5e3)
- 부동소수점(floating-point) 정밀도 함정
- 논리형(bool)은 사실 int의 서브클래스
- Truthy / Falsy 전체 목록
- 타입 확인의 두 방법: type() vs isinstance()
- 클래스 상속 관계: issubclass()
- 변수 할당 심화: 병렬 / 체인 / 확장 언패킹

💡 basic_core/02 를 먼저 보세요.
"""

# ============================================================
# 0. 변수 이름 규칙 (Variable Naming Rules)
# ============================================================
#
# 규칙 (Rules — 어기면 SyntaxError):
#   ✓ 영문자/숫자/언더스코어(_) 사용 가능
#   ✓ 첫 글자는 영문자 또는 _ (숫자 X)
#   ✓ 대소문자 구분 (age 와 Age 는 다른 변수)
#   ✗ 예약어(keyword) 사용 불가: if, for, def, class, return ...
#
# 컨벤션 (Convention — PEP 8):
#   - 변수/함수: snake_case        예: user_name, total_count
#   - 상수:     UPPER_SNAKE_CASE  예: MAX_SIZE, PI
#   - 클래스:   PascalCase         예: UserProfile

user_age = 25      # ✓ 좋음
user2 = "Bob"      # ✓ 가능
# 2user = "Bob"    # ✗ SyntaxError (숫자로 시작 불가)
# class = "A"      # ✗ SyntaxError (예약어)

# ============================================================
# 1. 숫자형 심화 (Numbers - In Depth)
# ============================================================

# --- 정수 (int) ---
a = 10
b = -3
big = 1_000_000     # 언더스코어로 자릿수 구분 (Python 3.6+, 가독성용)
hex_num = 0xFF      # 16진수(hexadecimal) = 255
oct_num = 0o17      # 8진수(octal)        = 15
bin_num = 0b1010    # 2진수(binary)       = 10

print(f"big = {big}")       # 1000000  (출력 시 _ 사라짐)
print(f"0xFF = {hex_num}")  # 255

# --- 실수 (float) ---
pi = 3.14
scientific = 2.5e3   # 지수 표기 = 2500.0  (e3 = ×10³)
tiny = 1.5e-4        # = 0.00015

# ⚠️ 부동소수점(floating-point) 정밀도 주의
print(0.1 + 0.2)     # 0.30000000000000004 (정확히 0.3이 아님!)
# 이유: 컴퓨터는 0.1을 2진수로 정확히 표현하지 못합니다.
# 금융 계산처럼 정확도가 필요하면 decimal 모듈을 사용하세요.
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))   # 0.3 (정확!)

# --- 복소수 (complex) ---
# 수학의 a + bi 형태. 파이썬은 i 대신 j 를 허수 단위로 사용합니다.
c = 3 + 4j
print(f"실수부(real): {c.real}, 허수부(imag): {c.imag}")  # 3.0, 4.0
print(f"절댓값(magnitude): {abs(c)}")                       # 5.0
# 활용: 신호처리, 전자공학, 물리 시뮬레이션 등.
# 일반 프로그래밍에서는 거의 쓰지 않습니다.

# --- 정수 나눗셈의 동작 차이 ---
print(10 // 3)    # 3   (몫만)
print(-10 // 3)   # -4  (작은 정수 쪽으로 내림 — floor division)
print(int(3.9))   # 3   (truncation: 0 방향으로 잘라냄)
print(int(-3.9))  # -3  (역시 0 방향)

# 정리:
#   //     = floor division (수직선상 작은 쪽으로)
#   int()  = truncation     (0 방향으로)
#   round()= 반올림 (단, 5는 짝수 쪽으로 — banker's rounding)
print(round(0.5))   # 0  (예상은 1이지만, 짝수 쪽인 0)
print(round(1.5))   # 2

# ============================================================
# 2. 논리형 (Booleans) — 심화
# ============================================================

# bool 은 사실 int 의 서브클래스(subclass)입니다.
print(True + True)              # 2   (True=1, False=0)
print(True * 5)                 # 5
print(isinstance(True, int))    # True

# --- Falsy 값 전체 목록 ---
# if 문에서 False 로 평가되는 값들:
#   False, None
#   0, 0.0, 0j           # 모든 0
#   "", [], (), {}, set()  # 빈 컬렉션/문자열
#   range(0)             # 빈 range
# 그 외는 모두 Truthy.

# 활용: 빈 컨테이너 검사
items = []
if items:
    print("아이템 있음")
else:
    print("아이템 없음")   # ← 이쪽. len(items) == 0 보다 짧고 파이썬다움.

# ============================================================
# 3. 타입 확인 (Type Checking) — type() vs isinstance()
# ============================================================

# --- type(): 정확한 타입 비교 ---
print(type(42) == int)          # True
print(type(True) == int)        # False  (bool 은 별도 타입)

# --- isinstance(): 상속 관계까지 고려 (권장) ---
print(isinstance(True, int))    # True   (bool 은 int 의 서브클래스)
print(isinstance(3.14, float))  # True

# 여러 타입 중 하나인지 확인 (튜플 전달)
def is_number(x):
    """x 가 int 또는 float 인지 검사"""
    return isinstance(x, (int, float))

print(is_number(10))      # True
print(is_number(3.14))    # True
print(is_number("10"))    # False

# 권장: 일반적으로 isinstance() 사용. type() 은 정확한 타입이 필요할 때만.

# --- issubclass(): 클래스 간 상속 관계 ---
print(issubclass(bool, int))    # True
print(issubclass(int, object))  # True  (모든 클래스는 object 상속)
print(issubclass(int, float))   # False

# ============================================================
# 4. 변수 할당 심화 (Variable Assignment - Advanced)
# ============================================================

# --- 병렬 할당 (parallel assignment) — basic_core 복습 ---
x, y = 10, 20
x, y = y, x         # swap 한 줄!
print(f"x={x}, y={y}")

# --- 체인 할당 (chained assignment) ---
a = b = c = 0       # 셋 다 0
print(f"a={a}, b={b}, c={c}")

# ⚠️ 주의: 가변 객체(mutable object)는 같은 객체를 공유함!
list1 = list2 = []
list1.append(1)
print(list2)        # [1] ← list2도 같이 바뀜! (둘이 같은 리스트)

# 안전한 방법: 따로 만들기
list1, list2 = [], []
list1.append(1)
print(list1, list2)  # [1] []

# --- 확장 언패킹 (extended unpacking, Python 3+) ---
# *변수: 나머지를 리스트로 모아 받음.
first, *rest = [1, 2, 3, 4, 5]
print(f"first={first}, rest={rest}")    # 1, [2, 3, 4, 5]

*head, last = [1, 2, 3, 4, 5]
print(f"head={head}, last={last}")      # [1, 2, 3, 4], 5

first, *middle, last = [1, 2, 3, 4, 5]
print(f"first={first}, middle={middle}, last={last}")

# 활용: 첫 줄/나머지 줄 분리
text = "제목\n본문 1\n본문 2\n본문 3"
title, *body_lines = text.split("\n")
print(f"제목: {title}")
print(f"본문: {body_lines}")

# ============================================================
# 실행 (Run Examples)
# ============================================================
if __name__ == "__main__":
    print("\n=== 종합 예제: 학생 성적 처리 ===")

    # (이름, 점수1, 점수2, 점수3, ...)
    student = ("Alice", 90, 85, 95, 88, 92)

    # 확장 언패킹으로 이름과 점수 분리
    name, *scores = student
    avg = sum(scores) / len(scores)

    print(f"{name}님의 평균: {avg:.1f}")
    print(f"최고점: {max(scores)}, 최저점: {min(scores)}")

    # 타입 검증 함수 활용
    def safe_average(values):
        if not all(isinstance(v, (int, float)) for v in values):
            return None
        return sum(values) / len(values)

    print(f"안전한 평균: {safe_average(scores)}")
    print(f"잘못된 입력: {safe_average([1, 2, 'x'])}")  # None
