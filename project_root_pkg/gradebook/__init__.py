# ---------------------------------------------
# gradebook/__init__.py
# ---------------------------------------------

"""
GradeBook 패키지

학생 성적 관리 프로그램
- utils: 평균, 학점 계산 함수
- models: Student, GradeBook 클래스
- io.csvio: CSV 파일 입출력
- cli: 명령행 실행 인터페이스
"""

from .models import Student, GradeBook
from .utils import mean, letter_grade

__all__ = ["Student", "GradeBook", "mean", "letter_grade"]
__version__ = "1.0.0"
