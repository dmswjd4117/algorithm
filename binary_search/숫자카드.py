import sys
from collections import deque
 
INF = float('inf')

input = lambda : sys.stdin.readline().rstrip()
 

n = int(input())

cards = list(map(int, input().split()))

m = int(input())

arr = list(map(int, input().split()))

cards.sort()

 

def upper(left, right, num):
    mid = (left + right) // 2
    
    if left > right:
        return left
    
    if cards[mid] <= num:
        return upper(mid+1, right, num)
    
    if cards[mid] > num: 
        return upper(left, mid-1, num)

def lower(left, right, num):
    mid = (left + right) // 2
    if left > right:
        return right
    
    if cards[mid] < num:
        return lower(mid+1, right, num)
    
    if cards[mid] >= num:
        return lower(left, mid-1, num)

 
for i in range(m):
    a = upper(0, n-1, arr[i])
    b = lower(0, n-1, arr[i])
    print(a-b-1,end=' ')


# 2
import sys
from collections import deque
 
INF = float('inf')

input = lambda : sys.stdin.readline().rstrip()



n = int(input())
arr = list(map(int, input().split()))

m = int(input())
find_arr = list(map(int, input().split()))

arr.sort()

def lower(start, end, target):
    if start >= end:
        return end

    mid = (start + end) // 2

    if arr[mid] < target:
        return lower(mid+1, end, target)

    if arr[mid] >= target:
        return lower(start, mid, target)

def upper(start, end, target):
    if start >= end:
        return end

    mid = (start + end)//2

    if arr[mid] <= target:
        return upper(mid+1, end, target)

    if arr[mid] > target:
        return upper(start, mid, target)

 

for a in find_arr:
    
    left = lower(0, n, a)
    right = upper(0, n, a)

 
 
    print(right-left,end=' ')
 
    
 