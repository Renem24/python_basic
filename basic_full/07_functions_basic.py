"""
07. 함수 기초 (Functions - Basics) - 심화

이 파일에서 다루는 것:
- 왜 함수를 쓰는가 — DRY 원칙
- 표준 함수(built-in functions) 카테고리별 정리
- 사용자 정의 함수(user-defined functions)와 docstring
- 리턴 값과 다중 반환
- 변수의 범위 (scope): 지역(local) vs 전역(global)
- 함수도 값(first-class object)이다
- map / filter / lambda 맛보기

💡 basic_core/07 을 먼저 보세요.
"""

# ============================================================
# 0. 왜 함수를 쓰는가? (Why Functions?) — DRY 원칙
# ============================================================
#
# DRY (Don't Repeat Yourself): 같은 코드를 반복하지 마라.
#
# 함수는 다음을 가능하게 합니다:
#   - 재사용 (reuse): 한 번 만들고 여러 번 호출
#   - 추상화 (abstraction): 복잡한 동작을 이름 하나로 가림
#   - 테스트 (testing): 작은 단위로 검증
#   - 유지보수 (maintenance): 한 곳만 고치면 됨
#
# "같은 일을 두 번 이상 한다면 함수로 만들 시기"

# ============================================================
# 1. 표준 함수 / 내장 함수 (Built-in Functions) — 카테고리
# ============================================================

# --- 입출력 (I/O) ---
print("Hello!")                      # 출력
# name = input("이름: ")             # 입력 (대화형 실행 시)

# --- 타입 / 변환 (type / casting) ---
print(type(42), len("Hello"))        # 타입, 길이
print(int("42"), float("3.14"), str(100), bool(1))

# --- 수학 (math) ---
print(abs(-7), round(3.14159, 2))    # 절댓값, 반올림
print(min(3, 1, 4), max(3, 1, 4))    # 최소/최대
print(sum([1, 2, 3]), pow(2, 10))    # 합계, 거듭제곱
print(divmod(17, 5))                  # (3, 2)  몫과 나머지를 한 번에

# --- 시퀀스 / 순회 (sequence / iteration) ---
print(list(range(5)))                            # [0, 1, 2, 3, 4]
print(sorted([3, 1, 2]))                         # 정렬된 새 리스트
print(list(reversed([1, 2, 3])))                 # [3, 2, 1]
print(list(enumerate(["a", "b"])))               # [(0,'a'), (1,'b')]
print(list(zip([1, 2], ["a", "b"])))             # [(1,'a'), (2,'b')]

# --- 함수형 도구 (functional) — lambda 와 자주 쓰임 ---
nums = [1, 2, 3, 4, 5]
print(list(map(lambda x: x ** 2, nums)))         # 모든 원소에 함수 적용
print(list(filter(lambda x: x % 2 == 0, nums)))  # 조건 통과만
print(any([False, True, False]))                  # 하나라도 True?
print(all([True, True, True]))                    # 전부 True?

# --- 객체/디버깅 (object / debugging) ---
print(callable(print))   # True   호출 가능한가?
print(id(42))             # 객체의 메모리 ID
print(repr("hello"))      # "'hello'"   디버그용 표현 (따옴표 포함)
# print(dir(list))        # list 의 모든 속성/메서드 목록

# 💡 전체 목록: https://docs.python.org/3/library/functions.html
#    외울 필요 없음 — "이런 게 있다"만 알고 필요할 때 검색.

# ============================================================
# 2. 사용자 정의 함수 (User-defined Functions)
# ============================================================
# 형식:
#   def 함수이름(매개변수):
#       """docstring (설명)"""
#       실행할 코드
#       return 결과값

# --- 기본 ---
def greet():
    """인사말을 반환"""
    return "안녕하세요!"

print(greet())

# --- docstring (문서화 문자열) ---
# 함수 첫 줄에 """...""" 로 작성. help() 로 볼 수 있고 에디터 툴팁에도 표시됨.
def add(x, y):
    """
    두 수의 합을 반환합니다.

    Args:
        x: 첫 번째 수
        y: 두 번째 수
    Returns:
        x + y
    """
    return x + y

print(add(3, 5))
print(add.__doc__)        # docstring 직접 접근
# help(add)               # 도움말 표시

