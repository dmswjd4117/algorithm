import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

arr = [
    [0, 0]
    for _ in range(100)
]

arr[1][0] = 0
arr[1][1] = 1
arr[2][0] = 1

for i in range(3, N+1):
    arr[i][0] = arr[i-1][0] + arr[i-1][1]
    arr[i][1] = arr[i-1][0]

print(arr[N][0] + arr[N][1])