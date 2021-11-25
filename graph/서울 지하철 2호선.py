# 1

import sys
from collections import deque
from copy import deepcopy as dcpy
 
import heapq
INF = float('inf')

input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(1000000)
 
n = int(input())

graph = [
    [] for _ in range(n+1)
]

vis = [False] * (n+1)
p = [x for x in range(n+1)]
via = [x for x in range(n+1)]

cycle = set([])
check = set([])

def find(x):
    if x == p[x]:
        return x
    p[x] = find(p[x])
    return p[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        via[b] = a
        p[a] = p[b]
    else:
        p[b] = p[a]

def find_cyc(x, end, S):
    if x in check:
        return
    check.add(x)

    global cycle
    S.add(x)

    if x == end:
        for ele in S:
            cycle.add(ele)
        return

    for nx in graph[x]:
        find_cyc(nx, end, S)

    S.remove(x)

def bfs(start):
    dq = deque([])

    vis = [False] * (n+1)
    dq.append((0, start))

    while dq:
        cost, x = dq.popleft()
        
        if vis[x]: continue
        vis[x] = True

        if x in cycle:
            return cost

        for nx in graph[x]:
            dq.append((cost+1, nx))

for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    if find(a) == find(b):
        find_cyc(a, b, set([]))
    else:
        union(a, b)

for i in range(1, n+1):
    res = bfs(i)
    print(res,end=' ')
 
        

# 2 

import sys
from collections import deque
 
INF = float('inf')

input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(1000000)
 

n = int(input())
cycle = set([])
graph = [
    [] for _ in range(n+1)
]
check = set([])

def find(pre, now, S):
    global cycle
    S.add(now)

    for nx in graph[now]:
        if nx in check and pre != nx:
            for ele in S:
                cycle.add(ele)
            return True 
        if nx in check:
            continue
        check.add(nx)
        find(now, nx, S)

    S.remove(now)

def bfs(start):
    dq = deque([])

    vis = [False] * (n+1)
    dq.append((0, start))

    while dq:
        cost, x = dq.popleft()
        
        if vis[x]: continue
        vis[x] = True

        if x in cycle:
            return cost

        for nx in graph[x]:
            dq.append((cost+1, nx))



for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

find(1, 1, set([]))
 

for i in range(1, n+1):
    res = bfs(i)
    print(res,end=' ')
        

 