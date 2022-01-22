from math import floor, log2
import sys
from tkinter.tix import MAX

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

for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

M = int(input())

for i in range(M):
    a, b = map(int, input().split()) 
    arr.append((a, b))
    

def set_tree(here, parent):

    depth[here] = depth[parent] + 1
    ps[here][0] = parent

    for i in range(1, MAX_LEVEL+1):
        temp = ps[here][i-1]
        ps[here][i] = ps[temp][i-1]



    for next_node in graph[here]:
        if next_node != parent:
            set_tree(next_node, here)


depth[0] = -1
set_tree(1, 0)

 
for a, b in arr:
    if(depth[a] != depth[b]):
        if depth[a] > depth[b]:
            a, b = b, a
        
        # b의 2^i 번째 조상 깊이와 a 깊이 비교 
        for i in range(MAX_LEVEL, -1, -1):

            #b의 2^i 번째 조상이 a 깊이보다 깊거나 같으면
            #b의 2^i 번째 조상의 2^(i-1)번째~ 1번째 조상과 비교를 계속한다.
            if depth[a] <= depth[ps[b][i]]:
                b = ps[b][i] 

    answer = a
    if a != b:
        # 2^i 번째 조상이 서로 달라지면 a, b 교체
        for i in range(MAX_LEVEL, -1, -1):
            if ps[a][i] != ps[b][i]:
                a = ps[a][i]
                b = ps[b][i]
            answer = ps[a][i]
    print(answer)

 