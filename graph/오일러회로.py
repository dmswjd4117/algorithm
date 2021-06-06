from collections import deque
from itertools import permutations
from heapq import *
import  sys 
sys.setrecursionlimit(10**9)
input = lambda : sys.stdin.readline().rstrip()

 

INF = int(1e10)
mod = 10007

N = int(input())


graph = []
diction = {}
ind = [0] * (N)

for i in range(N):
    diction[i] = []


for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        for k in range(graph[i][j]):
            ind[i] += 1
            diction[i].append(j)


for i in range(0, N):
    if ind[i] % 2 != 0:
        print(-1)
        exit(0)


def go(node):
    for i in diction[node]:
        while graph[node][i]:
            graph[node][i] -= 1
            graph[i][node] -= 1
            go(i)
    
    print(node+1,end=' ')

go(0)