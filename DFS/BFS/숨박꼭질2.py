from collections import deque

MAX = 100001
dist = [0] * 100001
count = [0] * 100001
check = [False] * 100001

N ,K = map(int, input().split())

dq = deque([])
dq.append(N)
count[N] = 1
check[N] = True

while dq:
    now = dq.popleft()
    for a in [now-1, now+1, now*2]:
        if 0 > a or a > 100000 :
            continue

        if check[a] == False:
            check[a] = True
            count[a] = 1
            dist[a] = dist[now] + 1
            dq.append(a)

        elif dist[a] == dist[now]+1:
            count[a] += 1
            dq.append(a)

        elif dist[a] > dist[now]+1:
            count[a] = 1
            dist[a] = dist[now] + 1
            dq.append(a)

print(dist[K])
print(count[K])