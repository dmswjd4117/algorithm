from collections import deque

moving = [ 
    [-2,-1], [-2, 1], [-1, -2],[1, -2],
    [2, -1], [2, 1], [1, 2], [-1, 2]
]


def find(x1, y1, x2, y2):
    dist = [[-1 for _ in range(n)] for _ in range(n)]

    dq = deque()
    dq.append([x1,y1])
    dist[x1][y1] = 0

    while dq:
        x ,y = dq.popleft()
        
        if x == x2 and y == y2:
            print(dist[x][y])
            return 

        for i in range(8):
            nx = x + moving[i][0]
            ny = y + moving[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: 
                continue
            if dist[nx][ny] != -1 :
                continue

            dq.append([nx, ny])
            dist[nx][ny] = dist[x][y] + 1


T = int(input())

for test in range(T):
    n = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    find(x1, y1, x2, y2)


    