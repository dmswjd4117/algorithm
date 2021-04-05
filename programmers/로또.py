def find(num):
    if num <= 1:
        return 6
    return 7-num

def solution(lottos, win_nums):
    answer = []
    ans = len(set(lottos) & set(win_nums))
    cnt = 0
    for i in lottos:
        if i == 0:
            cnt += 1
    a = cnt + ans
    b = ans
    a = find(a)
    b = find(b)
    answer.append(a)
    answer.append(b)
    return answer