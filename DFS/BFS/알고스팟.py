from collections import deque
import sys
sys.setrecursionlimit(10000000)
input = lambda : sys.stdin.readline().rstrip()


f = open("./main.txt", "r")
input = lambda : f.readline().rstrip()

MAX = 100 * 100 + 2
moving = [
    [0 , 1], [1, 0], [-1, 0], [0, -1]
]

graph = []

M, N = map(int, input().split())
for i in range(N):
    graph.append(list(map(int, input())))

check = [
    [ False for _ in range(M)]
    for _ in range(N)
]

dist = [
    [ 0 for _ in range(M)]
    for _ in range(N)
]

dq = deque([])
dq.append((0, 0))
check[0][0] = True
dist[0][0] = graph[0][0]

ans = MAX
while dq:
    x, y = dq.popleft()
    for i in range(4):
        tx, ty = x + moving[i][0] , y + moving[i][1]
        if tx == N-1 and ty == M-1:
            ans = min(ans, dist[x][y] + graph[tx][ty]) 

        if tx < 0 or tx >= N or ty < 0 or ty >= M:
            continue
        if check[tx][ty] :
            if dist[tx][ty] > dist[x][y] + graph[tx][ty]:
                dist[tx][ty] = dist[x][y] + graph[tx][ty]
                dq.append((tx, ty))
        else:
            dist[tx][ty] = dist[x][y] + graph[tx][ty]
            check[tx][ty] = True        
            dq.append((tx, ty))


if ans == MAX:
    print(0)
else:
    print(ans)
