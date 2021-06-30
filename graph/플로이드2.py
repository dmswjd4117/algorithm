# https://www.acmicpc.net/problem/11780
import  sys 
import copy
from itertools import permutations
import heapq

sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()

 
INF = float('inf')

n = int(input())
m = int(input())

graph = [
    [INF] * (n+1)
    for _ in range(n+1)
]

via = [
    [0] * (n+1)
    for _ in range(n+1)
]

for i in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c
 

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                continue
            cost = graph[i][k] + graph[k][j]
            if graph[i][j] > cost:
                graph[i][j] = cost
                via[i][j] = k

 
def p(graph):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == INF:
                print('0', end=' ')
            else:
                print(graph[i][j],end=' ')
        print()
 

 
ans = []
def go(x, y):
 
    if via[x][y] == 0:
        return []

    go(x, via[x][y])

    ans.append(via[x][y])

    go(via[x][y], y)


p(graph)

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0)
            continue

        ans = []
        go(i, j)

        leng = len(ans)
        print(leng+2, i, end=' ')
        for a in ans:
            print(a, end=' ')
        print(j, end=' ')

        print()
