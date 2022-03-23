# https://www.acmicpc.net/problem/2579

import sys
 
sys.setrecursionlimit(10000)

input = lambda : sys.stdin.readline().rstrip()

f = open("./file.txt", "r")
input = lambda: f.readline().rstrip()


INF = float('inf')

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
    
dp = [
    [0, 0, 0] for _ in range(N)
]

dp[0][0] = arr[0]

dp[1][0] = arr[1] 
dp[1][1] = dp[0][0] + arr[1]

for i in range(2, N):
    dp[i][0] = max(dp[i-2]) + arr[i]
    dp[i][1] = dp[i-1][0] + arr[i]
    dp[i][2] = dp[i-1][1] + arr[i]

for i in range(N):
    print(dp[i])