import copy
import sys
from collections import deque
import math
input = lambda : sys.stdin.readline().rstrip()

f = open("main.txt", 'r')
input = lambda : f.readline().rstrip()

N = 1234567891234
length = len(str(N))
g = 1000 ** 5

while N != 0:
    ans = N // g
    N = N % g
    g = g // 1000

    if ans == 0:
        continue

    print(ans, end='')

    if N != 0:
        print(',',end='')