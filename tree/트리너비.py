import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(1000000)
 

MAX = 10002

N = int(input())
graph = [
    [0, 0, 0] for _ in range(N+1)
]


root = 0
arr = [0] * (N+1)
ansMin = [0] * (N+1)
ansMax = [0] * (N+1)

for i in range(N):
    a, b, c = map(int, input().split())
    graph[a][0] = a
    graph[a][1] = b
    graph[a][2] = c
    
    # -1 이 아닐때 !!
    if b!=-1:
        arr[b] += 1
    if c != -1:
        arr[c] += 1 

for i in range(1, N+1):
    if arr[i] == 0:
        root = i
        break

cnt = 0
lev = 0
def go(index, level):
    global lev
    global cnt
    if index == -1:
        return 

    go(graph[index][1], level+1)

    cnt += 1
    lev = max(lev, level)
    if ansMin[level] == 0:
        ansMin[level] = cnt 
    ansMax[level] = cnt

    go(graph[index][2], level+1)

go(root, 1)

ans = 0
ans_lev = 0
for i in range(1, lev+1):
    if ans < ansMax[i] - ansMin[i] + 1:
        ans = ansMax[i] - ansMin[i] + 1
        ans_lev = i

print(ans_lev, ans)