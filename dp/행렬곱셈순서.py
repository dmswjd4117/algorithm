from collections import deque
from itertools import permutations
import heapq
import  sys 

sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()


INF = int(1e10)

N = int(input())
p = [[]]
for i in range(N):
    r, c = map(int,input().split())
    p.append((r,c))


m = [
    [0] * (501)
    for _ in range(501)
]

for r in range(1, N):
    for i in range(1, N-r+1):
        j = i + r
        m[i][j] = m[i+1][j] + p[i][0] * p[i][1] * p[j][1]
        for k in range(i+1, j):
            m[i][j] = min(m[i][j], m[i][k] + m[k+1][j] + p[i][0] * p[k][1] * p[j][1])

print(m[1][N])

