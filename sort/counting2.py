import copy
import sys
import heapq
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

f = open("main.txt", 'r')
input = lambda : f.readline().rstrip()

MAX = 10002

N = int(input())

ans = [0] * (MAX)
for i in range(N):
    num = int(input())
    ans[num] += 1
    

for i in range(0, MAX):
    if ans[i] != 0:
        for j in range(ans[i]):
            print(i)
