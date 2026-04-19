"""
01. 파이썬 개요 (Python Overview)

이 파일에서 다루는 것:
- 파이썬 설치
- 파이썬 실행 방법
- 에디터 선택
"""

# ============================================================
# 1. 파이썬 설치 (Installing Python)
# ============================================================
#
# 공식 사이트: https://www.python.org/downloads/
#
# [Windows]
#   - python.org에서 설치 파일 다운로드 후 실행
#   - 설치 시 "Add Python to PATH" 체크 필수
#   - 또는 winget 사용: winget install Python.Python.3.12
#
# [macOS]
#   - brew install python3
#   - 또는 python.org에서 설치 파일 다운로드
#
# [Linux]
#   - Ubuntu/Debian: sudo apt install python3
#   - Fedora: sudo dnf install python3
#
# 설치 확인:
#   $ python --version
#   $ python3 --version

# ============================================================
# 2. 파이썬 실행 (Running Python)
# ============================================================
#
# 방법 1: 스크립트 실행
#   $ python my_script.py
#
# 방법 2: 대화형 셸 (Interactive Shell / REPL)
#   $ python
#   >>> print("Hello!")
#   Hello!
#   >>> exit()
#
# 방법 3: 스크립트를 대화형 모드로 실행
#   $ python -i my_script.py
#   (스크립트 실행 후 대화형 셸이 열려서 변수 확인 가능)

# ============================================================
# 3. 에디터 (Editor)
# ============================================================
#
# 추천 에디터/IDE:
#   - VS Code: 무료, 가볍고 확장 기능 풍부 (Python 확장 설치 권장)
#   - PyCharm: Python 전용 IDE, Community 버전 무료
#   - Jupyter Notebook: 데이터 분석/학습에 적합
#   - IDLE: Python 설치 시 기본 포함
#
# 에디터 설정 시 권장사항:
#   - 들여쓰기: 스페이스 4칸 (탭 대신 스페이스)
#   - 인코딩: UTF-8
#   - 린터(linter) 활성화: 코드 품질 검사

# ============================================================
# 실행 예제
# ============================================================
import sys

if __name__ == "__main__":
    # 현재 파이썬 버전 확인
    print(f"Python 버전: {sys.version}")

    # 실행 중인 플랫폼 확인
    print(f"플랫폼: {sys.platform}")

    # 파이썬 실행 파일 경로 확인
    print(f"실행 경로: {sys.executable}")
