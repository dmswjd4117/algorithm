import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(1000000)


# f = open("./file.txt", "r")
# input = lambda: f.readline().rstrip()
 
n = int(input())
arr = list(map(int, input().split()))
rNode = int(input())


root = 0
answer = 0
graph = [
    set([]) for _ in range(n)
]

for i in range(n):
    if arr[i] == -1:
        root = i
    else:
        par = arr[i]
        graph[par].add(i)


if rNode == root:
    print(0)
    exit(0)

graph[arr[rNode]].discard(rNode)
 

vis = [False] * (n)
def go(index):
    global answer
    if vis[index]:
        return
    
    if not graph[index]:
        answer += 1

    for nextNode in graph[index]:
        go(nextNode)

    vis[index] = True

go(root)
print(answer)