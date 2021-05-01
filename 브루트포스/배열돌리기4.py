import  sys 
import copy
from itertools import permutations
sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()

MAX = 987654321

N, M, K = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

orders = []
for i in range(K):
    orders.append(list(map(int, input().split())))

def rotate(graph, x, y, N):
    temp = graph[x][y]
    for mx, my in [[0, 1],[1, 0],[0, -1],[-1, 0]]:
        for i in range(N):
            next_temp = graph[x+mx][y+my]
            x, y = x+mx, y+my
            graph[x][y] = temp
            temp = next_temp
            

ans = MAX
for perm in permutations(orders):
    temp_graph = copy.deepcopy(graph)
    for r,c,s in perm:
        x,y,n = r-s-1,c-s-1,2*s
        # print(x, y, n)
        index = 0
        for length in range(n, 1, -2):
            tx, ty = x+index*1 , y+index*1
            rotate(temp_graph, tx, ty, length)
            index += 1

    for i in range(N):
        hap = 0
        for j in range(M):
            hap += temp_graph[i][j]
        ans = min(hap, ans)

print(ans)