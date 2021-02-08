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