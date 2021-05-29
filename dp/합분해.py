from collections import deque
from itertools import permutations
import heapq
import  sys 

sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()

 

INF = int(1e10)
mod = int(1e9)

N, K = map(int, input().split())

arr = [
    [0] * (N+1)
    for _ in range(K+1)
]

for i in range(0, N+1):
    arr[1][i] = 1

for i in range(1, K+1):
    for j in range(0, N+1):
        for l in range(0, j+1):
            arr[i][j] += arr[i-1][l] % mod


 
print(arr[K][N] % mod)