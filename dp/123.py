import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()


Test = int(input())

MAX = 10 ** 6
mod = 1000000009
check = [0] * (MAX + 2)
check[1],check[2], check[3] = 1,2,4 

for i in range(4, MAX+1):
    check[i] = (check[i-1] + check[i-2] + check[i-3]) % mod

for TEST in range(Test):
    n = int(input())
    print(check[n])
