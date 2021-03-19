from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))


dq = deque([])
dist = [[-1 for _ in range(1000)] for _ in range(1000)]
check = [[ False for _ in range(1000)] for _ in range(1000)]


moving = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def find():
    dq.append([0,0])
    dist[0][0] = 1
    check[0][0] = True

    while dq:
        x, y = dq.pop()
        for i in range(4):
            nx = x + moving[i][0]
            ny = y + moving[i][1]
            if( nx < 0 or  nx >= N or  ny < 0 or ny >= M):
                continue
            if(check[nx][ny] == False and graph[nx][ny] == 1):
                check[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                dq.append([nx, ny])
            

find()
print(dist[N-1][M-1])
