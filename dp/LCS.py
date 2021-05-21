from collections import deque
from itertools import permutations
import heapq
import  sys 

sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()


INF = int(1e10)

a = [0] + list(input())
b = [0] + list(input())

N = len(a)
M = len(b)

lcs = [
    [0] * (M+1)
    for _ in range(N+1)
]

for i in range(1, N):
    for j in range(1, M):
        if a[i] == b[j]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

# for i in range(len(lcs)):
#     print(lcs[i])

print(lcs[N-1][M-1])