import sys
from collections import deque
import heapq
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
vis = [False] * (N+1)
ans = 987654321

def go(index, start, cur, hap):
    global ans
    if index == N-1:
        if graph[cur][start] != 0:
            ans = min(ans, hap+graph[cur][start])
        return 

    for i in range(N):
        if graph[cur][i] == 0: continue
        if vis[i] != False: continue
        vis[i] = True
        go(index+1, start, i, hap+graph[cur][i])
        vis[i] = False

for i in range(N):
    vis[i] = True
    go(0, i, i, 0)

print(ans)