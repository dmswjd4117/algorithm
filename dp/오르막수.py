from collections import deque
from itertools import permutations
import heapq
import  sys 

sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()


INF = int(1e10)
mod = 10007

N = int(input())
N = 1
arr = [
    [0] * (10)
    for i in range(N+1)
]

for i in range(10):
    arr[1][i] = 1

#             0 부터 시작 ㄴㄴ -> arr[-1] xx
for i in range(2, N+1): 
    for j in range(0, 10):
        for k in range(0, j+1):
            arr[i][j] += arr[i-1][k] 
            arr[i][j] %= mod


ans = 0
for i in range(10):
    ans += arr[N][i] 
    ans %= mod

print(ans)
