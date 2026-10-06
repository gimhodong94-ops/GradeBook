# ---------------------------------------------
# gradebook/utils.py
# ---------------------------------------------

"""성적 계산 관련 유틸리티 함수"""

def mean(scores):
    """리스트의 평균을 계산"""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

def letter_grade(score):
    """점수에 따른 학점 반환"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
