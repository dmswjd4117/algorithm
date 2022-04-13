# https://www.acmicpc.net/problem/14554
# https://casterian.net/archives/1337

# 어떤 최단 경로 문제든 최단 경로의 개수를 구하는 방법은 똑같습니다. 
# 현재 방문한 꼭짓점 u가 꼭짓점 v와 가중치 w인 변으로 연결되어 있을 때 d(v)>d(u)+w이면 
# d(v)를 d(u)+w로 업데이트하고 c(v)에 c(u)를 대입합니다.
# 물론 동시에 적절히 큐나 우선순위 큐에도 넣어주면 되죠. d(v)=d(u)+w이면 c(v)에 c(u)를 더해주면 됩니다. 
# 여기서 d(v)은 꼭짓점 v까지 가는 최단 거리이고 c(v)는 그 최단 거리의 개수입니다. 
# 시작점 s에서는 당연히 d(s)=0, c(s)=1입니다.

from collections import deque
import sys
import heapq

sys.setrecursionlimit(10**6)

input = lambda : sys.stdin.readline().rstrip()

f = open("./file.txt", "r")
input = lambda: f.readline().rstrip()

INF = float('inf')
MOD = 1000000009

N, M, s, t = map(int, input().split())
s -= 1
t -= 1

graph = [
    [] for _ in range(N)
]
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, c))
    graph[b].append((a, c))

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
                cnt[nx] %= MOD
                heapq.heappush(q, (cost, nx))
                
            elif dist[nx] == cost:
                cnt[nx] += cnt[x]
                cnt[nx] %= MOD
                heapq.heappush(q, (cost, nx))
                
    
    return cnt[end] % MOD
    
 
answer = find(s, t)
print(answer)