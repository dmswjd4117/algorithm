#https://programmers.co.kr/learn/courses/30/lessons/77486?language=python3


def solution(enroll, referral, seller, amount):
    N = len(enroll)
    answer = []
    p = {'root' : 'root'}
    moneys = {'root' : 0}
    
    # 돈, 부모 초기화
    for e, pe in zip(enroll,referral):
        if pe != '-':
            p[e] = pe
        else:
            p[e] = 'root'
        moneys[e] = 0
    
    def go(x, cost):
        if x == 'root':
            return 
        temp = cost // 10
        moneys[x] -= temp
        moneys[p[x]] += temp
        if temp == 0:
            return
        go(p[x], temp)
    
    for s, cnt in zip(seller, amount):
        cost = cnt * 100
        moneys[s] += cost        
        go(s, cost)
        
    for e in enroll:
        answer.append(moneys[e])
        
    return answer

