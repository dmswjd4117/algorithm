# https://www.baeldung.com/cs/graph-number-of-shortest-paths

from collections import deque
import sys
import heapq

sys.setrecursionlimit(10**6)

input = lambda : sys.stdin.readline().rstrip()

f = open("./file.txt", "r")
input = lambda: f.readline().rstrip()

INF = float('inf')
 

N, M = map(int, input().split())
graph = [
    [] for _ in range(N)
]
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def find(x, end):
    q = []
    vis = set([])
    cnt = [1] * (N)
    dist = [INF] * (N+1)
    
    dist[x] = 0
    heapq.heappush(q, (0, x))
    
    while q:
        pr, x = heapq.heappop(q)
        if x in vis:continue
        vis.add(x)
        
        for nx, value in graph[x]:
            cost = dist[x] + value
            if dist[nx] > cost:
                dist[nx] = cost
                cnt[nx] = cnt[x]
                heapq.heappush(q, (cost, nx))
                
            elif dist[nx] == cost:
                cnt[nx] += cnt[x]
                heapq.heappush(q, (cost, nx))
                
    print(dist)
    print(cnt)
    
    print(dist[end])
    
    return cnt[end]
    
s, t = map(int, input().split())
answer = find(s, t)
print(answer)