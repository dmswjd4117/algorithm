#https://www.acmicpc.net/problem/12970
# https://www.acmicpc.net/problem/1790

import sys
import heapq
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(10000)


f = open("./file.txt", "r")
input = lambda: f.readline().rstrip()

N, K = map(int, input().split())


def cal(N):
    res = 0
    leng = len(str(N))
    for i in range(1, leng+1):
        loc = 10 ** (i-1)
        if i == leng:
            res += i * (N - loc + 1)
        else:
            res += i * (9 * loc)

    return res


def more_than(start, end, leng):    
    mid = (start+end)//2
    mid_leng = cal(mid)

    if start > end:
        return start

    if mid_leng == leng: 
        return mid
    elif mid_leng < leng:
        return more_than(mid+1, end, leng)
    else:
        return more_than(start, mid-1, leng)


if cal(N) < K :
    print(-1)
else:
    number = more_than(0, 100_000_002, K)
    diff = cal(number) - K
    str_num = str(number)
    answer = str_num[-diff-1]


    print(answer)