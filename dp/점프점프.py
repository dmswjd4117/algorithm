from math import floor, log2
from operator import index
import sys
from collections import deque
sys.setrecursionlimit(10000)

input = lambda : sys.stdin.readline().rstrip()
 
INF = float('inf')
MAX_NODE = 50_002
MAX_LEVEL = floor(log2(MAX_NODE))
 
N = int(input())
arr = [0] + list(map(int, input().split()))

dp = [INF] * (N+1)
dp[1] = 0

for i in range(1, N+1):
    for j in range(1, i):
        if i <= j + arr[j]:
            dp[i] = min(dp[i], dp[j]+1)

if dp[N] == INF:
    print(-1)
else:
    print(dp[N])
