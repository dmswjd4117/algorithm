from collections import deque
from itertools import permutations
import heapq
import  sys 

sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()
 

INF = int(1e10)

N = int(input())
graph = [
    [] for _ in range(N+1)
]
ind = [0] * (N+1)
T = [ 0 for _ in range(N+1)]
for i in range(1, N+1):
    string = list(map(int, input().split()))
    t, cnt, arr = string[0], string[1], string[2:]
    T[i] = t
    ind[i] = cnt
    for a in arr:
        graph[a].append(i)


def top():
    ans = [0] * (N+1)
    q = deque([])
    
    for i in range(1, N+1):
        if ind[i] == 0:
            q.append(i)
            ans[i] = T[i]
    
    while q:
        now = q.popleft()

        for i in graph[now]:
            ind[i] -= 1
            ans[i] = max(ans[now] + T[i], ans[i])
            if ind[i] == 0:
                q.append(i)


    return ans

ans = top()
print(max(ans))
