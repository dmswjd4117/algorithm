vis = [-1] * (202)

def go(index, n, graph):
    if vis[index] != -1:
        return False
    
    vis[index] = 1
    for j in range(n):
        if graph[index][j] == 1:
            go(j, n, graph)
        
    return True
    
def solution(n, coms):
    answer = 0

    for i in range(0, n):
        if go(i, n, coms):
            answer += 1
            
    return answer


# 2 
vis = [-1] * (202)
graph = [[] for _ in range(202)]

def go(index):
    if vis[index] != -1:
        return False
    
    vis[index] = 1
    for nindex in graph[index]:
        go(nindex)
        
    return True
    
def solution(n, coms):
    answer = 0
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if coms[i][j] == 1:
                graph[i].append(j)
    
    for i in range(0, n):
        if go(i):
            answer += 1
            
    return answer