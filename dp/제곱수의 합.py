from math import floor, log2
from operator import index
import sys
from collections import deque
sys.setrecursionlimit(100000)

input = lambda : sys.stdin.readline().rstrip()
 
INF = float('inf')
 
N = int(input())

dp = [INF for _ in range(N+1)]

dp[0] = 0
for i in range(1, N+1):
    index = 1
    while True:
        a = index * index 
        if a > i: break
        if dp[i] > dp[i-a] + 1:
            dp[i] = dp[i-a] + 1
        index += 1

 
print(dp[N])