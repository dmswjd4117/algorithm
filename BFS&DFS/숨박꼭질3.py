from collections import deque
import sys
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