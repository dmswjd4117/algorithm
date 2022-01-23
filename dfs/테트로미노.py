# https://www.acmicpc.net/problem/14500
# pypy 
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()


f = open("./file.txt", "r")
input = lambda: f.readline().rstrip()

moving = [
    [1, 0], [0, 1], [-1, 0], [0, -1]
]

tetro_five = [
    [[0, 0], [-1, 0], [0, -1], [0, 1]],
    [[0, 0], [-1, 0], [1, 0], [0, 1]],
    [[0, 0], [0, -1], [0, 1],[1, 0]],
    [[0, 0], [0, -1], [-1, 0], [1, 0]]
]

n, m = map(int, input().split())
graph = []
vis = [
    [False for _ in range(m)]  
    for _ in range(n)
]
answer = 0

for i in range(n):
    graph.append(list(map(int ,input().split())))

def isin(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False


def go(x, y, cnt, hap):
    global answer
    if cnt == 4:
        answer = max(answer, hap)
        # print(hap, temp)
        return hap

    for move in moving:
        nx, ny = x + move[0], y + move[1]
        if not isin(nx, ny):
            continue
        if vis[nx][ny]:
            continue
        vis[nx][ny] = True
        go(nx, ny, cnt+1, hap+graph[nx][ny])
        vis[nx][ny] = False
 
 
def go_five(x, y):
    global answer
    res = 0

    for rotate in range(4):
        hap = 0
 
        for move in tetro_five[rotate]:
            tx = x + move[0]
            ty = y + move[1]
            if not isin(tx, ty): break 
            hap += graph[tx][ty]
 
        else:
            res = max(res, hap)
 
    answer = max(answer, res)

 

for i in range(n):
    for j in range(m):
        go(i, j, 0, 0)
        # ㅗ
        go_five(i, j)



print(answer)