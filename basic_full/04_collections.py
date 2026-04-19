"""
04. 컬렉션 (Collections) - 심화

이 파일에서 다루는 것:
- 가변(mutable) vs 불변(immutable) 차이
- 리스트(list) 메서드 추가 + 슬라이싱 할당, 정렬 옵션
- 튜플(tuple)을 dict 키로 사용 (불변이라 가능)
- 딕셔너리(dict) 추가 메서드 (setdefault, update)
- 셋(set) 전체 연산 + 부분/상위 집합 검사
- 중첩 컬렉션 (nested collections)
- 얕은 복사(shallow copy) vs 깊은 복사(deep copy)

💡 basic_core/04 를 먼저 보세요.

       | 순서(order) | 변경(mutable) | 중복(duplicate) | 표기
-------+-------------+---------------+-----------------+------
list   |     O       |       O       |        O        | [...]
tuple  |     O       |       X       |        O        | (...)
dict   |     O       |       O       |   키 X / 값 O   | {k:v}
set    |     X       |       O       |        X        | {...}
"""

# ============================================================
# 0. 가변 vs 불변 (Mutable vs Immutable) — 핵심 개념
# ============================================================
#
# 가변(mutable):   객체 내용을 바꿀 수 있음 → list, dict, set
# 불변(immutable): 한번 만들면 바꿀 수 없음 → int, float, str, tuple, frozenset
#
# 왜 중요한가?
#  - 불변 객체만 dict 의 키나 set 의 원소로 쓸 수 있음
#  - 함수에 가변 객체를 넘기면 함수 안에서 원본이 바뀔 수 있음 (주의!)

s = "hello"
# s[0] = "H"   # ✗ TypeError (str 은 불변)

lst = [1, 2, 3]
lst[0] = 99    # ✓ OK (list 는 가변)
print(lst)     # [99, 2, 3]

# ============================================================
# 1. 리스트 (List) — 심화
# ============================================================

fruits = ["사과", "바나나", "오렌지"]

# --- 메서드 정리 (basic_core 복습 + 추가) ---
fruits.append("포도")             # 끝에 추가
fruits.insert(1, "딸기")          # 위치에 끼워넣기
fruits.extend(["키위", "망고"])   # 여러 개 추가 (리스트 펼침)
print(fruits)

fruits.remove("바나나")           # 값으로 삭제 (첫 번째 일치)
last = fruits.pop()               # 마지막 꺼냄
first = fruits.pop(0)             # 인덱스로 꺼냄
print(f"pop: {first}, {last}")
print(fruits.index("오렌지"))    # 위치 찾기

# --- 슬라이싱 할당 (slice assignment) ---
nums = [1, 2, 3, 4, 5]
nums[1:4] = [20, 30, 40]          # 일부 구간을 통째로 교체
print(nums)                        # [1, 20, 30, 40, 5]

nums[1:4] = [99]                  # 길이가 달라도 OK
print(nums)                        # [1, 99, 5]

del nums[0]                       # 위치로 삭제
print(nums)                        # [99, 5]

# --- 정렬 옵션 ---
words = ["banana", "Apple", "cherry"]
words.sort()                      # 기본 정렬 (대소문자 구분: 대문자 먼저)
print(words)
words.sort(key=str.lower)         # 대소문자 무시
print(words)
words.sort(reverse=True)          # 내림차순
print(words)

# 길이 기준 정렬
words.sort(key=len)
print(words)

# sort() vs sorted() — 원본 변경 vs 새 리스트
original = [3, 1, 2]
new_list = sorted(original)       # original 유지, 새 리스트 반환
print(original, new_list)         # [3, 1, 2] [1, 2, 3]

# --- 리스트 컴프리헨션 (list comprehension) — 한 줄 리스트 생성 ---
squares = [x ** 2 for x in range(5)]
print(squares)                    # [0, 1, 4, 9, 16]

evens = [x for x in range(10) if x % 2 == 0]
print(evens)                      # [0, 2, 4, 6, 8]

# 위는 다음과 동등:
#   squares = []
#   for x in range(5):
#       squares.append(x ** 2)

# ============================================================
# 2. 튜플 (Tuple) — 심화
# ============================================================

# --- 튜플의 진가: dict 키와 set 원소로 사용 가능 ---
# 불변(immutable)이라 해시(hash)가 가능해서 키로 쓸 수 있습니다.
# 리스트는 가변이라 키로 못 씀!

locations = {(37.5, 127.0): "서울", (35.1, 129.0): "부산"}
print(locations[(37.5, 127.0)])   # "서울"

