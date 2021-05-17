# 벨만포드1 
# o(VE)

import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

INF = 987654321

class edge:
    def __init__(self):
        self.From = ''
        self.to = ''
        self.cost = 0

N, M = map(int, input().split())

a = [edge() for _ in range(M)] 
for i in range(M):
    a[i].From, a[i].to, a[i].cost = map(int, input().split())

dist = [INF] * (N+1)
dist[1] = 0

negative = False
for i in range(1, N+1):
    for j in range(M):
        x, y, z = a[j].From, a[j].to, a[j].cost
        if dist[x] != INF and dist[y] > dist[x] + z:
            dist[y] = dist[x] + z
            if i == N:
                negative = True
        
if negative: print(-1)
else:
    for i in range(2, N+1):
        if dist[i] == INF:dist[i] = -1
        print(dist[i])

# 벨만포드2
# o(VE)

import  sys 

sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()

INF = int(1e10)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
dist = [INF] * (N+1)

dist[1] = 0

NEG = False

# 모든 엣지에 대해 (노드수-1) 만큼의 edge relation
for k in range(1, N+1):
    # a노드->b노드 vs b원래 거리
    for a in range(1, N+1):
        for i in range(len(graph[a])):
            weight, b = graph[a][i]
            cost = dist[a] + weight
            if dist[a] != INF and dist[b] > cost:
                dist[b] = cost
                if k == N: NEG = True

if NEG:
    print(-1)
else:
    for i in range(2, N+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])

# SPFA

from collections import deque
import  sys 

sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()

INF = int(1e10)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

dist = [INF] * (N+1)
cnt = [0] * (N+1)
vis = [False] * (N+1)
dq = deque([])


def spfa(start):
    
    dq.append(start)
    dist[start] = 0
    vis[start] = True


    while dq:
        fr = dq.popleft()
        vis[fr] = False
        for weight, to in graph[fr]:
            cost = dist[fr] + weight
            if dist[to] > cost:
                dist[to] = cost
                if vis[to] == False:
                    vis[to] = True
                    dq.append(to)
                    cnt[to] += 1
                    if cnt[to] >= N:
                        return False

    return True


if not spfa(1):
    print(-1)
else:
    for i in range(2, N+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])

