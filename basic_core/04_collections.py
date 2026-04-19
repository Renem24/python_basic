"""
04. 컬렉션 (Collections)

이 파일에서 다루는 것:
- 여러 값을 하나로 묶는 4가지 자료구조(data structure)
- 리스트(list): 순서대로 담는 상자, 자유롭게 수정 가능
- 튜플(tuple): 리스트와 비슷하지만 한 번 만들면 수정 불가
- 딕셔너리(dictionary): 키(key)로 값(value)을 찾는 사전
- 셋(set): 중복 없는 값들의 묶음

컬렉션(collection): 여러 값을 하나의 변수에 담기 위한 자료구조.

       | 순서(order) | 변경(mutable) | 중복(duplicate) | 표기
-------+-------------+---------------+-----------------+------
list   |     O       |       O       |        O        | [...]
tuple  |     O       |       X       |        O        | (...)
dict   |     O       |       O       |   키 X / 값 O   | {k:v}
set    |     X       |       O       |        X        | {...}
"""

# ============================================================
# 1. 리스트 (List) — 가장 많이 쓰는 컬렉션
# ============================================================

# --- 만들기 ---
empty = []
nums = [1, 2, 3]
mixed = [1, "two", 3.0, True]   # 다양한 타입을 섞어도 OK

# --- 인덱싱과 슬라이싱 (문자열과 동일한 규칙) ---
fruits = ["사과", "바나나", "오렌지"]
print(fruits[0])    # "사과"     첫 번째 원소(element)
print(fruits[-1])   # "오렌지"   마지막 원소
print(fruits[0:2])  # ["사과", "바나나"]   슬라이싱

# --- 자주 쓰는 메서드 (methods) ---
fruits.append("포도")     # 끝에 추가 (append)
fruits.insert(1, "딸기")  # 1번 위치에 끼워넣기 (insert)
fruits.remove("바나나")   # 값으로 삭제 (remove)
last = fruits.pop()       # 마지막 원소 꺼내기 (pop) — 꺼내면서 반환
print(f"pop한 값: {last}")

# --- 기타 ---
print("사과" in fruits)   # True   포함 여부 (membership)
print(len(fruits))        # 원소 개수

numbers = [3, 1, 4, 1, 5]
numbers.sort()            # 정렬 — 원본을 바꿈 (in-place)
print(numbers)            # [1, 1, 3, 4, 5]
print(sorted([3, 1, 2]))  # [1, 2, 3] — 원본 유지, 새 리스트 반환

# ============================================================
# 2. 튜플 (Tuple) — 수정 불가능한 리스트
# ============================================================

# 좌표, 날짜처럼 "한번 정해지면 안 바뀌는" 값을 담을 때 씁니다.
point = (3, 4)
single = (1,)   # 원소 1개일 땐 쉼표 필수! (1) 은 그냥 숫자가 됨

# 언패킹 (unpacking) — 튜플의 값을 변수 여러 개에 한 번에 풀기
x, y = point
print(f"x={x}, y={y}")    # x=3, y=4

# point[0] = 10  # TypeError! 튜플은 수정 불가능 (immutable)

# ============================================================
# 3. 딕셔너리 (Dictionary) — 키로 값을 찾는 사전
# ============================================================

# 사전(dictionary)에서 단어로 뜻을 찾듯, 키(key)로 값(value)을 찾습니다.

empty_d = {}
pet = {"name": "Leo", "age": 7}

# --- 접근(access)과 수정(modify) ---
print(pet["name"])              # "Leo"
pet["sound"] = "야옹"           # 새 키-값 추가
pet["age"] = 8                  # 기존 값 수정

# get(): 키가 없어도 에러 안 남, 기본값(default)을 돌려줌
age = pet.get("age", 0)
missing = pet.get("weight", "없음")  # "없음"

# --- 삭제 ---
del pet["sound"]

# --- 키/값/쌍 조회 ---
info = {"name": "Frieda", "sound": "왈왈"}
print(list(info.keys()))    # ['name', 'sound']      모든 키
print(list(info.values()))  # ['Frieda', '왈왈']     모든 값
print(list(info.items()))   # [('name', 'Frieda'), ('sound', '왈왈')]  쌍

# ============================================================
# 4. 셋 (Set) — 중복 없는 묶음
# ============================================================

# 중복(duplicate)을 자동으로 제거하고, 집합 연산(union, intersection 등)이 가능합니다.

a = {1, 2, 3}
b = set([3, 4, 4, 5])   # 중복 자동 제거 → {3, 4, 5}
empty_s = set()         # 빈 셋. 주의: {} 는 빈 딕셔너리!

# --- 집합 연산 (set operations) ---
print(a | b)    # {1, 2, 3, 4, 5}   합집합 (union)
print(a & b)    # {3}               교집합 (intersection)
print(a - b)    # {1, 2}            차집합 (difference)

# --- 추가/제거 ---
a.add(10)
a.discard(2)    # 없어도 에러 안 남
print(3 in a)   # True

# --- 가장 흔한 활용: 리스트 중복 제거 ---
numbers = [1, 2, 2, 3, 3, 3]
unique = list(set(numbers))
print(f"중복 제거: {unique}")  # [1, 2, 3]

# ============================================================
# 실행 (Run Examples)
# ============================================================
if __name__ == "__main__":
    print("\n=== 4가지 컬렉션 비교 ===")
    print("list  [1,2,3]   → 순서O, 변경O, 중복O")
    print("tuple (1,2,3)   → 순서O, 변경X, 중복O")
    print("dict  {k:v}     → 순서O, 변경O, 키 중복X")
    print("set   {1,2,3}   → 순서X, 변경O, 중복X")
