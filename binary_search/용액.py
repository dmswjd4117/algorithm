import sys
 
input = lambda : sys.stdin.readline().rstrip()
 

# f = open("./file.txt", "r")
# input = lambda: f.readline().rstrip()
 
INF = float("inf")

N = int(input())

arr = list(map(int, input().split()))
arr.sort()


def lower_bound(start, end, target):
    mid = (start + end) // 2
    if start == end:
        return start
    
    if arr[mid] < target:
        return lower_bound(mid+1, end, target)
    if target <= arr[mid]:
        return lower_bound(start, mid, target)

 

answer = INF
values = []
for i in range(N):
    index = lower_bound(0, N-1, -arr[i])
    
    for j in [-1, 0, 1]:
        t_index = index + j
        if t_index < 0 or t_index >= N or t_index == i: continue

        res = abs(arr[i] + arr[t_index])
 

        if res < answer: 
            answer = res
            values = [arr[i], arr[t_index]]

values.sort()
print(values[0] , values[1])