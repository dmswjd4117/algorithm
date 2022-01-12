import sys
from collections import deque
 
INF = float('inf')

input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(1000000)

# f = open("./file.txt", "r")
# input = lambda: f.readline().rstrip()
 

m = int(input())
bits = 1 << 21

for i in range(m):
    arr = list(input().split())
    
    o = arr[0]
    num = 0
    if len(arr) > 1:
        num = int(arr[1])

    if  o == "all":
        # print(o)
        bits = ~(1 << 1)

    elif o == "empty":
        # print(o)
        bits = 1 << 21

    elif o == "add":
        # print(o)
        bits |= ( 1 << num )
 

    elif o == "remove":
        # print(o)
        bits &= ~(1 << num)


    elif o == "check":
        # print(o)
        if bits & ( 1<<num ):
            print(1)
        else:
            print(0)


    elif o == "toggle":
        # print(o)
        bits ^= (1 << num) 