# ---------------------------------------------
# gradebook/io/csvio.py
# ---------------------------------------------

"""CSV 파일로부터 학생 정보를 읽고 쓰는 모듈"""

import csv
from ..models import Student

def load_students_from_csv(path):
    """CSV 파일에서 학생 목록을 읽어옴
    CSV 형식: name,score1,score2,score3,...
    """
    students = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[0]
            scores = [float(x) for x in row[1:]]
            students.append(Student(name, scores))
    return students


def save_students_to_csv(path, students):
    """학생 리스트를 CSV 파일로 저장"""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for s in students:
            writer.writerow([s.name] + s.scores)
