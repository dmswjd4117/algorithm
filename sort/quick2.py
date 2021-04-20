import copy
import heapq
import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

f = open("main.txt", 'r')
input = lambda : f.readline().rstrip()


N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))

def part(start, end):
    p_index = end
    pivot = arr[end]
    # index는 pivot보다 작은수들중 가장 큰수의 위치이다.
    index = start-1
    for j in range(start, end):
        if arr[j] <= pivot:
            index += 1
            arr[index], arr[j] = arr[j], arr[index]
    
    arr[index+1],arr[p_index]=arr[p_index],arr[index+1]
    return index + 1



def quick(start, end):
    if start >= end:
        return 

    p_index = part(start, end)
    quick(start, p_index-1)
    quick(p_index+1, end)

quick(0, N-1)
for a in arr:
    print(a)