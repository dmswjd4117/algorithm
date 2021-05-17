from collections import deque
from itertools import permutations
import heapq
import  sys 

sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()


INF = int(1e8)
N, E = map(int, input().split())
edges = [[] for _ in range(N+1)]

for i in range(E):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

V1, V2 = map(int, input().split())

def dik(start):
    dist = [INF] * (N+1)
    heap = []
    heapq.heappush(heap, (0, start))
    dist[start] = 0

    while heap:
        weight, cur = heapq.heappop(heap)
        if dist[cur] < weight:
            continue
        for c, b in edges[cur]:
            cost = dist[cur] + c
            if dist[b] > cost:
                dist[b] = cost
                heapq.heappush(heap, (cost, b))

    return dist



from1 = dik(1)
fromV1 = dik(V1)
fromV2 = dik(V2)

ans = min(
    from1[V1]+fromV1[V2]+fromV2[N],
    from1[V2]+fromV2[V1]+fromV1[N]
)

if ans >= INF:
    print(-1)
else:
    print(ans)