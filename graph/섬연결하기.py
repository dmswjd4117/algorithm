# 1.최소비용신장트리
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x : x[2])
    p = [x for x in range(n)]
    
    def find(x):
        if p[x] == x:
            return x
        p[x] = find(p[x])
        return p[x]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        if a > b:
            p[a] = b
        else:
            p[b] = a
    
    for a, b, cost in costs:
        if find(a) != find(b):
            union(a, b)
            answer += cost
            
    return answer