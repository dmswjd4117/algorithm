# 1

N, M = map(int, input().split())


res = [0] * 10
def go(index, start):

    if index == M:
        for i in range(M):
            print(res[i],end=" ")
        print()
        return 

    for i in range(start, N+1):
        res[index] = i
        go(index+1, i+1)

go(0,1)

# 2 

N, M = map(int, input().split())

res = [0] * 10
nums = [x for x in range(1, N+1)]

def go(i, index):
    if index == M:
        for i in range(0, M):
            print(res[i],end=" ")
        print()
        return
    
    if i >= N:
        return

    res[index] = nums[i]
    go(i+1, index+1)

    res[index] = 0
    go(i+1, index)


go(0, 0)

# 3 combinations

from  itertools import combinations

N, M = map(int, input().split())

arr = [x for x in range(1, N+1)]
res = combinations(arr, M)

for nums in res:
  for num in nums:
    print(num, end=" ")
  print()


