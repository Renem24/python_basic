"""
01. 파이썬 개요 (Python Overview) - 심화

이 파일에서 다루는 것:
- 파이썬의 특징과 활용 분야
- 파이썬 설치 (운영체제별 상세)
- 파이썬 실행 방법 (스크립트 / REPL / -i 옵션)
- 에디터(Editor) / 통합개발환경(IDE) 선택
- 패키지 관리 (pip)와 가상 환경 (venv) 맛보기

💡 basic_core/01 을 먼저 보세요. 여기서는 같은 주제를 더 깊이 설명하고
   실무에서 알아야 할 추가 개념을 소개합니다.
"""

# ============================================================
# 0. 파이썬이란? (What is Python?)
# ============================================================
#
# 파이썬(Python)은 1991년 귀도 반 로섬(Guido van Rossum)이 만든 프로그래밍 언어.
#
# 특징:
#   - 인터프리터 언어(interpreted language): 컴파일 없이 줄 단위로 실행
#   - 동적 타입(dynamic typing): 변수 타입을 미리 선언하지 않음
#   - 들여쓰기(indentation)로 코드 블록 구분 — 가독성 강제
#   - 풍부한 표준 라이브러리(standard library)와 외부 패키지 생태계
#
# 주요 활용 분야:
#   - 데이터 분석/머신러닝 (pandas, numpy, scikit-learn, PyTorch)
#   - 웹 개발 (Django, Flask, FastAPI)
#   - 자동화/스크립팅 (시스템 관리, 크롤링)
#   - 교육 (입문 언어로 가장 인기)

# ============================================================
# 1. 파이썬 설치 (Installing Python)
# ============================================================
#
# 공식 사이트: https://www.python.org/downloads/
#
# [Windows]
#   - python.org에서 설치 파일 다운로드 후 실행
#   - 설치 시 "Add Python to PATH" 체크 필수
#       → 안 하면 cmd/PowerShell 에서 python 명령어가 안 먹힘
#   - 또는 winget: winget install Python.Python.3.12
#
# [macOS]
#   - 공식 권장: brew install python3
#   - 시스템에 기본 설치된 python3는 건드리지 마세요 (시스템 의존성)
#
# [Linux]
#   - Ubuntu/Debian: sudo apt install python3 python3-pip
#   - Fedora: sudo dnf install python3
#
# 설치 확인:
#   $ python --version       # 또는 python3 --version
#   Python 3.12.0
#
# 💡 운영체제에 따라 명령어가 python 또는 python3 로 갈립니다.

# ============================================================
# 2. 파이썬 실행 (Running Python) — 3가지 방법
# ============================================================
#
# 방법 1: 스크립트 실행 (Script Execution)
# ---------------------------------------
#   .py 파일에 코드를 저장하고 통째로 실행.
#
#     $ python my_script.py
#
#   장점: 같은 코드 반복 실행 가능, 큰 프로그램에 적합.
#
# 방법 2: 대화형 셸 / REPL (Read-Eval-Print Loop)
# -----------------------------------------------
#   터미널에서 한 줄씩 즉시 실행. 처음 배울 때 가장 좋은 방식!
#
#     $ python
#     Python 3.12.0 ...
#     >>> 2 + 3
#     5
#     >>> name = "Alice"
#     >>> print(f"Hi, {name}!")
#     Hi, Alice!
#     >>> exit()
#
#   장점: 즉시 결과 확인, 가벼운 실험에 좋음.
#
# 방법 3: 스크립트 + REPL (-i 옵션)
# ---------------------------------
#   스크립트 실행 후 REPL이 열려서 변수를 확인할 수 있음. 디버깅에 유용.
#
#     $ python -i my_script.py

# ============================================================
# 3. 에디터와 IDE (Editor & IDE)
# ============================================================
#
# 에디터(Editor): 코드 편집기. 가볍고 빠름.
# IDE(Integrated Development Environment): 편집 + 디버깅 + 빌드 등 통합 도구.
#
# 추천:
#   - VS Code: 무료, 확장 풍부, 가장 많이 씀
#       필수 확장: Python (Microsoft), Pylance
#   - PyCharm: 파이썬 전용 IDE, Community 무료, 강력한 디버거
#   - Jupyter Notebook: 셀(cell) 단위 실행, 데이터 분석/학습용
#   - IDLE: 파이썬 설치 시 기본 포함, 가장 단순
#
# 권장 설정:
#   - 들여쓰기: 스페이스(space) 4칸 (탭 X)  ← PEP 8
#   - 인코딩: UTF-8
#   - 린터(linter): Pylint, flake8, ruff 등으로 코드 품질 검사

# ============================================================
# 4. 패키지 관리 - pip (Package Manager) ★ 맛보기
# ============================================================
#
# pip: 파이썬의 공식 패키지 설치 도구. 외부 라이브러리(library)를 받습니다.
#
# 설치:
#   $ pip install requests           # requests 라이브러리 설치
#   $ pip install numpy pandas       # 여러 개 한 번에
#   $ pip install requests==2.31.0   # 특정 버전
#
# 조회/제거:
#   $ pip list                       # 설치된 패키지 목록
#   $ pip show requests              # 패키지 정보
#   $ pip uninstall requests         # 제거
#
# 의존성 관리:
#   $ pip freeze > requirements.txt        # 현재 환경 저장
#   $ pip install -r requirements.txt      # 저장된 목록 일괄 설치

# ============================================================
# 5. 가상 환경 - venv (Virtual Environment) ★ 맛보기
# ============================================================
#
# 프로젝트마다 패키지를 독립적으로 관리하기 위한 격리 환경.
# 프로젝트 A는 Django 4, 프로젝트 B는 Django 5를 따로 쓸 수 있게 됨.
#
# 만들기 / 활성화:
#   $ python -m venv .venv             # .venv 폴더에 가상환경 생성
#   $ source .venv/bin/activate        # macOS/Linux 활성화
#   $ .venv\Scripts\activate           # Windows 활성화
#   (이후 pip install 은 이 환경에만 영향)
#
# 비활성화:
#   $ deactivate
#
# 💡 실무에서는 거의 항상 가상환경을 사용합니다. 입문 단계에서는
#    "이런 게 있다" 정도만 알아두고, 프로젝트가 늘어나면 적용하세요.

# ============================================================
# 실행 예제 (Run Examples)
# ============================================================
import sys
import platform

if __name__ == "__main__":
    print("=== 내 파이썬 환경 정보 ===")
    print(f"Python 버전: {sys.version}")
    print(f"버전 정보(version_info): {sys.version_info}")
    print(f"플랫폼: {sys.platform}")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"실행 경로: {sys.executable}")
    print(f"모듈 검색 경로 개수: {len(sys.path)}")
