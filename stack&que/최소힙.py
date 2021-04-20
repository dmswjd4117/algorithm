import copy
import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

f = open("main.txt", 'r')
input = lambda : f.readline().rstrip()


N = int(input())
arr = deque([0])

def heapify(index, n):
    p = index
    left = index*2 
    right = index*2+1
    if left <= n and arr[left] < arr[p]:
        p = left
    if right <= n and arr[right] < arr[p]:
        p = right
    if p != index:
        arr[p],arr[index]=arr[index],arr[p]
        heapify(p, n)

def remove(n):
    deleted = arr[1]

    arr[1], arr[n] = arr[n], arr[1]
    arr.pop()
    heapify(1, n-1)

    return deleted

def insert(num, n):
    arr.append(num)
    n += 1

    while n > 1:
        if arr[n] < arr[n//2]:
            arr[n//2],arr[n] = arr[n],arr[n//2]
            n = n // 2
        else:
            break

for i in range(N):
    o = int(input())
    n = len(arr)-1
    if o == 0 and n == 0:
        print(0)
    elif o == 0 and n!= 0:
        a = remove(n)
        print(a)
    else:
        insert(o, n)
