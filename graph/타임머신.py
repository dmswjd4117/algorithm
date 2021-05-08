import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

INF = 987654321

class edge:
    def __init__(self):
        self.From = ''
        self.to = ''
        self.cost = 0

N, M = map(int, input().split())

a = [edge() for _ in range(M)] 
for i in range(M):
    a[i].From, a[i].to, a[i].cost = map(int, input().split())

dist = [INF] * (N+1)
dist[1] = 0

negative = False
for i in range(1, N+1):
    for j in range(M):
        x, y, z = a[j].From, a[j].to, a[j].cost
        if dist[x] != INF and dist[y] > dist[x] + z:
            dist[y] = dist[x] + z
            if i == N:
                negative = True
        
if negative: print(-1)
else:
    for i in range(2, N+1):
        if dist[i] == INF:dist[i] = -1
        print(dist[i])
