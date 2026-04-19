"""
03. 문자열 (Strings)

이 파일에서 다루는 내용:
- 문자열 생성
- 문자열 연산
- 문자열 메서드
- 인덱싱과 슬라이싱
- 문자열 포매팅 (f-string, format)
- raw string과 이스케이프 시퀀스

참고: Real Python Pocket Reference
"""

# ============================================================
# 1. 문자열 생성 (Creating Strings)
# ============================================================

single = 'Hello'          # 작은따옴표
double = "World"           # 큰따옴표 (권장)
multi = """여러 줄에 걸친
문자열을 작성할 수
있습니다."""               # 삼중 따옴표 (여러 줄)

# ============================================================
# 2. 문자열 연산 (String Operations)
# ============================================================

# 연결 (concatenation)
greeting = "Hello" + " " + "World"  # "Hello World"

# 반복 (repetition)
line = "-" * 30  # "------------------------------"

# 길이 (length)
length = len("Python")  # 6

# ============================================================
# 3. 문자열 메서드 (String Methods)
# ============================================================

print("hello".upper())              # "HELLO"     대문자 변환
print("HELLO".lower())              # "hello"     소문자 변환
print("  hello  ".strip())          # "hello"     양쪽 공백 제거
print("abc".replace("bc", "ha"))    # "aha"       문자열 치환
print("a b c".split())              # ['a', 'b', 'c']  공백 기준 분리
print("-".join(["a", "b", "c"]))    # "a-b-c"     구분자로 결합

# 추가 유용한 메서드
print("hello world".title())        # "Hello World"  단어 첫 글자 대문자
print("hello world".capitalize())   # "Hello world"  문장 첫 글자만 대문자
print("hello".startswith("he"))     # True
print("hello".endswith("lo"))       # True
print("hello".find("ll"))          # 2  (위치 반환, 없으면 -1)
print("hello world".count("l"))     # 3  (등장 횟수)

# ============================================================
# 4. 인덱싱과 슬라이싱 (Indexing & Slicing)
# ============================================================

text = "Python"
# 인덱스:  0  1  2  3  4  5
#         P  y  t  h  o  n
# 음수:   -6 -5 -4 -3 -2 -1

print(text[0])    # "P"     첫 번째 문자
print(text[-1])   # "n"     마지막 문자
print(text[1:4])  # "yth"   1번~3번 인덱스 (4 미포함)
print(text[:3])   # "Pyt"   처음~2번 인덱스
print(text[3:])   # "hon"   3번~끝
print(text[::2])  # "Pto"   2칸 간격
print(text[::-1]) # "nohtyP" 문자열 뒤집기

# ============================================================
# 5. 문자열 포매팅 (String Formatting)
# ============================================================

name = "Alice"
age = 25

# --- f-string (Python 3.6+, 권장) ---
print(f"이름: {name}")                # "이름: Alice"
print(f"{name}은 {age}살입니다.")     # "Alice은 25살입니다."
print(f"내년 나이: {age + 1}")        # "내년 나이: 26"
print(f"디버그: {age=}")              # "디버그: age=25"

# 서식 지정
pi = 3.14159
print(f"원주율: {pi:.2f}")           # "원주율: 3.14"   소수점 2자리
print(f"정렬: {'왼쪽':<10}|")        # 왼쪽 정렬 (폭 10)
print(f"정렬: {'오른쪽':>10}|")      # 오른쪽 정렬
print(f"정렬: {'가운데':^10}|")      # 가운데 정렬

# --- format() 메서드 ---
template = "이름: {name}, 나이: {age}"
print(template.format(name="Bob", age=30))  # "이름: Bob, 나이: 30"

# ============================================================
# 6. 이스케이프 시퀀스와 raw string
# ============================================================

# 이스케이프 시퀀스
print("탭:\t구분")           # 탭 문자
print("줄바꿈:\n다음 줄")    # 줄바꿈
print("백슬래시: \\")        # 백슬래시 출력
print("따옴표: \"안녕\"")    # 따옴표 포함

# raw string (이스케이프 무시)
print(r"C:\new\folder")     # C:\new\folder (\n이 줄바꿈 안 됨)
print("C:\\new\\folder")    # 같은 결과 (일반 문자열로 표현 시)

# ============================================================
# 실행 (Run Examples)
# ============================================================
if __name__ == "__main__":
    print("\n=== 문자열 종합 예제 ===")

    # 사용자 이메일에서 정보 추출
    email = "user@example.com"
    username, domain = email.split("@")
    print(f"사용자명: {username}")  # user
    print(f"도메인: {domain}")      # example.com

    # 문자열로 간단한 표 만들기
    print("\n--- 구구단 2단 ---")
    for i in range(1, 10):
        print(f"2 x {i} = {2 * i:2d}")
