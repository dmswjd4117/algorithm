from collections import deque
from itertools import permutations
import heapq
import  sys 

sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()
 
INF = int(1e10)
mod = 10007

N, S, M = map(int, input().split())
V = [0] + list(map(int, input().split()))
arr = [
    [False] * (M+1)
    for _ in range(N+1)
]
arr[0][S] = True
def isin(n):
    return 0<=n<=M

for i in range(0, N):
    for j in range(0, M+1):
        if arr[i][j] == False:
            continue
        t = j + V[i+1]
        if isin(t):
            arr[i+1][t] = True

        t = j - V[i+1]
        if isin(t):
            arr[i+1][t] = True

# for i in range(0, N+1):
#     for j in range(0, M+1):
#         if arr[i][j]:
#             print('1', end=' ')
#         else:
#             print(0, end=' ')
#     print()

ans = -1

for i in range(0, M+1):
    if arr[N][i] == True:
        ans = i

print(ans)
