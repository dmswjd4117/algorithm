from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

f = open("./main.txt", "r")
input = lambda: f.readline().rstrip()


TEST = int(input())
for _ in range(TEST):
    N = int(input())
    graph = []
    vis = [
        [False] * N
        for _ in range(N)
    ]
    for i in range(N):
        graph.append(list(map(int,input().split())))

    K = int(input())

    move = [
        [0,1],[1,0],[0,-1],[-1,0]
    ]

    res = 0

    def go(x,y,cnt):
        global res
        if x == N-1 and y == N-1:
            if cnt <= K: res += 1

        vis[x][y] = True

        for i in range(4):
            tx,ty = x+move[i][0],y+move[i][1]
            if tx<0 or ty<0 or tx>=N or ty>=N:continue
            if vis[tx][ty]: continue
            if graph[tx][ty] == 1:continue

            go(tx, ty, cnt+1)

        vis[x][y] = False


    go(0,0,0)
    print(res)