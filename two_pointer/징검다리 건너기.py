# https://programmers.co.kr/learn/courses/30/lessons/64062

import sys
from copy import deepcopy

INF = 200_000_000 
hs = set([])

sys.setrecursionlimit(10**5)
 

def is_possible(t, arr, k):
    N = len(arr)
    T = t-1
    cnt = 0
    for i in range(N):
        
        if arr[i] - T <= 0:
            cnt += 1
        else:
            cnt = 0

        if cnt >= k:
            return False
        
    if cnt >= k:
        return False
    
    return True
                

def bs(arr, start, end, k):
    mid = (start + end) // 2
    
    if start > end: return end

    if is_possible(mid, deepcopy(arr), k):
        return bs(arr, mid+1, end, k)
    
    return bs(arr, start, mid-1, k)
    
            
def solution(stones, k):
    answer = 0
    
    answer = bs(stones, 0, INF, k)
        
    return answer

 