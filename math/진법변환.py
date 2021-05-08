import sys
input = lambda : sys.stdin.readline().rstrip()

A , B = map(int, input().split())
m = int(input())
nums = list(map(int, input().split()))


# 10진법에서 base진법으로
def fromTen(num, base):
    res = []
    while num != 0:
        na = num % base
        num = num // base
        res.append(str(na))
    return res

ten = 0
go = 1
for i in range(m-1, -1 ,-1):
    ten += go * nums[i]
    go *= A


ans = fromTen(ten, B)
for i in range(len(ans)-1, -1, -1):
    print(int(ans[i]), end=' ')
    
