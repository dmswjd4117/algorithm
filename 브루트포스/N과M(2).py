from  itertools import combinations

N, M = map(int, input().split())

arr = [x for x in range(1, N+1)]
res = combinations(arr, M)

for nums in res:
  for num in nums:
    print(num, end=" ")
  print()