# 피봇을 파트의 마직막 번호로 설정
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
    pi_index = end
    left = start
    right = end-1

    while 1:
        while arr[left] < arr[pi_index]:
            left += 1
        while arr[right] > arr[pi_index]:
            right -= 1

        if left > right: break
        if left < right:
            arr[left],arr[right]=arr[right],arr[left]

    arr[left], arr[pi_index] = arr[pi_index], arr[left]
    return left

def quick(start, end):
    if start >= end:
        return 
    pivot_index = part(start , end)
    quick(start , pivot_index-1)
    quick(pivot_index+1, end)

quick(0, N-1)
for a in arr:
    print(a)



# 피봇을 파트의 처음으로 설정
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
    pi_index = start
    left = start+1
    right = end

    while 1:
        while left <= end and arr[left] < arr[pi_index]:
            left += 1
        while right >= start and arr[right] > arr[pi_index]:
            right -= 1

        if left > right: break
        if left < right:
            arr[left],arr[right]=arr[right],arr[left]

    arr[right], arr[pi_index] = arr[pi_index], arr[right]
    return right

def quick(start, end):
    if start >= end:
        return 
    pivot_index = part(start , end)
    quick(start , pivot_index-1)
    quick(pivot_index+1, end)

quick(0, N-1)
for a in arr:
    print(a)