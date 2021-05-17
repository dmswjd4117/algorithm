import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)
from collections import deque

 
N, M = map(int, input().split())
ps = [x for x in range(N+1)]

def find(x):
    if ps[x] == x:
        return x
    ps[x] = find(ps[x]) 
    return ps[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        ps[b] = a
    else:
        ps[a] = b

for i in range(M):
    order, a, b = map(int, input().split())
    if order == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")