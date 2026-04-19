# python-basic

파이썬 기초 문법을 주제별로 정리한 학습용 저장소.

**2단계 학습 구조**로 되어 있어 입문자가 단계적으로 학습할 수 있다.

- `basic_core/` — **하루 입문 강의용**. 핵심만 추려 쉬운 설명 포함.
- `basic_full/` — **심화 학습용**. core 학습 후 더 깊은 내용과 함정/예제까지.

각 파일은 독립적으로 실행 가능하며, 코드와 주석을 함께 읽으며 학습한다.

## 구조

```
basic_core/                          # 1단계: 핵심 (입문자가 먼저 학습)
├── 01_python_overview.py            # 파이썬 개요 / 설치 / 실행 / 에디터
├── 02_variables_and_types.py        # 변수와 자료형 (int, float, bool)
├── 03_strings.py                    # 문자열 / 인덱싱 / f-string
├── 04_collections.py                # 리스트 / 튜플 / 딕셔너리 / 셋
├── 05_operators.py                  # 비교 / 논리 / 비트 연산자
├── 06_control_flow.py               # if / for / while / break / continue
├── 07_functions_basic.py            # 내장 함수 / 사용자 정의 함수 / 리턴
└── 08_functions_parameters.py       # 매개변수 / 키워드 인자 / 디폴트 값

basic_full/                          # 2단계: 심화 (core 학습 후 참고)
├── 01_python_overview.py            # + pip / venv / Python 특징
├── 02_variables_and_types.py        # + complex / isinstance / 확장 언패킹
├── 03_strings.py                    # + 메서드 전체 / format spec / raw string
├── 04_collections.py                # + 컴프리헨션 / namedtuple / 깊은 복사
├── 05_operators.py                  # + == vs is / 단축 평가 / 권한 플래그
├── 06_control_flow.py               # + match-case / for-else / 소수 찾기
├── 07_functions_basic.py            # + scope / first-class / map·filter
└── 08_functions_parameters.py       # + mutable default 함정 / *args / **kwargs / lambda

ref/
└── python-cheatsheet.pdf            # 참고 치트시트
```

## 학습 순서 권장

1. `basic_core/` 의 01 → 08 순서대로 학습
2. 각 주제마다 코드를 직접 입력하며 실행
3. 더 깊이 알고 싶을 때 `basic_full/` 의 같은 번호 파일을 참고

> 💡 **하루 강의 운영 시**
> 4교시 × 90분 기준으로 `basic_core/` 만 다루는 것을 권장.
> `basic_full/` 은 강의 후 자율 학습/심화 자료로 활용.

## 요구사항

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (패키지 매니저)

## 실행

```bash
# core 파일 실행 (입문)
uv run python basic_core/01_python_overview.py
uv run python basic_core/03_strings.py

# full 파일 실행 (심화)
uv run python basic_full/04_collections.py
```

## 토픽 매핑

| 토픽 | core | full 추가 내용 |
|---|---|---|
| 파이썬 개요 | 설치/실행/에디터 | + pip, venv, 활용 분야 |
| 변수와 자료형 | int, float, bool, 변환 | + complex, 부동소수점, isinstance |
| 문자열 | 메서드 6종, f-string 기본 | + 메서드 전체, format spec, raw string |
| 컬렉션 | list, tuple, dict, set 기본 | + 컴프리헨션, 중첩, 복사, namedtuple |
| 연산자 | 비교/논리/in, 비트(참고) | + == vs is, 단축 평가, 권한 플래그 |
| 제어문 | if / for / while / break | + match-case, for-else, FizzBuzz, 소수 |
| 함수 기초 | 내장/정의/리턴 | + scope, first-class, map/filter/lambda |
| 함수 매개변수 | 위치/키워드/디폴트 | + mutable default 함정, *args, **kwargs, lambda 심화 |
