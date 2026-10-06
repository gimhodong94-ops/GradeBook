# ---------------------------------------------
# gradebook/cli.py
# ---------------------------------------------

"""명령행 실행 인터페이스 (CLI)"""

import sys
from pathlib import Path

from .models import Student, GradeBook
from .io.csvio import load_students_from_csv

def run_cli():
    """터미널에서 실행할 간단한 CLI"""
    sys.stdout.reconfigure(encoding="utf-8")
    print("📖 GradeBook CLI 실행 중...")
    
    # CSV 파일로부터 데이터 불러오기 (예시)
    try:
        students = load_students_from_csv(Path(__file__).with_name("students.csv"))
    except FileNotFoundError:
        print("⚠️ students.csv 파일이 없습니다. 기본 데이터 사용.")
        students = [
            Student("Alice", [90, 85, 92]),
            Student("Bob", [70, 75, 68]),
        ]
        
    gb = GradeBook()
    for s in students:
        gb.add_student(s)
        
    print(f"\n전체 반 평균 점수: {gb.class_average():.2f}\n")
    for s in gb.students:
        print(f"{s.name}: 평균={s.average():.1f}, 학점={s.grade()}")
