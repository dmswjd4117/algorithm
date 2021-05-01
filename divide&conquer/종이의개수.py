from collections import deque, Counter
import  sys 
sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

ans = [0, 0, 0]

def isin(x, y):
    return 0 <= x <= N-1 and 0 <= y <= N-1

def issame(x, y, index):
    num = graph[x][y]
    for i in range(index):
        for j in range(index):
            tx, ty = x + i, y + j
            if graph[tx][ty] != num:
                return False
    return True

def go(x, y, index):

    if issame(x, y, index):
        num = graph[x][y]
        ans[num+1] += 1
        return

    size = index // 3
    for i in range(3):
        for j in range(3):
            tx, ty = x+size*i, y+size*j
            if not isin(tx, ty): continue
            go(tx, ty, size)

go(0, 0, N)