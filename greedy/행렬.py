# https://www.acmicpc.net/problem/1080

import sys
from copy import deepcopy
from itertools import combinations
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

f = open("./data.txt", "r")
input = lambda: f.readline().rstrip()

n, m = map(int, input().split())
am = []
bm = []
answer = 0
for i in range(n):
    am.append(list(map(int, input())))
for i in range(n):
    bm.append(list(map(int, input())))

 
def flip(arr, x, y):
    for i in range(3):
        for j in range(3):
            tx = x + i
            ty = y + j
            arr[tx][ty] = 1 - arr[tx][ty]

 
for i in range(n-2):
    for j in range(m-2):
        if am[i][j] != bm[i][j]:
            flip(am, i, j)
            answer += 1

def anwer_out():
    for i in range(n):
        for j in range(m):
            if am[i][j] != bm[i][j]:
                print(-1)
                return

    print(answer)

anwer_out()