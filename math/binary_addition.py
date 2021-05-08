# 이산수학 5.2.1
from collections import deque
import sys
sys.setrecursionlimit(10000000)
input = lambda : sys.stdin.readline().rstrip()

f = open("./main.txt", "r")
input = lambda : f.readline().rstrip()

T = int(input())

def addBin(a, b):
    carry = 0
    ans = deque([])
    A = len(a)-1
    B = len(b)-1
    while 1:
        if A <= -1 and B <= -1: break
        ta, tb = 0, 0 
        if A >= 0: ta = int(a[A])
        if B >= 0: tb = int(b[B])
        thap = ta + tb + carry
        carry = thap // 2
        ans.appendleft(thap % 2)
        A -= 1
        B -= 1

    if carry:
        ans.appendleft(1)

    index = 0
    while ans[index] == 0 and index < len(ans)-1:
        index += 1

    for i in range(index, len(ans)):
        print(ans[i],end='')
    print()

for _ in range(T):
    a, b = input().split()
    addBin(a, b)