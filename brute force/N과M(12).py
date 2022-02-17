N , M = map(int, input().split())

nums = list(map(int, input().split()))

nums = sorted(list(set(nums)))
N = len(nums)

ans = [0] * 10
check = [False] * 10

def find(index, start):
    if index == M:
        for i in range(M):
            print(ans[i], end=" ")
        print()
        return 
    
    for i in range(start, N):
        ans[index] = nums[i]
        find(index+1, i)


find(0, 0)

# 2 

import sys
 
sys.setrecursionlimit(10000)

input = lambda : sys.stdin.readline().rstrip()


# f = open("./file.txt", "r")
# input = lambda: f.readline().rstrip()

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
arr = [0] * (m)
vis = set([])
 
def go(index):
    if index == m:
        string = " ".join(map(str, arr))
        if string in vis:
            return
        vis.add(string)
        print(string)
        return
    for i in range(n):
        num = nums[i]
        if index == 0:
            arr[index] = num
            go(index+1)
        elif  arr[index - 1] <= num:
            arr[index] = num
            go(index+1)

go(0)


 

 