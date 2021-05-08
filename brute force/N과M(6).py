from itertools import permutations

N, M = map(int , input().split())

arr = list(map(int , input().split()))


arr.sort()

p = permutations(arr, M)

for arr in p:
    if list(arr) == sorted(arr):
        for i in arr:
            print(i , end=" ")
        print()