def solution(info, edges):
    answer = 0
    N = len(info)
    ALL_VISTED = (1 << N)- 1
    graph = [[] for _ in range(N)] 
    cache = [False] * (1 << N)
    
    for a, b in edges:
        graph[a].append(b)
    
    def get_counts(visted):
        s, w = 0, 0
        for i in range(N):
            if not (visted & (1 << i)):
                continue
            if info[i] == 0:
                s += 1
            else:
                w += 1
        return [s, w]        
        
    
    def find(cur, visted):
        nonlocal answer    
        # 이미 방문한 노드라면     
        if visted & (1 << cur):
            return
        visted |= (1 << cur)
        
        # 이미 방문한 경로라면
        if cache[visted]:
            return
        cache[visted] = True
        
        s, w = get_counts(visted)
        # 늑대 수가 양수 보다 많다면 
        if s <= w:
            return
        
        answer = max(answer, s)
        
        for parent in range(N):
            if visted & (1 << parent):
                for child in graph[parent]:
                    find(child, visted)
                    
    find(0, 0)

    return answer

