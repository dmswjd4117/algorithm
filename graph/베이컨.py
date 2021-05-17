import  sys 
import copy
from itertools import permutations
import heapq

f = open("data.txt", 'r')
input = lambda : f.readline().rstrip()

INF = int(1e10)

N, M = map(int, input().split())
graph = [
    [INF] * (N+1)
    for _ in range(N+1)
]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, N+1):
    graph[i][i] = 0 


for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][k] == 0 or graph[k][j] == 0:
                continue
            cost = graph[i][k] + graph[k][j]
            if graph[i][j] > cost:
                graph[i][j] = cost


ans_index = 0
ans_cnt = INF

for i in range(1, N+1):
    hap = 0

    for j in range(1, N+1):
        hap += graph[i][j]

    if ans_cnt > hap:
        ans_cnt = hap
        ans_index = i

print(ans_index)

    
            