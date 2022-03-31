import sys
from collections import deque

sys.setrecursionlimit(10000)

input = lambda : sys.stdin.readline().rstrip()

INF = float('inf')

N = int(input())
arr = list(map(int, input().split()))

def lower_bound(l, r, arr, key):
    while l < r:
        m = ( l + r ) // 2 
        if arr[m] < key:
            l = m + 1
        if arr[m] >= key:
            r = m
    return l


sub = [arr[0]]
pos = [(0, arr[0])]

for i in range(1, N):
    index = lower_bound(0, len(sub), sub, arr[i])
    if index == len(sub):
        sub.append(arr[i])
    else:
        sub[index] = arr[i]
    pos.append((index, arr[i]))
    
answer = deque([])
index = len(sub)-1
while pos:
    end = pos.pop()
    if end[0] == index:
        answer.append(end[1])
        index -= 1
    
print(len(answer))
while answer:
    a = answer.pop()
    print(a, end=' ')