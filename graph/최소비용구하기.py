# 1
import sys
import heapq
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

INF = int(1e9)

V = int(input())
E = int(input())

graph = [[] for _ in range(V+1)]
vis = [False] * (V+1)
dist = [INF] * (V+1)

for i in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((w, v))

start, end = map(int, input().split())


def dijlstra(start, end):
    q = []

    dist[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        cur_node = heapq.heappop(q)[1]

        if vis[cur_node]: continue
        vis[cur_node] = True

        for weight, next_node in graph[cur_node]:
            cost = dist[cur_node] + weight

            if dist[next_node] > cost:
                dist[next_node] = cost
                heapq.heappush(q, (cost, next_node))

                 
dijlstra(start, end)

print(dist[end])

# 2 
import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

INF = int(1e9)

V = int(input())
E = int(input())

graph = [[] for _ in range(V+1)]
vis = [False] * (V+1)
dist = [INF] * (V+1)

for i in range(E):
    u,v,w = map(int, input().split())
    for j in range(len(graph[u])):
        origin_w, origin_v = graph[u][j][0], graph[u][j][1]
        if v == origin_v and origin_w < w:
            break
    else:
        graph[u].append((w, v))


start, end = map(int, input().split())

def getSmallNode():
    min_value = INF
    index = 0
    for i in range(1, V+1):
        if vis[i]: continue
        if min_value > dist[i]:
            index = i
            min_value = dist[i]
    return index

def dijlstra(start, end):

    vis[start] = True
    dist[start] = 0
    for w, v in graph[start]:
        dist[v] = w
    
    for i in range(V-2): 
        now = getSmallNode()
        vis[now] = True


        for w, v in graph[now]:
            if vis[v]: continue
            if dist[v] > dist[now] + w:
                dist[v] = dist[now] + w

dijlstra(start, end)

print(dist[end])