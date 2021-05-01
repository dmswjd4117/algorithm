import sys
from collections import deque
import heapq
input = lambda : sys.stdin.readline().rstrip()
MAX = 987654321


M, N = map(int, input().split())
graph = []
vis = [
    [ -1 ] * (M+1)
    for _ in range(N)
]
move = [[0, 1], [1, 0], [-1, 0], [0, -1]]
for i in range(N):
    graph.append(list(map(int, input())))

def isin(x, y):
    return 0 <= x <= N-1 and 0 <= y <= M-1

def go(x, y):
    dq = []
    heapq.heappush(dq, (0, x, y))
    vis[x][y] = 0

    while dq:
        z, x, y = heapq.heappop(dq)

        for i in range(4):
            tx, ty = x + move[i][0], y + move[i][1]
            if not isin(tx, ty): continue
            if vis[tx][ty] != -1: continue

            if graph[tx][ty] == 1:
                vis[tx][ty] = vis[x][y] + 1
                heapq.heappush(dq, (z+1, tx, ty))
            else:
                vis[tx][ty] = vis[x][y]
                heapq.heappush(dq, (z, tx, ty))

go(0, 0)
print(vis[N-1][M-1])