from collections import deque
from itertools import permutations
import heapq
import  sys 

sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()

INF = int(1e10)
mod = 9901

N = int(input())
arr = [
    [0] * (4)
    for _ in range(N+1)
]
arr[1][1], arr[1][2], arr[1][3] = 1, 1, 1

for i in range(2, N+1):
    arr[i][1] = (arr[i-1][2] + arr[i-1][3]) % mod
    arr[i][2] = (arr[i-1][1] + arr[i-1][3]) % mod
    arr[i][3] = (arr[i-1][1] + arr[i-1][2] + arr[i-1][3]) % mod

print((sum(arr[N]))%mod)