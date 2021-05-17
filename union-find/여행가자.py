from collections import deque
from itertools import permutations
import heapq
import  sys 

sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()

INF = int(1e8)

N = int(input())
M = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

city = list(map(int, input().split()))

for i in range(M):
    city[i] -= 1
ps = [x for x in range(N)]

def find(x):
    if x == ps[x]:
        return x
    ps[x] = find(ps[x])
    return ps[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        ps[a] = b
    else:
        ps[b] = a


for i in range(N):
    for j in range(i, N):
        if graph[i][j] == 1:
            union(i, j)

parent = find(city[0])
for c in city:
    if parent != find(c):
        print("NO")
        break
else:
    print("YES")


from collections import deque
from itertools import permutations
import heapq
import  sys 

sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()

f = open("data.txt", 'r')
input = lambda : f.readline().rstrip()

INF = int(1e8)

N = int(input())
M = int(input())

graph = [
    [0] * (N+1)
    for _ in range(N+1)
]

for i in range(1, N+1):
    temp = list(map(int,input().split()))
    for j in range(1, N+1):
        graph[i][j] = temp[j-1]
    

city = list(map(int, input().split()))
vis = [False] * (N+1)

def bfs(start):
    dq = deque([start])
    
    while dq:
        x = dq.popleft()
        vis[x] = True

        for j in range(1, N+1):
            if graph[x][j] == 1 and vis[j] == False:
                dq.append(j)
        

bfs(city[0])

for i in range(1, M):
    if vis[city[i]] == False:
        print('NO')
        break
else:
    print('YES')

