from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

# f = open("main.txt", 'r')
# input = lambda : f.readline().rstrip()

N = int(input())


MOD = 1000000000
arr = [
    [0] * (10)
    for _ in range(N+1)
]

for i in range(1, 10):
    arr[1][i] = 1


for n in range(2, N+1):
    arr[n][0] = (arr[n-1][1]) % MOD
    for i in range(1, 8+1):
        arr[n][i] = (arr[n-1][i-1] + arr[n-1][i+1]) % MOD
    arr[n][9] = (arr[n-1][8]) % MOD

ans = 0
for i in range(0, 10):
    ans += arr[N][i] 


print(ans % MOD )
