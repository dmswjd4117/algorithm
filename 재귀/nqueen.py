import sys
from itertools import permutations
input = lambda : sys.stdin.readline().rstrip()

# f = open("./main.txt" , 'r')
# input = lambda : f.readline().rstrip()

N = int(input())
ans = [
    [0] for _ in range(N)
]

def check(tx, ty):
    for i in range(0, tx):
        x, y = i, ans[i]
        # if x == tx or y == ty:
        #     return False
        if abs(tx-x) == abs(ty-y):
            return False

    return True


vis = [False] * N
cnt = 0
def go(index):
    global cnt
    if index == N:
        cnt += 1
        return
    
    for i in range(0, N):
        if vis[i]: continue

        ans[index] =  i #(index, i)
        if index >= 1 and not check(index, i):
            continue
        vis[i] = True
        go(index+1)
        vis[i] = False

go(0)

print(cnt)
