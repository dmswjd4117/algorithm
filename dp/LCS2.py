# https://hjp845.tistory.com/29
# https://www.acmicpc.net/problem/9252

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

ans = [
    [ '0' ] * (M+1)
    for _ in range(N+1)
]


for i in range(1, N):
    for j in range(1, M):
        if a[i] == b[j]:
            lcs[i][j] = lcs[i-1][j-1] + 1
            if ans[i-1][j-1] != '0':
                ans[i][j] = ans[i-1][j-1] + a[i]
            else:
                ans[i][j] = a[i]
        else:
            if lcs[i][j-1] > lcs[i-1][j]:
                lcs[i][j] =  lcs[i][j-1]
                ans[i][j] = ans[i][j-1] 
            else:
                lcs[i][j] =  lcs[i-1][j]
                ans[i][j] = ans[i-1][j]
        
 
if lcs[N-1][M-1] == 0:
    print(lcs[N-1][M-1])
else:
    print(lcs[N-1][M-1])
    print(ans[N-1][M-1])
