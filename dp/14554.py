from collections import deque
from itertools import permutations
from heapq import *
import  sys 
sys.setrecursionlimit(10**9)
input = lambda : sys.stdin.readline().rstrip()



INF = int(1e8)
mod = 10*9+9

V, E,S,E = map(int, input().split())

edges = [
    [] for _ in range(V+1)
]
for i in range(V):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

dist = [INF] * (V+1)
cnt = [1] * (V+1)

def dikj(start):
    d = deque([])
    d.append((0, start))
    dist[start] = 0

    while d:
        w, x = d.popleft()
        if dist[x] < w:
            continue

        for nw, nx in edges[x]:
            cost = dist[x] + nw
            if dist[nx] == cost:
                cnt[nx] = cnt[x] + 1
            if dist[nx] > cost:
                dist[nx] = cost
                d.append((cost, nx))

                cnt[nx] = cnt[x]

dikj(S)
print(cnt[E])
print(cnt)
# https://hyeonyeee.tistory.com/82