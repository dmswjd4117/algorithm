import copy
import sys
import heapq
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

f = open("main.txt", 'r')
input = lambda : f.readline().rstrip()

MAX = 10002

N = int(input())

arr = []
haps = [0] * (MAX)
ans = [0] * (N+2)

for i in range(N):
    num = int(input())
    arr.append(num)
    haps[num] += 1
    

for i in range(1, N):
    haps[i] = haps[i-1] + haps[i]


for i in range(N-1, -1, -1):
    num = arr[i]
    index = haps[num]
    ans[index] = num
    haps[num] -= 1


for i in range(1, N+1):
    print(ans[i])