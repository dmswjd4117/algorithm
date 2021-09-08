from itertools import combinations


def solution(orders, course):
    answer = []
    
    for k in course:
        dict = {}
        
        for order in orders:
            combins = combinations(order, k)
            for menus_t in combins:
                menus = "".join(sorted(list(menus_t)))
                if menus not in dict.keys():
                    dict[menus] = 1
                else:
                    dict[menus] += 1
                    
        dict = sorted(dict.items(), key=lambda x : x[1], reverse=True)
        
        if dict:
            temp = dict[0][1]
            for menu , cnt in dict:
                if cnt < 2:
                    break
                if cnt != temp:
                    break
                answer.append(menu)
                
    answer.sort()
    return answer




# 2 
# 95/100 시간초과

from itertools import combinations

orders_set = []


def check(menus):
    cnt = 0
    
    for order in orders_set:
        for menu in menus:
            if menu not in order:
                break
        else:
            cnt += 1
            
    return cnt

 
def solution(orders, course):
    answer = []
    alphas = set()
    N = len(orders)
    
    for order in orders:
        temp = set()
        for c in order:
            temp.add(c)
            alphas.add(c)
        orders_set.append(temp)
    
    alphas = list(alphas)
    alphas.sort()
    
    for number in course:
        perm = combinations(alphas, number)
        temp = []
        big = 2

        for menu in perm:
            cnt = check(menu)
            if cnt >= big:
                big = cnt
                temp.append((cnt, menu))
         
        for cnt, menu in temp:
            if cnt == big:
                answer.append("".join(menu))
  
            
    answer.sort()
    
    return answer


'''
1) 
주문당 가능한 조합의 수를 세기
VS 
2)
가능한 조합들을 만든후 
주문들중 2번이상 포함된 조합 찾기

-> 가능한 조합들이 몇번 포함되었는지 탐색하는데 
o(조합의 길이*메뉴길이*메뉴개수)
'''