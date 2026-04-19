"""
03. 문자열 (Strings) - 심화

이 파일에서 다루는 것:
- 문자열은 불변(immutable)이라는 사실
- 다양한 문자열 메서드 (대소문자, 검사, 검색, 정렬)
- 인덱싱/슬라이싱 심화 (스텝, 역순)
- f-string 포맷 사양(format spec): 정렬, 폭, 패딩, 디버그
- format() 메서드 (구버전 호환용)
- 이스케이프 시퀀스 정리
- raw string (r"...") — 경로/정규식에 유용

💡 basic_core/03 을 먼저 보세요.
"""

# ============================================================
# 0. 문자열은 불변 (Strings are Immutable)
# ============================================================
#
# 한번 만들어진 문자열은 수정할 수 없습니다(immutable).
# 메서드는 "원본을 바꾸는" 게 아니라 "새 문자열을 반환"합니다.

s = "hello"
# s[0] = "H"        # ✗ TypeError! 수정 불가
upper = s.upper()   # ✓ 새 문자열을 만들어 반환
print(s)            # "hello" (원본은 그대로)
print(upper)        # "HELLO"

# 만약 정말 바꾸고 싶다면 새 변수에 재할당:
s = s.upper()
print(s)            # "HELLO"

# ============================================================
# 1. 문자열 만들기 (Creating Strings) — 복습 + 추가
# ============================================================

single = 'Hello'
double = "World"
multi = """여러 줄
문자열"""

# 따옴표 안에 같은 따옴표를 쓰려면?
mixed1 = "She said 'Hi'"        # 큰따옴표 안의 작은따옴표
mixed2 = 'He said "Hi"'         # 작은따옴표 안의 큰따옴표
mixed3 = "She said \"Hi\""      # 이스케이프

# ============================================================
# 2. 문자열 메서드 — 카테고리별 정리
# ============================================================

# --- 대소문자 변환 ---
print("hello".upper())          # "HELLO"
print("HELLO".lower())          # "hello"
print("hello world".title())    # "Hello World"      각 단어 첫 글자
print("hello world".capitalize())  # "Hello world"   문장 첫 글자만
print("HeLLo".swapcase())       # "hEllO"            대↔소

# --- 공백/문자 제거 ---
print("  hello  ".strip())      # "hello"   양쪽 제거
print("  hello  ".lstrip())     # "hello  " 왼쪽만 (left)
print("  hello  ".rstrip())     # "  hello" 오른쪽만 (right)
print("###hi###".strip("#"))    # "hi"      특정 문자 제거

# --- 검색 / 검사 ---
print("hello".startswith("he"))     # True
print("hello".endswith("lo"))       # True
print("hello world".find("world"))  # 6   (위치, 없으면 -1)
print("hello world".index("world")) # 6   (없으면 ValueError)
print("hello world".count("l"))     # 3
print("hello" in "say hello")       # True (간단한 포함 검사는 in 으로)

# --- 분리 / 결합 ---
print("a b c".split())              # ['a', 'b', 'c']
print("a,b,c".split(","))           # ['a', 'b', 'c']
print("line1\nline2".splitlines())  # ['line1', 'line2']
print("-".join(["a", "b", "c"]))    # "a-b-c"

# --- 치환 ---
print("hello".replace("l", "L"))         # "heLLo"   모두 치환
print("hello".replace("l", "L", 1))      # "heLlo"   1번만

# --- 검증 (모두 ~인지) ---
print("abc".isalpha())     # True   알파벳만?
print("123".isdigit())     # True   숫자만?
print("abc123".isalnum())  # True   알파벳+숫자만?
print("   ".isspace())     # True   공백만?
print("ABC".isupper())     # True

# ============================================================
# 3. 인덱싱과 슬라이싱 심화 (Indexing & Slicing - In Depth)
# ============================================================
# 슬라이싱 형태: [start:stop:step]
#   start: 시작 인덱스 (포함)
#   stop:  끝 인덱스 (미포함)
#   step:  간격 (양수=앞으로, 음수=뒤로)

text = "Python"
# 인덱스:  0  1  2  3  4  5
#         P  y  t  h  o  n
# 음수:   -6 -5 -4 -3 -2 -1

