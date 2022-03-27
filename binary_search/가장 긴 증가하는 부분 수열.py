# https://www.acmicpc.net/problem/12015

import sys
 
from collections import deque
from itertools import permutations
import heapq

sys.setrecursionlimit(10000)

input = lambda : sys.stdin.readline().rstrip()
 
INF = float('inf')

def lower_bound(arr, l, r, key):
    while l < r:
        m = (l + r) // 2
        if arr[m] < key:
            l = m + 1
        else:
            r = m
    return r


N = int(input())
arr = list(map(int, input().split()))

subs = [INF] * (N+1)
cnt = 0
for i in range(N):
    a = lower_bound(subs, 0, N, arr[i])
    subs[a] = arr[i]
    
answer = 1
for i in range(N):
    if subs[i] == INF:
        answer = i
        break
else:
    print(N)
    exit(0)
    
print(answer)
 