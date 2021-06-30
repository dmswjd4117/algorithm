from collections import deque
import sys
from heapq import *

sys.setrecursionlimit(10000000)
input = lambda : sys.stdin.readline().rstrip()
 
MAX = 100000
check = [False] * 100002
dist = [999999] * 100002

N, M = map(int, input().split())

dq = deque([])
dq.append(N)
dist[N] = 0


while dq:
    x = dq.popleft()
    if x == M:
        print(dist[x])
        break
    # 파이썬 False == 0 <--- True
    if x!= 0 and x*2 <= MAX and dist[x*2] > dist[x]:
        dist[x*2] = dist[x] + 0
        dq.append(x*2)

    if x+1 <= MAX and dist[x+1] > dist[x]+1:
        dist[x+1] = dist[x] + 1
        dq.append(x+1) 

    if 0 <= x-1  and dist[x-1] > dist[x]+1:
        dist[x-1] = dist[x] + 1
        dq.append(x-1)


# heapq

INF = int(1e8)
mod = 10*9+9
MAX = 10**9

n, m = map(int, input().split())

def isin(x):
    return 0 <= x <= 100000


def go(start, end):
    q = []
    vis = set()
    heappush(q, (0, start))
    vis.add(start)

    while q:
        t, x = heappop(q)
        if x in vis:
            continue

        vis.add(x) 

        if x == end:
            return t

        nx = x * 2
        if isin(nx) and ( nx not in vis):
            heappush(q, (t, nx))
 
        nx = x + 1
        if isin(nx) and ( nx not in vis):
            heappush(q, (t+1, nx))
 

        nx = x - 1
        if isin(nx) and ( nx not in vis):
            heappush(q, (t+1, nx))

    return False

print(go(n, m))

# https://www.acmicpc.net/board/view/63576