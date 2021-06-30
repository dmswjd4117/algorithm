import  sys 
import copy
from itertools import permutations
import heapq

f = open("data.txt", 'r')
input = lambda : f.readline().rstrip()


n = int(input())
graph = ['0']
for i in range(n):
    graph.append(int(input()))


vis = [0] * (n+1)
res = []
def dfs(start, cur):
 
    if start == cur and vis[cur] >= 1: 
        res.append(start)
        return True

    if vis[cur] == 0:
        vis[cur] += 1
        dfs(start, graph[cur])

    return False


for i in range(1, n+1):
    vis = [0] * (n+1)
    dfs(i, i)
 

print(len(res))

for a in res:
    print(a)

# 2

import  sys 
import copy
from itertools import permutations
import heapq

 

n = int(input())
graph = ['0']
for i in range(n):
    graph.append(int(input()))


vis = [0] * (n+1)

def dfs(x):
    if vis[x] >= 2:
        return
 
    vis[x] += 1
    dfs(graph[x])

def init():
    for i in range(1, n+1):
        if vis[i] != 2:
            vis[i] = 0


for i in range(1, n+1):
    if vis[i] != 2:
        dfs(i)
        init()

ans = []
for i in range(1, n+1):
    if vis[i] == 2:
        ans.append(i)


print(len(ans))
ans.sort()
for a in ans:
    print(a)