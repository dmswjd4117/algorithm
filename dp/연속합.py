from math import floor, log2
from operator import index
import sys
from collections import deque
sys.setrecursionlimit(100000)

input = lambda : sys.stdin.readline().rstrip()
 
INF = float('inf')
MAX_NODE = 50_002
MAX_LEVEL = floor(log2(MAX_NODE))

 

N = int(input())
m = list(map(int, input().split()))

dp = [0] * (N)
 
dp[0] = m[0]
for i in range(1, N):
    dp[i] = max(dp[i-1] + m[i], m[i])

 

print(max(dp))
