import sys
from collections import deque
 
INF = float('inf')

input = lambda : sys.stdin.readline().rstrip()
 
 
n, m = map(int, input().split())

arr = list(map(int, input().split()))

start, end = 0, 0
S = 0
answer = 0

while 1:
    
    if S >= m:
        S -= arr[start]
        start += 1

    elif end == n:
        break

    elif S < m:
        S += arr[end]
        end += 1

    if S == m:
        answer += 1

print(answer)