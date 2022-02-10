# https://www.acmicpc.net/problem/1956

import sys

input = lambda : sys.stdin.readline().rstrip()
 


INF = float('inf')

N, M = map(int, input().split())

q = []
graph = [
    [INF for _ in range(N+1)]
    for _ in range(N+1)
]

for i in range(M):
    a, b, v = map(int, input().split())
    graph[a][b] = v

for i in range(1, N+1):
    graph[i][i] = 0

for k in range(N):
    for i in range(1, N+1):
        for j in range(1, N+1):
            value = graph[i][k] + graph[k][j]
            if value < graph[i][j]:
                graph[i][j] = value


def print_graph():
    for i in range(1, N+1):
        for j in range(1, N+1):
            print(graph[i][j], end=' ')
        print()

answer = INF
for a in range(1, N+1):
    for b in range(a+1, N+1):
        temp = graph[a][b] + graph[b][a]
        answer = min(answer, temp)

if answer == INF:
    print(-1)
else:
    print(answer)

    