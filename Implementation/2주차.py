from collections import Counter

INF = float('inf')
scores = []
a = 2
n = 0

def get_grade(num):
    if num >= 90:
        return 'A'
    if num >= 80:
        return 'B'
    if num >= 70:
        return 'C'
    if num >= 50:
        return 'D'
    return 'F'

def check(index):
    fix = scores[index][index]
    max_num = max(scores[index])
    min_num = min(scores[index])

    if max_num <= fix or min_num >= fix:
        if Counter(scores[index])[fix] == 1:
            return False

    return True

def cal(number):    
    hap = 0
    cnt = 0

    for index, score in enumerate(scores[number]):
        if index == number:
            if check(index):
                hap += scores[number][index]
                cnt += 1
        else:
            hap += scores[number][index]
            cnt += 1

    res = hap / cnt
    return res
    
    
def solution(scores_param):
    global n, scores
    
    answer = ''
    n = len(scores_param)
    scores = list(map(list, zip(*scores_param)))

    for i in range(n):
        answer += get_grade(cal(i))
            
    return answer


