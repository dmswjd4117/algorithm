import sys
from copy import deepcopy
from itertools import combinations

sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

f = open("./data.txt", "r")
input = lambda: f.readline().rstrip()

INF = float('inf')



n, m = map(int, input().split())

arr = []
chicken = []
house = []
answer = INF

for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append((i, j))
        elif arr[i][j] == 1:
            house.append((i, j))

chic_len = len(chicken)
ans = [0] * chic_len

def cal(fx, fy, x, y):
    return abs(fx-x) + abs(fy-y)

ans = [0] * m
 
def go(index, start):
    global answer

    if index == m:
        res = 0      
        for i in range(len(house)):
            x, y = house[i]
            temp = INF
            for j in range(m):
                cx, cy = chicken[ans[j]]
                temp = min(temp, cal(cx, cy, x, y))
            res += temp

        answer = min(answer, res)
        return

    for i in range(start, chic_len):
        ans[index] = i
        go(index+1, i+1)


go(0, 0)
print(answer)


# 2 

import sys
from copy import deepcopy
from itertools import combinations

sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()
 

INF = float('inf')



n, m = map(int, input().split())

arr = []
chicken = []
house = []
answer = INF

for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append((i, j))
        elif arr[i][j] == 1:
            house.append((i, j))

chic_len = len(chicken)
ans = [0] * chic_len

def cal(fx, fy, x, y):
    return abs(fx-x) + abs(fy-y)

def dfs(index, select):
    global answer
    
    if select == m:
        res = 0
        for i in range(len(house)):
            x, y = house[i]
            temp = INF
            for j in range(chic_len):
                if not ans[j]:
                    continue
                cx, cy = chicken[j]
                temp = min(temp, cal(cx, cy, x, y))
            res += temp

        answer = min(answer, res)
        return

    if index == chic_len:
        return

    ans[index] = True
    dfs(index+1, select+1)

    ans[index] = False
    dfs(index+1, select)


dfs(0, 0)

print(answer)