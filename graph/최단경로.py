import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()
import heapq

INF = int(1e9)

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

vis = [False] * (V+1)
dist = [INF] * (V+1)

def dijkstra(start):
    q = []

    dist[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        _, cur_node = heapq.heappop(q)
        if vis[cur_node]:continue
        vis[cur_node] = True

        for weight, next_node in graph[cur_node]:
            cost = dist[cur_node]+weight
            if dist[next_node] > cost:
                dist[next_node] = cost
                heapq.heappush(q, (cost, next_node))

dijkstra(K)

for i in range(1, V+1):
    ans = dist[i]
    if ans == INF:print("INF")
    else:print(ans)
