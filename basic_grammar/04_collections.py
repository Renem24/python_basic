"""
04. 컬렉션 (Collections)

이 파일에서 다루는 내용:
- 리스트 (List) - 순서 O, 변경 O, 중복 O
- 튜플 (Tuple) - 순서 O, 변경 X, 중복 O
- 딕셔너리 (Dictionary) - 순서 O(3.7+), 변경 O, 키 중복 X
- 셋 (Set) - 순서 X, 변경 O, 중복 X

참고: Real Python Pocket Reference
"""

# ============================================================
# 1. 리스트 (List)
# ============================================================

# --- 생성 ---
empty = []
nums = [1, 2, 3]
mixed = [1, "two", 3.0, True]  # 다양한 타입 혼합 가능

# --- 인덱싱 ---
fruits = ["사과", "바나나", "오렌지"]
print(fruits[0])    # "사과"     첫 번째 원소
print(fruits[-1])   # "오렌지"   마지막 원소
print(fruits[0:2])  # ["사과", "바나나"]  슬라이싱

# --- 주요 메서드 ---
fruits.append("포도")         # 끝에 추가: ["사과", "바나나", "오렌지", "포도"]
fruits.insert(1, "딸기")      # 1번 위치에 삽입
fruits.extend(["키위", "망고"])  # 여러 원소 추가
fruits.remove("바나나")       # 값으로 삭제 (첫 번째 일치)
last = fruits.pop()           # 마지막 원소 제거 후 반환
print(f"pop한 값: {last}")

# --- 기타 연산 ---
print("사과" in fruits)       # True   포함 여부
print(len(fruits))            # 원소 개수

numbers = [3, 1, 4, 1, 5]
numbers.sort()                # 오름차순 정렬 (원본 변경)
print(numbers)                # [1, 1, 3, 4, 5]
print(sorted([3, 1, 2]))     # [1, 2, 3] (원본 유지, 새 리스트 반환)

# ============================================================
# 2. 튜플 (Tuple)
# ============================================================

# --- 생성 ---
point = (3, 4)
single = (1,)   # 원소 1개짜리 튜플 (쉼표 필수!)
empty_t = ()

# --- 기본 언패킹 ---
x, y = point
print(f"x={x}, y={y}")       # x=3, y=4

# --- 확장 언패킹 ---
first, *rest = (1, 2, 3, 4)
print(f"first={first}")      # 1
print(f"rest={rest}")         # [2, 3, 4]

# --- 불변성 ---
# point[0] = 10  # TypeError! 튜플은 수정 불가

# 튜플은 딕셔너리 키나 셋 원소로 사용 가능 (불변이므로)
locations = {(37.5, 127.0): "서울", (35.1, 129.0): "부산"}
print(locations[(37.5, 127.0)])  # "서울"

# ============================================================
# 3. 딕셔너리 (Dictionary)
# ============================================================

# --- 생성 ---
empty_d = {}
pet = {"name": "Leo", "age": 7}

# --- 접근 및 수정 ---
print(pet["name"])             # "Leo"   키로 접근
pet["sound"] = "야옹"          # 새 키-값 추가
pet["age"] = 8                 # 기존 값 수정
age = pet.get("age", 0)        # get()은 키가 없으면 기본값 반환
missing = pet.get("weight", "없음")  # "없음"

# --- 삭제 ---
del pet["sound"]               # 키 삭제
removed = pet.pop("age")       # 삭제하면서 값 반환
print(f"삭제된 값: {removed}") # 8

# --- 주요 메서드 ---
info = {"name": "Frieda", "sound": "왈왈"}
print(list(info.keys()))       # ['name', 'sound']
print(list(info.values()))     # ['Frieda', '왈왈']
print(list(info.items()))      # [('name', 'Frieda'), ('sound', '왈왈')]

# 딕셔너리 순회
for key, value in info.items():
    print(f"  {key}: {value}")

# ============================================================
# 4. 셋 (Set)
# ============================================================

# --- 생성 ---
a = {1, 2, 3}
b = set([3, 4, 4, 5])   # 중복 자동 제거 → {3, 4, 5}
empty_s = set()          # 빈 셋 ({}는 빈 딕셔너리!)

# --- 집합 연산 ---
print(a | b)    # {1, 2, 3, 4, 5}  합집합
print(a & b)    # {3}              교집합
print(a - b)    # {1, 2}           차집합
print(a ^ b)    # {1, 2, 4, 5}     대칭 차집합

# --- 원소 추가/제거 ---
a.add(10)       # 추가
a.discard(2)    # 제거 (없어도 에러 안 남)
print(3 in a)   # True  포함 여부

# --- 활용: 중복 제거 ---
numbers = [1, 2, 2, 3, 3, 3]
unique = list(set(numbers))
print(f"중복 제거: {unique}")   # [1, 2, 3] (순서 보장 안 됨)

# ============================================================
# 실행 (Run Examples)
# ============================================================
if __name__ == "__main__":
    print("\n=== 컬렉션 비교 ===")
    print(f"리스트 [1,2,3]  → 순서O, 변경O, 중복O")
    print(f"튜플  (1,2,3)   → 순서O, 변경X, 중복O")
    print(f"딕셔너리 {{k:v}} → 순서O, 변경O, 키중복X")
    print(f"셋    {{1,2,3}} → 순서X, 변경O, 중복X")

    # 공통 연산: len(), in
    data = [10, 20, 30]
    print(f"\nlen({data}) = {len(data)}")
    print(f"20 in {data} = {20 in data}")
