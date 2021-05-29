# 버블정렬(오름차순)
import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

f = open("./main.txt", "r")
input = lambda: f.readline().rstrip()

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

for last in range(N-1, -1, -1):
    for i in range(0, last):
        if arr[i] > arr[i+1]:
            arr[i+1],arr[i] = arr[i], arr[i+1]

for a in arr:
    print(a)

# O(n^2)