"""
02. 변수와 자료형 (Variables and Data Types)

이 파일에서 다루는 내용:
- 숫자형 (int, float, complex)
- 논리형 (bool)
- 타입 확인과 변환
- 변수 할당

참고: Real Python Pocket Reference
"""

# ============================================================
# 1. 숫자형 (Numbers)
# ============================================================

# --- 정수 (int) ---
a = 10
b = -3
big = 1_000_000  # 언더스코어로 자릿수 구분 가능

# --- 실수 (float) ---
pi = 3.14
negative_float = -0.5
scientific = 2.5e3  # 2500.0 (지수 표기법)

# --- 복소수 (complex) ---
c = 3 + 4j
print(f"실수부: {c.real}, 허수부: {c.imag}")  # 3.0, 4.0

# --- 산술 연산자 ---
print(10 + 3)   # 13   덧셈
print(10 - 3)   # 7    뺄셈
print(10 * 3)   # 30   곱셈
print(10 / 3)   # 3.33 나눗셈 (항상 float 반환)
print(10 // 3)  # 3    정수 나눗셈 (몫)
print(10 % 3)   # 1    나머지
print(2 ** 3)   # 8    거듭제곱

# --- 유용한 수학 함수 ---
print(abs(-5))          # 5       절댓값
print(round(3.7))       # 4       반올림
print(round(3.14159, 2))  # 3.14  소수점 둘째 자리까지
print(min(3, 1, 2))     # 1       최솟값
print(max(3, 1, 2))     # 3       최댓값
print(sum([1, 2, 3]))   # 6       합계

# ============================================================
# 2. 논리형 (Booleans)
# ============================================================

is_active = True
is_deleted = False

# bool은 int의 하위 클래스
print(True + True)   # 2
print(False + 1)     # 1
print(isinstance(True, int))  # True

# --- Truthy / Falsy ---
# 다음 값들은 False로 평가됨 (Falsy):
#   0, 0.0, "", [], (), {}, set(), None, False
# 그 외 나머지는 True (Truthy)

print(bool(0))      # False
print(bool(42))     # True
print(bool(""))     # False
print(bool("hello"))  # True
print(bool([]))     # False
print(bool([1]))    # True
print(bool(None))   # False

# ============================================================
# 3. 타입 확인과 변환 (Type Checking & Conversion)
# ============================================================

# --- 타입 확인 ---
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("Hello"))  # <class 'str'>
print(type(True))     # <class 'bool'>
print(type(None))     # <class 'NoneType'>

# isinstance: 특정 타입인지 확인
print(isinstance(3.14, float))      # True
print(isinstance(42, (int, float)))  # True (여러 타입 동시 확인)

# issubclass: 클래스 상속 관계 확인
print(issubclass(bool, int))     # True (bool은 int의 하위 클래스)
print(issubclass(int, object))   # True (모든 클래스는 object 상속)

# --- 타입 변환 ---
print(int("42"))      # 42      문자열 → 정수
print(float("3.14"))  # 3.14    문자열 → 실수
print(str(42))        # "42"    정수 → 문자열
print(bool(1))        # True    정수 → 불리언
print(int(3.9))       # 3       실수 → 정수 (버림)
print(list("abc"))    # ['a', 'b', 'c']  문자열 → 리스트

# ============================================================
# 4. 변수 할당 (Variable Assignment)
# ============================================================

# --- 기본 할당 ---
name = "Alice"   # 문자열
age = 25         # 정수
height = 5.6     # 실수
is_student = True  # 불리언
nothing = None   # None 타입

# --- 병렬 할당 (Parallel Assignment) ---
x, y = 10, 20       # 동시에 여러 변수에 값 할당
print(f"x={x}, y={y}")  # x=10, y=20

# 값 교환 (swap)
x, y = y, x
print(f"교환 후: x={x}, y={y}")  # x=20, y=10

# --- 체이닝 할당 (Chained Assignment) ---
a = b = c = 0  # 여러 변수에 같은 값 할당
print(f"a={a}, b={b}, c={c}")  # 모두 0

# --- 복합 할당 연산자 (Augmented Assignment) ---
counter = 0
counter += 1   # counter = counter + 1
counter -= 1   # counter = counter - 1
counter *= 3   # counter = counter * 3
counter //= 2  # counter = counter // 2

score = 100
score += 50
print(f"점수: {score}")  # 150

# ============================================================
# 실행 (Run Examples)
# ============================================================
if __name__ == "__main__":
    print("\n=== 숫자형 타입 확인 ===")
    print(f"10의 타입: {type(10)}")
    print(f"3.14의 타입: {type(3.14)}")
    print(f"3+4j의 타입: {type(3+4j)}")

    print("\n=== 변수 할당 예제 ===")
    first, *rest = [1, 2, 3, 4, 5]
    print(f"first={first}, rest={rest}")  # first=1, rest=[2, 3, 4, 5]
