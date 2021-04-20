# 오름차순
# 선택정렬 (최소값을 앞에 나두기)
import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

f = open("./main.txt", "r")
input = lambda: f.readline().rstrip()

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

for i in range(0, N):
    minI = i
    for j in range(i+1, N):
        if arr[minI] > arr[j]:
            minI = j

    arr[minI],arr[i] = arr[i], arr[minI]

for a in arr:
    print(a)


# 선택정렬 (최대값을 뒤에 나두기)
import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

f = open("./main.txt", "r")
input = lambda: f.readline().rstrip()

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

for point in range(N-1, -1, -1):
    maxI = point
    for i in range(0, point):
        if arr[maxI]<arr[i]:
            maxI = i
    arr[maxI], arr[point] = arr[point], arr[maxI]

for a in arr:
    print(a)


# O(n^2)