import sys 

input = lambda : sys.stdin.readline().rstrip()

N, S = map(int, input().split())

arr = list(map(int, input().split()))

count = 0
for i in range(1, 1 << N):
    hap = 0
    for j in range(N):
        if(i & (1 << j)):
            hap += arr[j]
    if hap == S:
        count += 1

print(count)