print(text[1:4])    # "yth"
print(text[::2])    # "Pto"     2칸씩 — 0,2,4 인덱스
print(text[1::2])   # "yhn"     1부터 2칸씩
print(text[::-1])   # "nohtyP"  뒤집기 (자주 쓰는 관용구)
print(text[::-2])   # "nhy"     뒤에서부터 2칸씩

# 슬라이싱은 범위를 벗어나도 에러 안 남 (인덱싱과 다름)
print(text[10:20])  # ""        빈 문자열
# print(text[10])   # IndexError!

# ============================================================
# 4. f-string 포맷 사양 (Format Spec)
# ============================================================
# 형태: f"{값:사양}"
#   사양: [채움문자][정렬][폭].[정밀도][타입]

name = "Alice"
age = 25
pi = 3.14159

# --- 기본 ---
print(f"이름: {name}, 나이: {age}")

# --- 디버그 출력 (Python 3.8+): 변수명까지 자동 표시 ---
print(f"{age=}")            # "age=25"
print(f"{pi=:.2f}")         # "pi=3.14"

# --- 정밀도 (소수점) ---
print(f"{pi:.2f}")          # "3.14"        소수점 2자리
print(f"{pi:.4f}")          # "3.1416"
print(f"{1234567:,}")       # "1,234,567"   천 단위 콤마

# --- 폭과 정렬 ---
print(f"|{'왼쪽':<10}|")      # |왼쪽        |   < 왼쪽 정렬, 폭 10
print(f"|{'오른쪽':>10}|")    # |       오른쪽|   > 오른쪽
print(f"|{'가운데':^10}|")    # |   가운데   |   ^ 가운데
print(f"|{42:0>5}|")        # |00042|         0으로 채움
print(f"|{42:*^10}|")       # |****42****|    *로 채움

# --- 진법 변환 ---
print(f"{255:b}")    # "11111111"  2진수
print(f"{255:o}")    # "377"       8진수
print(f"{255:x}")    # "ff"        16진수
print(f"{255:X}")    # "FF"        16진수 대문자

# --- 퍼센트 ---
print(f"{0.85:.1%}")   # "85.0%"

# ============================================================
# 5. format() 메서드 (구버전 호환용)
# ============================================================
# f-string 이전(Python 3.6 미만)에 쓰던 방식. 가끔 마주칩니다.

print("이름: {}, 나이: {}".format("Bob", 30))           # 위치
print("이름: {0}, 나이: {1}, 다시: {0}".format("Bob", 30))  # 인덱스
print("이름: {name}, 나이: {age}".format(name="Bob", age=30))  # 키워드

# ============================================================
# 6. 이스케이프 시퀀스 (Escape Sequences) 정리
# ============================================================
#
#   \n   줄바꿈 (newline)
#   \t   탭 (tab)
#   \\   백슬래시 자체
#   \"   큰따옴표
#   \'   작은따옴표
#   \r   캐리지 리턴 (Windows 줄바꿈에 사용)
#   \0   널 문자

print("탭:\t구분")
print("줄바꿈:\n다음 줄")
print("백슬래시: \\")
print("따옴표: \"안녕\"")

# ============================================================
# 7. Raw String (r"...") — 경로/정규식에 유용
# ============================================================
# r"" 로 감싸면 백슬래시(\)를 그대로 문자로 취급. 이스케이프 무시.

print("C:\new\test")          # "C:\new\test" 인데 \n, \t가 적용됨!
print(r"C:\new\test")         # "C:\new\test" 그대로
print("C:\\new\\test")        # 같은 결과 (이스케이프 두 번)

# 정규식(regular expression)에서 raw string이 거의 필수:
import re
pattern = r"\d+"              # 숫자 1개 이상
print(re.findall(pattern, "abc 123 def 456"))   # ['123', '456']

# ============================================================
# 실행 (Run Examples)
# ============================================================
if __name__ == "__main__":
    print("\n=== 종합 예제: 영수증 출력 ===")
    items = [("사과", 1500, 3), ("우유", 3200, 2), ("빵", 2800, 1)]

    print(f"{'상품':<8}{'단가':>8}{'수량':>5}{'합계':>10}")
    print("-" * 31)
    total = 0
    for name, price, qty in items:
        subtotal = price * qty
        total += subtotal
        print(f"{name:<8}{price:>8,}{qty:>5}{subtotal:>10,}")
    print("-" * 31)
    print(f"{'TOTAL':<8}{'':>13}{total:>10,}원")
