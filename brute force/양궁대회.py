from copy import deepcopy
max_diff = 1
arr = [0] * (10)

def comp(a, b):
    a_res = 0
    b_res = 0
    
    index = 0
    score = 10
    while index < 10:
        if a[index] == b[index] and b[index] == 0:
            pass
        elif a[index] >= b[index]:
            a_res += score
        else:
            b_res += score
        
        index += 1
        score -= 1
        
    return b_res - a_res



def solution(n, info):  
    answer = [0] * (11)

    def go(index, start, n):
        global max_diff

        if index == n: 
            res = comp(info, arr)
            if res > max_diff:
                max_diff = res
                for i in range(10):
                    answer[i] = arr[i]
            return

        for i in range(start, 11):
            if i != 0:
                arr[10-i] += 1
            go(index+1, i, n)
            if i != 0:
                arr[10-i] -= 1

    go(0, 0, n)
    
    t = sum(answer)
    if t == 0:
        return [-1]
    
    answer[-1] = n - t
    
    return answer

 