# https://steady-coding.tistory.com/187
 
import sys
 
sys.setrecursionlimit(10000)

input = lambda : sys.stdin.readline().rstrip()
 
INF = float('inf')


# f = open("./file.txt", "r")
# input = lambda: f.readline().rstrip()

dp = [
    [0] * (61)
    for _ in range(61)
]  

dp[1][0] = 1
dp[1][1] = 1
for i in range(2, 61):
    for j in range(0,i+1):
        if j == 0: 
            dp[i][0] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
# for i in range(0, 10):
#     for j in range(0, 10):
#         print(dp[i][j], end=' ')
#     print()

while True:
    n = int(input())
    if not n: break
    t = 2 * n
    
    print(dp[n][n])
    

    
 
        
 
 
 

# from copy import deepcopy
# import sys
 
# sys.setrecursionlimit(10000)

# input = lambda : sys.stdin.readline().rstrip()

# f = open("./file.txt", "r")
# input = lambda: f.readline().rstrip()


# INF = float('inf')


    
    
# while True:
#     n = int(input())
#     if not n: break
    
#     res = 0
#     def find(cnt, one, half, string):
#         global res
#         if cnt == 2 * n:
#             res += 1
#             return
 
         
#         if one >= 1:
#             find(cnt + 1, one-1, half+1, string+"W")
        
#         if half >= 1:
#             find(cnt + 1, one, half-1, string+"H")
            
            
#     find(0, n, 0, "")
#     print(res)
 