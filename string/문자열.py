import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(1000000)

A, B = input().split()
N = len(A)

index = 0
ans = 100
while index+N <= len(B):
    temp = 0
    for i in range(N):
        if B[index+i] != A[i]: temp+=1
    ans = min(ans, temp)
    index += 1
print(ans)
