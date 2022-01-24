from math import floor, log2
import sys
sys.setrecursionlimit(100000)

input = lambda : sys.stdin.readline().rstrip()
 
INF = float('inf')
MAX_NODE = 50_002
MAX_LEVEL = floor(log2(MAX_NODE))

 

N = int(input())

ps = [
    [0 for _ in range(20)]
    for _ in range(MAX_NODE)
]
parent = [0] * (N+1)
depth = [0] * (N+1)
vis = set([])
graph = [
    [] for _ in range(N+1)
]
arr = []
dis = [0] * (N+1)
for i in range(N-1):
    a, b, v = map(int, input().split())
    graph[a].append((b, v))
    graph[b].append((a, v))

M = int(input())

for i in range(M):
    a, b = map(int, input().split()) 
    arr.append((a, b))
    

def set_tree(here, parent, value):

    depth[here] = depth[parent] + 1
    ps[here][0] = parent
    dis[here] = dis[parent] + value

    for i in range(1, MAX_LEVEL+1):
        temp = ps[here][i-1]
        ps[here][i] = ps[temp][i-1]



    for next_node , value in graph[here]:
        if next_node != parent:
            set_tree(next_node, here, value)


depth[0] = -1
dis[0] = 0
set_tree(1, 0, 0)

 
for a, b in arr:
    cur = [a, b]
    if(depth[a] != depth[b]):
        if depth[a] > depth[b]:
            a, b = b, a
        
        for i in range(MAX_LEVEL, -1, -1):
            if depth[a] <= depth[ps[b][i]]:
                b = ps[b][i] 

    lca = a
    if a != b:
        for i in range(MAX_LEVEL, -1, -1):
            if ps[a][i] != ps[b][i]:
                a = ps[a][i]
                b = ps[b][i]
            lca = ps[a][i]
    
    a, b = cur
    answer = dis[a] + dis[b] - dis[lca] * 2
    print(answer)
        


 