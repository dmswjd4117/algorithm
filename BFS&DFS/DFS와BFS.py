from collections import deque

N , M , V = map(int, input().split())

# 각 정점에 인접한 정점들 , 인접 리스트
graph = [[] for _ in range(N+1)]
# 방문 했으면 True 방문 안했으면 Fasle
vis = [0] * (N+1)

for i in range(M):
    a, b = map(int ,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1,N+1):
    graph[i].sort()

# dfs
def dfs(v):
    print(v, end=" ")
    vis[v] = True

    for i in graph[v]:
        if not vis[i]:
            dfs(i)


# bfs
def bfs(v):
    temp = deque([])

    answer = [v]
    vis[v] = True

    for i in graph[v]:
        temp.append(i)
        vis[i] = True

    while temp:
        num = temp.popleft()
        vis[num] = True
        answer.append(num)

        for n in graph[num]:
            if vis[n]:
                continue
            vis[n] = True
            temp.append(n)
    
    for i in answer:
        print(i , end=" ")


dfs(V)
print()
vis = [0] * (N+1)
bfs(V)