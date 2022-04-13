# https://www.acmicpc.net/problem/16167

from collections import deque
import sys
import heapq

sys.setrecursionlimit(10**6)

input = lambda : sys.stdin.readline().rstrip()

INF = float('inf')
 

N, R = map(int, input().split())
graph = [
    [] for _ in range(N)
]
for i  in range(R):
    a, b, c, d, e = map(int, input().split())
    a -= 1 
    b -= 1
    value = c
    if e > 10:
        value += (e - 10) * d
    graph[a].append((b, value))


count = [INF] * (N)
cnt = 0

    
def dijkstra(x):
    q = []
    
    vis = set([])
    dist = [INF] * (N)
    
    
    heapq.heappush(q, (0, x))
    dist[x] = 0
    count[x] = 1
    
    while q:
        pr, x = heapq.heappop(q)
        if x in vis:
            continue
        vis.add(x)
        
        for nx, value in graph[x]:
            cost = dist[x] + value
            
            if dist[nx] > cost:
                dist[nx] = cost
                heapq.heappush(q, (cost, nx))
                count[nx] = count[x] + 1
                
            elif dist[nx] == cost:
                if count[nx] > count[x] + 1:
                    count[nx] = count[x] + 1
                    heapq.heappush(q, (cost, nx))
                
                
    return dist[N-1]
     
answer = dijkstra(0)
        
if answer == INF:
    print("It is not a great way.")
else:
    print(answer, count[N-1])
    

    
    