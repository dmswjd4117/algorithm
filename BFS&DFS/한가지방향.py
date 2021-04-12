from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

f = open("./main.txt", "r")
input = lambda: f.readline().rstrip()

T = int(input())
for _ in range(T):
    N= int(input())
    graph = []
    vis = [
        [0] * N
        for _ in range(N)
    ]

    for i in range(N):
        graph.append(list(map(int, input().split())))
    WALL = 1

    move = [
        [0, 1], [1, 0], [0, -1], [-1, 0]
    ]
    TURN = 5
    def go(x, y, d):
        if x == N-1 and y == N-1:
            return True
        
        if vis[x][y] == TURN:
            return False

        tx, ty = x+move[d][0], y +move[d][1]
        if 0<=tx<N and 0<=ty<N and graph[tx][ty] != WALL:
            if vis[tx][ty] == 0: vis[tx][ty] = 3
            return go(tx, ty, d)


        vis[x][y] = TURN
        for i in range(4):
            tx, ty = x +move[i][0], y+move[i][1]
            if 0<=tx<N and 0<=ty<N and graph[tx][ty] != WALL:
                if vis[tx][ty] == 0: vis[tx][ty] = 3
                if go(tx, ty, i):return True
        return False 
        
    x,y = 0,0
    if go(x, y, 0) or go(x, y, 1):
        print("YES")
    else:
        print("NO")

    for i in vis:
        print(" ".join(map(str, i)))
        print()