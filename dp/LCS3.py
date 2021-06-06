from collections import deque
from itertools import permutations
import heapq
import  sys 

sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()

 

INF = int(1e10)
mod = 10007


a = list(input())
b = list(input())
c = list(input()) 
N, M, K = len(a), len(b), len(c)

d = [
    [[0] * (K+1) for _ in range(M+1)]  
    for _ in range(N+1)
]


for i in range(1, N+1):
    for j in range(1, M+1):
        for k in range(1, K+1):
            if a[i-1] == b[j-1] == c[k-1]:
                d[i][j][k] = d[i-1][j-1][k-1]+1
            else:
                d[i][j][k] = max(d[i-1][j][k], d[i][j-1][k] )
                d[i][j][k] = max(d[i][j][k],  d[i][j][k-1])


print(d[N][M][K])