# 좌표 셋
points = {(0, 0), (1, 1), (2, 2)}
print((1, 1) in points)            # True

# --- 단일 원소 튜플은 쉼표 필수 ---
not_tuple = (1)        # 그냥 정수 1
real_tuple = (1,)      # 튜플
print(type(not_tuple), type(real_tuple))

# --- 명명된 튜플 (namedtuple) — 맛보기 ---
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)        # 3 4 (인덱스 아닌 이름으로 접근!)

# ============================================================
# 3. 딕셔너리 (Dictionary) — 심화
# ============================================================

pet = {"name": "Leo", "age": 7}

# --- 추가 메서드 ---
# setdefault: 키가 있으면 값 반환, 없으면 추가하고 반환
pet.setdefault("color", "흰색")   # color 가 없으니 추가됨
print(pet)
pet.setdefault("color", "검정")   # 이미 있으니 무시됨, 기존값 반환
print(pet)

# update: 다른 dict로 일괄 갱신
pet.update({"age": 8, "weight": 5.2})
print(pet)

# pop: 키로 삭제하면서 값 반환 (기본값 지정 가능)
removed = pet.pop("weight", None)
print(f"removed: {removed}")

# --- 순회 (iteration) ---
for key in pet:                      # 기본은 키만
    print(f"  키: {key}")

for key, value in pet.items():       # 키-값 쌍
    print(f"  {key} = {value}")

# --- dict 컴프리헨션 ---
squares = {x: x ** 2 for x in range(5)}
print(squares)                       # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# --- 두 리스트로 dict 만들기 (zip 활용) ---
keys = ["name", "age", "city"]
values = ["Alice", 25, "Seoul"]
person = dict(zip(keys, values))
print(person)

# ============================================================
# 4. 셋 (Set) — 심화
# ============================================================

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# --- 모든 집합 연산 ---
print(a | b)    # {1,2,3,4,5,6}  합집합 (union)
print(a & b)    # {3, 4}         교집합 (intersection)
print(a - b)    # {1, 2}         차집합 (difference)
print(a ^ b)    # {1,2,5,6}      대칭차집합 (symmetric difference) — 둘 중 한쪽만 있는 원소

# 메서드 형태로도 가능
print(a.union(b))
print(a.intersection(b))

# --- 부분집합/상위집합 검사 ---
small = {1, 2}
print(small.issubset(a))     # True   small ⊆ a
print(a.issuperset(small))   # True   a ⊇ small
print(small.isdisjoint({99, 100}))  # True   교집합 없음

# --- frozenset: 불변 셋 (set 의 원소나 dict 키로 쓸 수 있음) ---
fs = frozenset([1, 2, 3])
# fs.add(4)   # ✗ AttributeError
print(fs)

# --- set 컴프리헨션 ---
unique_lengths = {len(w) for w in ["hi", "bye", "yes", "no"]}
print(unique_lengths)        # {2, 3}

# ============================================================
# 5. 중첩 컬렉션 (Nested Collections)
# ============================================================

# 행렬 (2차원 리스트)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix[1][2])          # 6 (1행 2열)

# 학생 정보 (dict 안에 list)
students = {
    "Alice": {"age": 25, "scores": [90, 85, 95]},
    "Bob":   {"age": 30, "scores": [70, 80, 75]},
}
print(students["Alice"]["scores"][0])    # 90

# ============================================================
# 6. 얕은 복사 vs 깊은 복사 (Shallow vs Deep Copy)
# ============================================================

import copy

original = [[1, 2], [3, 4]]

# 얕은 복사: 바깥은 새로, 안쪽은 공유
shallow = copy.copy(original)
shallow[0][0] = 99
print(original)              # [[99, 2], [3, 4]]  ← 원본도 바뀜!

# 깊은 복사: 모든 단계까지 새로 복사
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 99
print(original)              # [[1, 2], [3, 4]]  ← 원본 그대로

# ============================================================
# 실행 (Run Examples)
# ============================================================
if __name__ == "__main__":
    print("\n=== 종합 예제: 단어 빈도 세기 ===")
    text = "사과 바나나 사과 오렌지 바나나 사과 포도"
    words = text.split()

    # 방법 1: dict 로 직접
    count = {}
    for w in words:
        count[w] = count.get(w, 0) + 1
    print(count)

    # 가장 많은 단어
    most = max(count, key=count.get)
    print(f"최다 단어: {most} ({count[most]}회)")

    # 중복 제거된 단어들 (set)
    unique = set(words)
    print(f"고유 단어 수: {len(unique)}")
