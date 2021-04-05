import copy
import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()


N = int(input())
arr = deque([0])

def heapify(index, n):
    p = index
    left = index*2
    right = index*2+1

    if left<= n and arr[left]>arr[p]:
        p = left

    if right<= n and arr[right]>arr[p]:
        p = right

    if p != index:
        arr[p],arr[index]=arr[index],arr[p]
        heapify(p, n)


def insert(a):
    arr.append(a)

    n = len(arr)-1
    while n > 1:
        if arr[n] < arr[n//2]:
            break
        arr[n],arr[n//2] = arr[n//2],arr[n]
        n //= 2
        

def delete(n):
    deleted = arr[1]
    arr[1],arr[n] = arr[n], arr[1]
    arr.pop()
    heapify(1, n-1)
    return deleted


for i in range(N):
    a = int(input())

    if a == 0:
        n = len(arr)-1
        if n == 0: 
            print(0)
        else:            
            print(delete(n))

    else:
        insert(a)


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
    o = int(input())
    if o == 0:
        if len(arr) == 0:
            print(0)
            continue
        print(-1 * heapq.heappop(arr))
    else:
        heapq.heappush(arr,-1 * o)