# ============================================================
# 3. 리턴 값 (Return Values)
# ============================================================
# return: 함수 결과를 호출한 곳으로 돌려줌. 만나면 함수 즉시 종료.

# --- 단일 값 ---
def square(n):
    return n ** 2
print(square(4))

# --- 다중 값 (실은 튜플) ---
def get_min_max(numbers):
    """최솟값과 최댓값을 한 번에 반환"""
    return min(numbers), max(numbers)

mn, mx = get_min_max([3, 1, 4, 1, 5, 9])
print(f"min={mn}, max={mx}")

# 받는 쪽에서 튜플 그대로 받기도 가능
result = get_min_max([3, 1, 4])
print(result, type(result))    # (1, 4) <class 'tuple'>

# --- 조기 반환 (early return) — 가독성 패턴 ---
def classify(age):
    if age < 0:    return "잘못된 입력"
    if age < 13:   return "어린이"
    if age < 20:   return "청소년"
    return "성인"

print(classify(15))

# --- return 없으면 None 자동 반환 ---
def say(msg):
    print(msg)

result = say("hi")
print(repr(result))    # None

# ============================================================
# 4. 변수의 범위 (Variable Scope) — Local vs Global
# ============================================================
#
# 지역(local): 함수 안에서 선언. 함수 끝나면 사라짐.
# 전역(global): 모듈(파일) 최상위에서 선언. 어디서든 읽기 가능.
#
# 검색 순서: LEGB
#   Local → Enclosing(중첩 함수) → Global → Built-in

count = 0   # 전역 변수

def increment_bad():
    count = count + 1   # ✗ UnboundLocalError!
                        #   할당이 있으면 파이썬은 count 를 지역으로 간주.
# increment_bad()

def increment_good():
    global count        # "전역 count 를 사용하겠다" 선언
    count = count + 1

increment_good()
print(count)            # 1

# 💡 global 은 가급적 피하세요. 매개변수와 리턴으로 처리하는 게 깔끔합니다.
def increment_better(n):
    return n + 1

count = increment_better(count)
print(count)

# ============================================================
# 5. 함수도 값이다 (Functions are First-Class Objects)
# ============================================================
# 파이썬에서 함수는 변수에 담고, 인자로 넘기고, 반환할 수 있는 "값"입니다.

def double(x):
    return x * 2

# 1. 변수에 담기
f = double
print(f(5))             # 10

# 2. 다른 함수의 인자로 넘기기
def apply(func, value):
    return func(value)

print(apply(double, 7))    # 14

# 3. 함수에서 함수를 반환하기
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

triple = make_multiplier(3)
print(triple(5))           # 15

# 이 개념은 람다(lambda)와 함수형 도구(map/filter)의 기반.

# ============================================================
# 6. 람다(lambda) 함수 — 짧은 익명 함수
# ============================================================
# lambda 매개변수: 표현식
# def 로 만들 정도가 아닌 짧은 함수에 사용. (자세히는 08에서)

square = lambda x: x ** 2
print(square(5))           # 25

# sorted / map / filter 의 key 인자로 자주 사용
words = ["banana", "apple", "cherry"]
print(sorted(words, key=lambda w: len(w)))    # 길이순 정렬

# ============================================================
# 실행 (Run Examples)
# ============================================================
if __name__ == "__main__":
    print("\n=== 종합: 온도 변환 ===")

    def celsius_to_fahrenheit(c):
        """섭씨 → 화씨"""
        return c * 9 / 5 + 32

    def fahrenheit_to_celsius(f):
        """화씨 → 섭씨"""
        return (f - 32) * 5 / 9

    for c in [0, 20, 37, 100]:
        f = celsius_to_fahrenheit(c)
        back = fahrenheit_to_celsius(f)
        print(f"{c}°C → {f:.1f}°F → {back:.1f}°C (왕복)")

    print("\n=== 종합: 통계 함수 ===")
    def stats(numbers):
        """리스트의 합/평균/최소/최대를 dict 로 반환"""
        if not numbers:
            return None
        return {
            "sum": sum(numbers),
            "avg": sum(numbers) / len(numbers),
            "min": min(numbers),
            "max": max(numbers),
        }

    print(stats([10, 20, 30, 40, 50]))
    print(stats([]))    # None
