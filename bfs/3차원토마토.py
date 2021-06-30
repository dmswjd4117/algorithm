from collections import deque
from itertools import permutations
from heapq import *
import  sys 
sys.setrecursionlimit(10**9)
input = lambda : sys.stdin.readline().rstrip()


INF = int(1e8)
mod = 10*9+9
NOT_VIS = -10
 

M, N, H = map(int, input().split())

graph = [
    [[0  for _ in range(H) ] for _ in range(M)]
    for _ in range(N)
]


arr = []
for h in range(H):
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(M):
            graph[i][j][h] = temp[j]
            if graph[i][j][h] == 1:
                arr.append((i, j, h))


def printf(graph):
    for h in range(H):
        for i in range(N):
            for j in range(M):
                print(graph[i][j][h],end=' ')
            print()
        print()
    print()

def isin(x, y, z):
    return (0<=x<N) and (0<=y<M) and (0<=z<H)

move = [
    [1,0,0],[0,1,0],[-1,0,0],[0,-1,0],
    [0,0,1],[0,0,-1]
]

def go(arr):
 
    dq = deque([])
    
    for x, y, z in arr:
        dq.append((x, y, z))
        graph[x][y][z] = 1

    while dq:
        x, y, z = dq.popleft()    

        for i in range(len(move)):
            nx,ny,nz = x+move[i][0], y+move[i][1], z+move[i][2]
            if not isin(nx,ny,nz):
                continue
            if graph[nx][ny][nz] != 0:
                continue

            graph[nx][ny][nz] = graph[x][y][z] + 1 
            dq.append((nx, ny, nz))

 
go(arr)

ans = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            # 토마토인데 방문하지 않았다면, 익지않았다는 뜻
            if graph[i][j][h] == 0: 
                print(-1)
                exit(0)
            ans = max(ans, graph[i][j][h])

print(ans-1)