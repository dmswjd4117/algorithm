test = int(input())
for TEST in range(test):

    N, M = map(int, input().split())

    graph = [
        [] 
        for _ in range(N+1)
    ]  

    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    vis = [False] * (N+1)

    ans = 1
    def go(x, cnt):
        global ans
        ans = max(ans, cnt)
        vis[x] = True

        for n in graph[x]:
            if vis[n]: continue
            go(n, cnt+1)
        
        # 방문해제하기 !-!
        vis[x] = False

    for i in range(1, N+1):
        go(i, 1)

    print("#%d %d"%(TEST+1, ans))