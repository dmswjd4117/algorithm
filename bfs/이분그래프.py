# https://www.acmicpc.net/problem/1707

from collections import deque
from itertools import permutations
from heapq import *
import  sys 
sys.setrecursionlimit(10**9)
input = lambda : sys.stdin.readline().rstrip()

f = open("data.txt", 'r')
input = lambda : f.readline().rstrip()

INF = int(1e8)
mod = 10*9+9

T = int(input())

for _ in range(T):

    V, E = map(int, input().split())
    
    graph = [
        [] for _ in range(V+1)
    ]

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    arr = [set(), set()]

    def bfs(x):
        dq = deque([(0, x)])
        arr[0].add(x)

        while dq:
            index, x = dq.popleft()

            nindex = 1-index
            for nx in graph[x]:

                if nx in arr[nindex]:
                    continue

                arr[nindex].add(nx)
                dq.append((nindex, nx))  


    for i in range(1, V+1):
        # 해당 노드를 아직 방문하지 않았을때만 
        if i not in arr[1]:
            bfs(i)

    flag = False

    for x in range(1, V+1):
        for nx in graph[x]:
            if x in arr[0] and nx in arr[0]:
                flag = True
                break
            if x in arr[1] and nx in arr[1]:
                flag = True
                break
        if flag:
            print('NO')
            break
    else:
        print('YES')
 
