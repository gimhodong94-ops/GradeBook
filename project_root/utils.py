# ----------------------------------------
# utils.py : 계산 관련 함수
# ----------------------------------------

# 평균을 계산하는 함수
def mean(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

# 평균 점수에 따라 학점을 정하는 함수
def letter_grade(score):
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
