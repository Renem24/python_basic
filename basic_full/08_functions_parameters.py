"""
08. 함수 매개변수 (Functions - Parameters)

이 파일에서 다루는 내용:
- 매개 변수 (Parameters)
- 키워드 인자 (Keyword Arguments)
- 디폴트 값 (Default Values)
- *args, **kwargs
- 람다 함수 (Lambda)

참고: Real Python Pocket Reference
"""

# ============================================================
# 1. 매개 변수 (Parameters)
# ============================================================

# 매개변수(parameter): 함수 정의 시 선언하는 변수
# 인자(argument): 함수 호출 시 전달하는 값

def introduce(name, age):
    """위치 매개변수: 순서대로 전달"""
    return f"{name}은(는) {age}살입니다."

# 위치 인자로 호출 (순서 중요!)
print(introduce("Alice", 25))   # "Alice은(는) 25살입니다."
print(introduce("Bob", 30))     # "Bob은(는) 30살입니다."

# ============================================================
# 2. 키워드 인자 (Keyword Arguments)
# ============================================================

# 키워드 인자: 매개변수 이름을 명시하여 전달 (순서 무관)
print(introduce(name="Alice", age=25))  # 순서대로
print(introduce(age=25, name="Alice"))  # 순서 바꿔도 OK

# 위치 인자와 키워드 인자 혼합 (위치 인자가 먼저!)
print(introduce("Alice", age=25))       # OK
# print(introduce(name="Alice", 25))    # SyntaxError! 키워드 뒤에 위치 인자 불가

# ============================================================
# 3. 디폴트 값 (Default Values)
# ============================================================

def greet(name, greeting="안녕하세요"):
    """greeting에 디폴트 값이 지정되어 있음"""
    return f"{greeting}, {name}님!"

print(greet("철수"))                    # "안녕하세요, 철수님!"
print(greet("영희", "반갑습니다"))       # "반갑습니다, 영희님!"
print(greet("민수", greeting="환영합니다"))  # "환영합니다, 민수님!"

def add(x, y=10):
    """y의 기본값은 10"""
    return x + y

print(add(5, 3))   # 8   (y=3으로 덮어씀)
print(add(7))       # 17  (y=10 기본값 사용)

# --- 주의: 가변 객체를 디폴트 값으로 사용하면 안 됨! ---

# 잘못된 예 (리스트가 함수 호출 간에 공유됨)
def bad_append(item, items=[]):
    items.append(item)
    return items

print(bad_append(1))   # [1]
print(bad_append(2))   # [1, 2]  ← 의도와 다름!

# 올바른 방법 (None을 기본값으로 사용)
def good_append(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(good_append(1))  # [1]
print(good_append(2))  # [2]  ← 매번 새 리스트

# ============================================================
# 4. *args와 **kwargs (가변 인자)
# ============================================================

# --- *args: 위치 인자를 튜플로 받음 ---
def total(*args):
    """임의 개수의 숫자를 합산"""
    print(f"  args = {args}")  # 튜플로 전달됨
    return sum(args)

print(total(1, 2, 3))       # args=(1,2,3) → 6
print(total(10, 20, 30, 40))  # args=(10,20,30,40) → 100

# --- **kwargs: 키워드 인자를 딕셔너리로 받음 ---
def print_info(**kwargs):
    """임의 개수의 키워드 인자를 출력"""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print_info(name="Alice", age=25, city="Seoul")

# --- *args와 **kwargs 함께 사용 ---
def flexible(x, y, *args, **kwargs):
    """고정 매개변수 + 가변 위치 + 가변 키워드"""
    print(f"  x={x}, y={y}")
    print(f"  추가 위치 인자: {args}")
    print(f"  추가 키워드 인자: {kwargs}")

flexible(1, 2, 3, 4, color="red", size=10)

# ============================================================
# 5. 매개변수 순서 규칙
# ============================================================

# 올바른 매개변수 순서:
#   def func(위치, *args, 키워드전용, **kwargs):

def example(a, b, *args, option="기본", **kwargs):
    """매개변수 순서 예시"""
    print(f"  a={a}, b={b}, args={args}, option={option}, kwargs={kwargs}")

example(1, 2)                          # a=1, b=2
example(1, 2, 3, 4)                    # args=(3, 4)
example(1, 2, option="변경")            # option="변경"
example(1, 2, 3, option="변경", x=10)   # 모두 사용

# ============================================================
# 6. 람다 함수 (Lambda Functions)
# ============================================================

# 람다: 이름 없는 한 줄 함수
# lambda 매개변수: 표현식

square = lambda x: x ** 2
print(f"5의 제곱: {square(5)}")   # 25

add = lambda x, y: x + y
print(f"3 + 4 = {add(3, 4)}")    # 7

# --- map()과 함께 사용 ---
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"제곱: {squared}")         # [1, 4, 9, 16, 25]

# --- filter()와 함께 사용 ---
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"짝수: {evens}")           # [2, 4]

# --- sorted()의 key로 사용 ---
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
by_score = sorted(students, key=lambda s: s[1])
print(f"점수순 정렬: {by_score}")
# [('Charlie', 78), ('Alice', 85), ('Bob', 92)]

by_score_desc = sorted(students, key=lambda s: s[1], reverse=True)
print(f"점수 내림차순: {by_score_desc}")
# [('Bob', 92), ('Alice', 85), ('Charlie', 78)]

# ============================================================
# 실행 (Run Examples)
# ============================================================
if __name__ == "__main__":
    print("\n=== 종합: 간단한 계산기 함수 ===")

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

    print(calculator(10, 3))                 # 13
    print(calculator(10, 3, "sub"))          # 7
    print(calculator(10, 3, operation="mul"))  # 30
    print(calculator(10, 3, operation="div"))  # 3.333...
    print(calculator(10, 0, operation="div"))  # 0으로 나눌 수 없음
