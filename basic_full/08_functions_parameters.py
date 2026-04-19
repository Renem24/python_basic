"""
08. 함수 매개변수 (Functions - Parameters) - 심화

이 파일에서 다루는 것:
- 매개변수(parameter) vs 인자(argument) 정리
- 위치 인자(positional) / 키워드 인자(keyword)
- 디폴트 값(default value)
- ⚠️ 가변 객체를 디폴트 값으로 쓰면 안 되는 함정 (mutable default trap)
- *args (가변 위치 인자), **kwargs (가변 키워드 인자)
- 매개변수 순서 규칙
- 키워드 전용(keyword-only) / 위치 전용(positional-only) 매개변수
- 람다(lambda) 함수 심화

💡 basic_core/08 을 먼저 보세요.

용어:
  매개변수(parameter): 함수를 정의할 때 적는 변수 이름
  인자(argument):     함수를 호출할 때 전달하는 실제 값
"""

# ============================================================
# 1. 위치 인자와 키워드 인자 (Positional vs Keyword)
# ============================================================

def introduce(name, age, city):
    return f"{name}({age}세, {city})"

# --- 위치 인자: 정의된 순서대로 ---
print(introduce("Alice", 25, "Seoul"))

# --- 키워드 인자: 이름 명시, 순서 무관 ---
print(introduce(name="Bob", age=30, city="Busan"))
print(introduce(city="Daegu", age=22, name="Carol"))

# --- 혼합: 위치 인자가 항상 먼저! ---
print(introduce("Dan", city="Incheon", age=40))    # OK
# print(introduce(name="Eve", 30, "Seoul"))        # ✗ SyntaxError

# 💡 키워드 인자의 장점:
#    - 가독성: introduce(name="Alice", age=25) 가 introduce("Alice", 25) 보다 명확
#    - 안전성: 인자 순서 바뀌어도 OK
#    - 일부만 바꾸기: 디폴트 값과 조합하면 매우 유용

# ============================================================
# 2. 디폴트 값 (Default Values)
# ============================================================

