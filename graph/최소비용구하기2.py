import  sys 
import copy
from itertools import permutations
import heapq

sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()


INF = int(1e10)

N = int(input())
M = int(input())
edges = [[] for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    a ,b = a-1, b-1
    edges[a].append((c, b))

start, end = map(int ,input().split())
start, end = start-1, end-1

dist = [INF] * (N)
via = [x for x in range(N)]

ans = []
def find(x):
    global cnt
    if via[x] == x:
        ans.append(x)
        return 

    find(via[x]) 
    ans.append(x)


def dik(start):
    global index
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        cur_w, cur_node = heapq.heappop(q)
        if dist[cur_node] < cur_w: continue
        for i in range(len(edges[cur_node])):
            w, next_node = edges[cur_node][i]
            cost = w + dist[cur_node]
            if dist[next_node] > cost:
                dist[next_node] = cost
                via[next_node] = cur_node
                heapq.heappush(q, (cost, next_node))

dik(start)

print(dist[end])
find(end)
print(len(ans))
for a in ans:
    print(a+1, end=' ')