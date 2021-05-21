from collections import deque
from itertools import permutations
import heapq
import  sys 

sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()


INF = int(1e10)

N = int(input())
arr = list(map(int, input().split()))
dist = [INF] * (N)

dist[0] = 0
for i in range(N):
    cnt = arr[i]
    for j in range(i+1, i+1+cnt):
        if j >= N: break
        if dist[j] > dist[i] + 1:
            dist[j] = dist[i] + 1

if dist[N-1] == INF:
    print(-1)
else:
    print(dist[N-1])