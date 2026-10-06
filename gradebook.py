import csv
import sys
from pathlib import Path


def mean(scores):
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def letter_grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        return mean(self.scores)

    def grade(self):
        return letter_grade(self.average())


class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def class_average(self):
        return mean([student.average() for student in self.students])


def load_students(path):
    students = []
    with path.open(newline="", encoding="utf-8") as csv_file:
        for row in csv.reader(csv_file):
            if row:
                students.append(Student(row[0], [float(score) for score in row[1:]]))
    return students


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    students = load_students(Path(__file__).with_name("students.csv"))
    gradebook = GradeBook()
    for student in students:
        gradebook.add_student(student)

    print("📖 GradeBook CLI 실행 중...")
    print(f"\n전체 반 평균 점수: {gradebook.class_average():.2f}\n")
    for student in gradebook.students:
        print(f"{student.name}: 평균={student.average():.1f}, 학점={student.grade()}")


if __name__ == "__main__":
    main()
