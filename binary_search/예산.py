import sys
from collections import deque
 
INF = float('inf')

input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(1000000)
 

n = int(input())

arr = list(map(int, input().split()))

m = int(input())

def cal(num):
    res = 0
    for money in arr:
        if money <= num:
            res += money
        else:
            res += num
    return res

def check(num):

    if cal(num) > m:
        return False
    
    return True

def find(start, end):
   
    if start > end:
        max_n = 0
        for i in range(n):
            temp = arr[i]
            if arr[i] <= end:
                temp = arr[i]
            else:
                temp = end
            if max_n < temp:
                max_n = temp
        print(max_n)
        return
    
    mid = (start+end)//2
   

    if not check(mid):
        return find(start, mid-1) 

    return find(mid+1, end) 

find(0, m)
 
