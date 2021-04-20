import sys
from itertools import permutations
sys.setrecursionlimit(100000)
input = lambda : sys.stdin.readline().rstrip()
 
A,B =input().split()  
N = len(A)
B = int(B)

arr = []
pers = list(permutations(A))

for per in pers:
    num = int("".join(per))
    if len(str(num)) != N:
        continue
    arr.append(num)

arr.sort()

def floor(left, right, K):
    if left >= right :
        if arr[left-1] < K:
            return arr[left-1]
        return -1

    mid = (left + right)//2
    if arr[mid] > K:
        return floor(left, mid, K)
    elif arr[mid] < K:
        return floor(mid+1, right, K)
    else:
        return floor(left+1, right-1, K)

print(floor(0, len(arr)-1, B))
