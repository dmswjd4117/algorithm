import sys
import copy
sys.setrecursionlimit(100000)
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
B = []
for i in range(M):
    B.append(list(map(int, input().split())))

for a in range(0, N):
    for i in range(0, K):
        t = 0
        for j in range(0, M):
            t += B[j][i] * A[a][j]
        print(t,end=' ')
    print()