# 플로이드 와샬
INF = float('inf')

def solution(n, s, a, b, fares):
    answer = 0
    graph = [
        [INF for _ in range(n+1)] 
        for _ in range(n+1)
    ]
    for i in range(n+1):
        graph[i][i] = 0
        
    for aNode, bNode, cost in fares:
        graph[aNode][bNode] = cost
        graph[bNode][aNode] = cost

        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                cost = graph[i][k] + graph[k][j]
                if graph[i][j] > cost:
                    graph[i][j] = cost
                    
    
    answer = graph[s][a] + graph[s][b]
    for i in range(1, n+1):
        answer = min(answer, graph[s][i]+graph[i][a]+graph[i][b])
        
                    
    return answer


# 다익스트라 알고리즘

import heapq

INF = float('inf')

def solution(n, s, A, B, fares):
    answer = INF
    
    graph = [
        [] for _ in range(n+1)
    ]
    
    
    for a, b, cost in fares:
        graph[a].append((cost, b))
        graph[b].append((cost, a))
        
    def dijk(start):
        q = []
        vis = set([])
        dist = [INF] * (n+1)
        
        dist[start] = 0
        heapq.heappush(q, (0, start))
        
        while q:
            cost, x = heapq.heappop(q)
            if x in vis:
                continue
            vis.add(x)
            for nc, nx in graph[x]:
                value = dist[x] + nc
                if value < dist[nx]:
                    dist[nx] = value
                    heapq.heappush(q, (value, nx))
                    
        return dist
        
    dist = dijk(s)
    
    for i in range(1, n+1):
        temp = dijk(i)
        res = dist[i] + temp[A] + temp[B]
        answer = min(answer, res)
        
    return answer






