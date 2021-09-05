# https://www.acmicpc.net/problem/1744

import sys
from copy import deepcopy as dcpy
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

f = open("./data.txt", "r")
input = lambda: f.readline().rstrip()

n = int(input())
answer = 0
arr = []
minus = []

for i in range(n):
    a = int(input())
    if a <= 0:
        minus.append(a)
    else:
        arr.append(a)

arr.sort(reverse=True)
minus.sort()

def get(arr):
    res = 0
    i = 0
    while True:
        if i >= len(arr):
            break
        if i == len(arr)-1:
            res += arr[i]
            break

        if arr[i+1]*arr[i] > arr[i]:
            # print( arr[i+1], arr[i])
            res += arr[i+1]*arr[i]
            i += 2
        else:
            # print( arr[i])
            res += arr[i]
            i += 1
    return res

 
print(get(arr) + get(minus))
