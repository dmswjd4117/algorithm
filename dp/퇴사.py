# 1
from math import floor, log2
import sys
from collections import deque
sys.setrecursionlimit(100000)

input = lambda : sys.stdin.readline().rstrip()
 
INF = float('inf')
MAX_NODE = 50_002
MAX_LEVEL = floor(log2(MAX_NODE))

f = open("./file.txt", "r")
input = lambda: f.readline().rstrip()


N = int(input())

time = [0] * (N+1)
m = [0] * (N+1)
dp = [0] * (N+2)

for i in range(1, N+1):
    a, b = map(int, input().split())
    time[i] = a
    m[i] = b
    dp[i] = b

for i in range(1, N+1):
    for n in range(1, i):
        temp = n + time[n]
        if temp <= i:
            dp[i] = max(dp[i], m[i] +  dp[n])
            

 

answer = 0
for i in range(1, N+1):
    if i + time[i] <= N+1:
        answer = max(answer, dp[i])

print(answer)


# 2

from math import floor, log2
import sys
from collections import deque
sys.setrecursionlimit(100000)

input = lambda : sys.stdin.readline().rstrip()
 
INF = float('inf')
MAX_NODE = 50_002
MAX_LEVEL = floor(log2(MAX_NODE))

 
N = int(input())

time = [0] * (N+1)
m = [0] * (N+1)
dp = [0] * (N+2)

for i in range(1, N+1):
    a, b = map(int, input().split())
    time[i] = a
    m[i] = b
    

for i in range(N, 0, -1):
 
    if i + time[i] > N + 1: 
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], m[i] + dp[i+time[i]])
 
print(max(dp))

