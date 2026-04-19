# python-basic

파이썬 기초 문법을 주제별로 정리한 학습용 저장소.

각 파일은 독립적으로 실행 가능하며, 코드와 주석을 함께 읽으며 학습할 수 있도록 구성되어 있다.

## 구조

```
basic_grammar/
├── 01_python_overview.py        # 파이썬 개요
├── 02_variables_and_types.py    # 변수와 자료형
├── 03_strings.py                # 문자열
├── 04_collections.py            # 컬렉션 (리스트, 딕셔너리 등)
├── 05_operators.py              # 연산자
├── 06_control_flow.py           # 조건문과 반복문
├── 07_functions_basic.py        # 함수 기초
└── 08_functions_parameters.py   # 함수 매개변수
ref/
└── python-cheatsheet.pdf        # 참고 치트시트
```

## 요구사항

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (패키지 매니저)

## 실행

```bash
# 개별 파일 실행
uv run python basic_grammar/01_python_overview.py

# 원하는 주제만 골라서 실행
uv run python basic_grammar/03_strings.py
```


