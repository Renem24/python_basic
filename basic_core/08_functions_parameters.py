"""
08. 함수 매개변수 (Functions - Parameters)

이 파일에서 다루는 것:
- 매개변수(parameter)와 인자(argument)의 차이
- 위치 인자(positional argument): 순서대로 전달
- 키워드 인자(keyword argument): 이름을 명시해서 전달
- 디폴트 값(default value): 인자를 안 줘도 되는 매개변수

용어 정리:
  매개변수(parameter): 함수를 **정의할 때** 적는 변수 이름
  인자(argument):     함수를 **호출할 때** 전달하는 실제 값

  예) def add(x, y):       ← x, y 가 매개변수
          return x + y
      add(3, 5)             ← 3, 5 가 인자
"""

# ============================================================
# 1. 매개변수와 위치 인자 (Parameters & Positional Arguments)
# ============================================================
# 위치 인자(positional argument): 정의된 순서대로 값을 전달.

def introduce(name, age):
    """이름과 나이로 자기소개 문장을 만듦"""
    return f"{name}은(는) {age}살입니다."

# 순서대로 전달 — 첫 번째가 name, 두 번째가 age
print(introduce("Alice", 25))   # "Alice은(는) 25살입니다."
print(introduce("Bob", 30))     # "Bob은(는) 30살입니다."

# 순서를 바꾸면 의미가 달라집니다!
print(introduce(25, "Alice"))   # "25은(는) Alice살입니다." ← 이상함

# ============================================================
# 2. 키워드 인자 (Keyword Arguments)
# ============================================================
# 이름(키워드)을 명시해서 전달 → 순서가 바뀌어도 OK.
# 가독성(readability)도 좋아집니다.

print(introduce(name="Alice", age=25))  # 순서대로
print(introduce(age=25, name="Alice"))  # 순서를 바꿔도 결과 동일

# 위치 인자와 키워드 인자를 섞어 쓸 수 있습니다 (위치 인자가 먼저!)
print(introduce("Alice", age=25))       # OK
# print(introduce(name="Alice", 25))    # SyntaxError! 키워드 뒤에 위치 인자는 불가

# ============================================================
# 3. 디폴트 값 (Default Values)
# ============================================================
# 매개변수에 기본값을 미리 정해두면, 호출 시 그 인자를 생략할 수 있습니다.
# 형태:  def 함수명(매개변수=기본값):

def greet(name, greeting="안녕하세요"):
    """greeting 의 기본값은 '안녕하세요'"""
    return f"{greeting}, {name}님!"

print(greet("철수"))                       # "안녕하세요, 철수님!"  (기본값 사용)
print(greet("영희", "반갑습니다"))         # "반갑습니다, 영희님!"  (기본값 덮어씀)
print(greet("민수", greeting="환영합니다")) # 키워드로 명시

def add(x, y=10):
    """y 의 기본값은 10"""
    return x + y

print(add(5, 3))   # 8   (y=3 으로 덮어씀)
print(add(7))      # 17  (y=10 기본값 사용)

# 주의: 디폴트 값이 있는 매개변수는 항상 뒤에 와야 합니다.
#   def func(a, b=10): ✓
#   def func(a=10, b): ✗ SyntaxError

# ============================================================
# 실행 (Run Examples)
# ============================================================
if __name__ == "__main__":
    print("\n=== 인사말 함수 (언어/격식 옵션) ===")

    def make_message(name, language="ko", formal=True):
        """
        이름과 옵션에 따라 인사말 생성.
        - language: "ko"(한국어) 또는 "en"(영어)
        - formal: True 면 격식체, False 면 친근체
        """
        if language == "ko":
            return f"{'안녕하세요' if formal else '안녕'}, {name}!"
        else:
            return f"{'Hello' if formal else 'Hi'}, {name}!"

    print(make_message("철수"))                              # 기본값 모두 사용
    print(make_message("영희", formal=False))                # 격식만 변경
    print(make_message("Alice", language="en"))              # 언어만 변경
    print(make_message("Bob", language="en", formal=False))  # 둘 다 변경
