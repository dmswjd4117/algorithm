# https://www.acmicpc.net/problem/9252
# https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence
#  1
from collections import deque
from itertools import permutations
from heapq import *
import  sys 
sys.setrecursionlimit(10**9)
input = lambda : sys.stdin.readline().rstrip()

 
INF = int(1e8)
mod = 10007

 
a =  '0'+input()
b =  '0'+input()

al = len(a)-1
bl = len(b)-1


dp = [
    [0] * (bl+1)
    for _ in range(al+1)
]
 

def printf():
    for i in range(1, al+1):
        for j in range(1, bl+1):
            print(dp[i][j],end=' ')
        print()
    print()


for i in range(1, al+1):
    for j in range(1, bl+1):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])



def go(x, y):
    if dp[x][y] == 0:
        return 

    px, py = x-1, y
    if dp[x][y] == dp[px][py]:
        return go(px, py)

    px, py = x, y-1
    if dp[x][y] == dp[px][py]:
        return go(px, py)

    px, py = x-1, y-1
    if dp[x][y]-1 == dp[px][py]:
        go(px, py)
        print(a[x],end='')
        

print(dp[al][bl])
go(al,bl)


# 2
# https://hjp845.tistory.com/29

# 3
from collections import deque
from itertools import permutations
import heapq
import  sys 

sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()


INF = int(1e10)

a = [0] + list(input())
b = [0] + list(input())

N = len(a)
M = len(b)

lcs = [
    [0] * (M+1)
    for _ in range(N+1)
]

ans = [
    [ '0' ] * (M+1)
    for _ in range(N+1)
]


for i in range(1, N):
    for j in range(1, M):
        if a[i] == b[j]:
            lcs[i][j] = lcs[i-1][j-1] + 1
            if ans[i-1][j-1] != '0':
                ans[i][j] = ans[i-1][j-1] + a[i]
            else:
                ans[i][j] = a[i]
        else:
            if lcs[i][j-1] > lcs[i-1][j]:
                lcs[i][j] =  lcs[i][j-1]
                ans[i][j] = ans[i][j-1] 
            else:
                lcs[i][j] =  lcs[i-1][j]
                ans[i][j] = ans[i-1][j]
        
 
if lcs[N-1][M-1] == 0:
    print(lcs[N-1][M-1])
else:
    print(lcs[N-1][M-1])
    print(ans[N-1][M-1])
