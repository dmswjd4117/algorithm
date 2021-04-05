import copy
import heapq
import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())

arr = []
dq = deque([])
water = [[0]*M for _ in range(N)]
vis = [[0]*M for _ in range(N)]

K = []
B = []

for i in range(N):
    arr.append(list(input()))
    for j in range(M):
        if arr[i][j] == '*':
            dq.append((i, j))
            water[i][j] = 1
        elif arr[i][j] == 'S':
            K.append((i, j))
        elif arr[i][j] == 'D':
            B.append((i, j))

move = [
    [1,0],[0,1],[-1,0],[0,-1]
]

while dq:
    x, y = dq.popleft()
    for i in range(4):
        tx,ty = x+move[i][0],y+move[i][1]
        if tx<0 or ty<0 or tx>=N or ty>=M:
            continue
        if arr[tx][ty] == 'S' or arr[tx][ty] == 'D' or arr[tx][ty] == 'X':
            continue
        if water[tx][ty]: 
            continue

        water[tx][ty] = water[x][y] + 1
        dq.append((tx, ty))


dq = deque([])

dq.append(K[0])
vis[K[0][0]][K[0][1]] = 1

while dq:
    x, y = dq.popleft()
    
    if x == B[0][0] and y == B[0][1]:
        print(vis[x][y]-1)
        break

    for i in range(4):
        tx,ty = x+move[i][0],y+move[i][1]
        if tx<0 or ty<0 or tx>=N or ty>=M:
            continue
        if vis[tx][ty]: 
            continue
        if arr[tx][ty] == 'X':
            continue
        if water[tx][ty] != 0 and water[tx][ty] <= vis[x][y] + 1:
            continue

        vis[tx][ty] = vis[x][y] + 1
        dq.append((tx, ty))

        # for i in range(N):
        #     for j in range(M):
        #         print(vis[i][j],end=' ')
        #     print()
        # print()

else:
    print("KAKTUS")