def greet(name, greeting="안녕하세요", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

print(greet("철수"))                              # 둘 다 디폴트
print(greet("영희", "반갑습니다"))                # greeting 변경
print(greet("민수", punctuation="."))             # 키워드로 일부만

# 규칙: 디폴트 값이 있는 매개변수는 항상 뒤에!
# def func(a=1, b): ...   # ✗ SyntaxError
# def func(a, b=1): ...   # ✓

# ============================================================
# 3. ⚠️ 가변 객체 디폴트 값의 함정 (Mutable Default Trap)
# ============================================================
#
# 디폴트 값은 **함수가 정의될 때 한 번만 평가**됩니다.
# 그래서 list/dict 같은 가변 객체를 디폴트로 쓰면 모든 호출이 같은 객체를 공유!

# --- 잘못된 예 ---
def bad_append(item, items=[]):       # ⚠️ items=[] 가 함정
    items.append(item)
    return items

print(bad_append(1))    # [1]
print(bad_append(2))    # [1, 2]   ← 의도와 다름! 같은 리스트가 누적됨
print(bad_append(3))    # [1, 2, 3]

# --- 올바른 방법: None을 디폴트로 두고 함수 안에서 새로 만들기 ---
def good_append(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(good_append(1))   # [1]
print(good_append(2))   # [2]   ← 매번 새 리스트
print(good_append(3))   # [3]

# 💡 규칙: 디폴트 값으로는 None, 숫자, 문자열, 튜플(불변) 만 사용.

# ============================================================
# 4. *args — 가변 위치 인자 (Variable Positional Arguments)
# ============================================================
#
# 임의 개수의 위치 인자를 튜플(tuple)로 받습니다.
# (이름은 args 가 아니어도 되지만 관례)

def total(*args):
    """전달된 모든 숫자의 합"""
    print(f"  args = {args}, type = {type(args).__name__}")
    return sum(args)

print(total(1, 2, 3))           # args=(1,2,3) → 6
print(total(10, 20, 30, 40))    # args=(10,20,30,40) → 100
print(total())                   # args=() → 0

# --- 활용: 평균 함수 (인자 개수 자유) ---
def average(*nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

print(average(80, 90, 100))     # 90.0
print(average(70))              # 70.0

# --- 언패킹과 *: 호출 시 리스트를 펼쳐 전달 ---
data = [1, 2, 3, 4]
print(total(*data))             # total(1, 2, 3, 4) 와 동일

# ============================================================
# 5. **kwargs — 가변 키워드 인자 (Variable Keyword Arguments)
# ============================================================
#
# 임의 개수의 키워드 인자를 딕셔너리(dict)로 받습니다.

def print_info(**kwargs):
    """전달된 모든 키워드 인자를 출력"""
    print(f"  kwargs = {kwargs}")
    for key, value in kwargs.items():
        print(f"    {key}: {value}")

print_info(name="Alice", age=25, city="Seoul")

# --- 활용: 설정 dict 만들기 ---
def make_config(**options):
    defaults = {"debug": False, "timeout": 30, "retries": 3}
    defaults.update(options)
    return defaults

print(make_config())                                # 디폴트만
print(make_config(debug=True, timeout=60))          # 일부 덮어씀

# --- 언패킹과 **: 호출 시 dict 를 키워드로 펼쳐 전달 ---
opts = {"debug": True, "retries": 5}
print(make_config(**opts))

# ============================================================
# 6. 매개변수 순서 규칙 (Parameter Order)
# ============================================================
#
# 올바른 순서:
#   def f(위치, *args, 키워드전용, **kwargs):

def example(a, b, *args, option="기본", **kwargs):
    print(f"  a={a}, b={b}, args={args}, option={option}, kwargs={kwargs}")

example(1, 2)
example(1, 2, 3, 4)                      # args=(3,4)
example(1, 2, option="변경")
example(1, 2, 3, option="X", x=10, y=20) # 모두 사용

# ============================================================
# 7. 키워드 전용 / 위치 전용 매개변수 (Python 3+)
# ============================================================

# --- 키워드 전용 (keyword-only): * 뒤의 매개변수 ---
def order(item, *, quantity=1, gift_wrap=False):
    """quantity 와 gift_wrap 은 반드시 키워드로만 전달해야 함"""
    return f"{item} x {quantity}, 포장: {gift_wrap}"

print(order("커피", quantity=2))
# print(order("커피", 2))   # ✗ TypeError (위치로는 못 전달)

# 왜 쓰나? 호출부 가독성. order("커피", 2, True) 보다 키워드가 명확.

# --- 위치 전용 (positional-only, Python 3.8+): / 앞의 매개변수 ---
def power(base, exp, /):
    """base, exp 는 키워드로 전달 불가 (위치만)"""
    return base ** exp

print(power(2, 10))
# print(power(base=2, exp=10))   # ✗ TypeError

# ============================================================
# 8. 람다 함수 심화 (Lambda Functions)
# ============================================================
# lambda 매개변수: 표현식
#
# 제약:
#   - 표현식 하나만 가능 (statement 못 씀, 즉 if 단독, for, return 불가)
#   - 한 줄짜리 짧은 함수에만 사용
#
# 언제 쓰나?
#   - sorted/map/filter 의 key 인자로 짧게 쓸 때
#   - 함수가 일회성이라 이름 붙이기 아까울 때

# --- 기본 ---
square = lambda x: x ** 2
print(square(5))            # 25

add = lambda x, y: x + y
print(add(3, 4))            # 7

# --- sorted 의 key 인자 ---
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
print(sorted(students, key=lambda s: s[1]))                  # 점수 오름차순
print(sorted(students, key=lambda s: s[1], reverse=True))    # 내림차순
print(sorted(students, key=lambda s: s[0]))                  # 이름순

# --- map / filter ---
nums = [1, 2, 3, 4, 5]
print(list(map(lambda x: x ** 2, nums)))                # 제곱
print(list(filter(lambda x: x % 2 == 0, nums)))         # 짝수만

# --- 조건 표현식 활용 ---
abs_value = lambda x: x if x >= 0 else -x
print(abs_value(-5))        # 5

# ⚠️ 람다가 길어지면 그냥 def 로 만드세요. 가독성이 우선.

# ============================================================
# 실행 (Run Examples)
# ============================================================
if __name__ == "__main__":
    print("\n=== 종합: 유연한 계산기 ===")

    def calculator(x, y, operation="add"):
        """사칙연산 계산기"""
        ops = {
            "add": lambda a, b: a + b,
            "sub": lambda a, b: a - b,
            "mul": lambda a, b: a * b,
            "div": lambda a, b: a / b if b != 0 else "0으로 나눌 수 없음",
        }
        func = ops.get(operation)
        if func is None:
            return f"지원하지 않는 연산: {operation}"
        return func(x, y)

    print(calculator(10, 3))                       # 13
    print(calculator(10, 3, "sub"))                # 7
    print(calculator(10, 3, operation="mul"))      # 30
    print(calculator(10, 0, operation="div"))      # 0으로 나눌 수 없음

    print("\n=== 종합: 학생 데이터 처리 ===")
    students = [
        {"name": "Alice", "score": 85},
        {"name": "Bob",   "score": 92},
        {"name": "Carol", "score": 78},
        {"name": "Dan",   "score": 95},
    ]

    # 점수순 정렬
    by_score = sorted(students, key=lambda s: s["score"], reverse=True)
    print("점수순:")
    for s in by_score:
        print(f"  {s['name']}: {s['score']}")

    # 80점 이상만 (filter)
    passed = list(filter(lambda s: s["score"] >= 80, students))
    print(f"\n80점 이상: {len(passed)}명")

    # 이름만 추출 (map)
    names = list(map(lambda s: s["name"], students))
    print(f"전체 이름: {names}")
