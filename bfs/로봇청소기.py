 
import sys
 
from collections import deque
from itertools import permutations
sys.setrecursionlimit(10000)

input = lambda : sys.stdin.readline().rstrip()

 
INF = float('inf')
moving = [ [0, 1], [1, 0], [-1, 0], [0, -1] ]

while True:
    M, N = map(int, input().split())
    if not M and not N:
        break
    
    graph = []
    loc = [()]
    for i in range(N):
        graph.append(list(input()))
        for j in range(M):
            if graph[i][j] == 'o':
                loc[0] = (i, j)
            if graph[i][j] == '*':
                loc.append((i, j))  

    def isin(x, y):
        return 0 <= x < N and 0 <= y < M

    def bfs(start, end):
        vis = [ 
            [False] * (M+1)
            for _ in range(N+1)
        ]
        arr = [
            [0] * (M+1)
            for _ in range(N+1)
        ]
        
        dq = deque([])
        dq.append(start)
        arr[start[0]][start[1]] = 0
        
        while dq:
            x, y = dq.popleft()
            if vis[x][y]:
                continue
            if x == end[0] and y == end[1]:
                return arr[x][y]
            vis[x][y] = True
            
            for i in range(4):
                nx, ny = x + moving[i][0], y + moving[i][1]
                if not isin(nx, ny):
                    continue
                if graph[nx][ny] == 'x':
                    continue
                dq.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1
        
        return False
                

    cnt = len(loc)
    dist = [
        [0] * (cnt)
        for _ in range(cnt)
    ]
    

    blocked = False
    for i in range(cnt):
        for j in range(cnt):
            if i == j: continue
            dist[i][j] = bfs(loc[i], loc[j])
            if not dist[i][j]:
                blocked = True
        if blocked: break
                    
    
    if blocked: 
        print(-1)
        
    elif cnt == 1:
        print(0)
        
    else:
        answer = INF
        nums = [ x for x in range(1, cnt)]
        for perm in permutations(nums):
            fr = 0
            to = perm[0]
            temp = dist[fr][to]
            for i in range(0, len(perm)-1):
                fr = perm[i]
                to = perm[i+1]
                temp += dist[fr][to]
            answer = min(answer, temp)
            
            
        print(answer)
                    
