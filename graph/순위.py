# https://programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    answer = 0
    INF = float('inf')
    graph = [
        [INF for _ in range(n+1)]
        for _ in range(n+1)
    ]
    
    for a, b in results:
        graph[a][b] = 1
        
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][k] != INF and graph[k][j] != INF:
                    graph[i][j] = 1
                    
                    
    def check(index):
        res = 0
        for i in range(1, n+1):
            if graph[index][i] != INF:
                res += 1
            if graph[i][index] != INF:
                res += 1
        return res == n-1
    
    
    for i in range(1, n+1):
        if check(i):
            answer += 1
        
        
    return answer



