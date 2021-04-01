import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

# f = open("./main.txt", "r")
# input = lambda: f.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
dist = [1] * (N)


for i in range(1, N):
    for j in range(0, i):
        if arr[i] > arr[j]:
            dist[i] = max(dist[i], dist[j]+1)

print(max(dist))