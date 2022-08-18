# [과제2][본인이름] 다음 조건에 맞게 python 프로그래밍하시오.
korean, english, mathematics, science = 100, 86, 81, 91
def get_max_score(*v):
    print(*v)
    return max(v)

max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)

max_score = get_max_score(english, science)
print('높은 점수:', max_score)