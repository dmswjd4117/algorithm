from collections import deque
from itertools import permutations
import heapq
import  sys 

sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()
 

INF = int(1e10)


v, e = map(int, input().split())
indegree = [0] * (v+1)
graph = [
    [] for _ in range(v+1)
]
for i in range(e):
    a, b = map(int, input().split())
    # a -> b 이동
    graph[a].append(b)
    indegree[b] += 1


def top():
    res = []
    q = []

    for i in range(1, v+1):
        if indegree[i] == 0:
            heapq.heappush(q, i)

    while q:
        now = heapq.heappop(q)
        res.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, i)
                

    return res

res = top()
for a in res:
    print(a, end=' ')

