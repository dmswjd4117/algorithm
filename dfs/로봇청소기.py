import sys
from copy import deepcopy as dcpy
from collections import deque
import heapq

INF = float('inf')
sys.setrecursionlimit(10000)

input = lambda : sys.stdin.readline().rstrip()

# f = open("./file.txt", "r")
# input = lambda: f.readline().rstrip()

N, M = map(int, input().split())
r, c, d = map(int, input().split())


graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
vis = [ 
   [False] * (M)
   for _ in range(N)    
]
moving = [
    [-1, 0] , [0, 1] , [1, 0], [0, -1]
]

def check(x, y):
    if graph[x][y] == 1:
        return False
    if vis[x][y]:
        return False
    return True

def nextDir(index):
    if index == 0:
        return 3
    return index-1

 
def isin(x, y):
    return 0 <= x < N and 0 <= y < M

answer = 1
def go(x, y, d, cnt):
    global answer
    
    if cnt == 4:
        nx = x + moving[d][0] * -1 
        ny = y + moving[d][1] * -1 
        
        if not isin(nx, ny):
            return
        
        if graph[nx][ny] != 1:
            go(nx, ny, d, 0)
            
        return 
    
    vis[x][y] = True
    
    nd = nextDir(d)
    nx, ny = x + moving[nd][0], y + moving[nd][1]
    
    if not isin(nx, ny):
        return
    
    if check(nx, ny):
        answer += 1
        go(nx, ny, nd, 0)
    
    else:
        go(x, y, nd, cnt+1)
            
    
go(r, c, d, 0)

print(answer)