from collections import deque
from itertools import permutations
import heapq
import  sys 

sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()

INF = int(1e10)
mod = 10007

N, K = map(int, input().split())
d = [
    [0] * (K+1)
    for _ in range(N+1)
]
arr = [0]
for i in range(N):
    w, v = map(int, input().split())
    arr.append((w, v))

for i in range(1, N+1):
    for j in range(1, K+1):
        weight, value = arr[i][0], arr[i][1]
        if j < weight:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], value+d[i-1][j-weight])
        
    
print(d[N][K])
