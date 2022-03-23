
import sys
 
sys.setrecursionlimit(10000)

input = lambda : sys.stdin.readline().rstrip()



INF = float('inf')

N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input())))


for i in range(1, N):
    for j in range(1, M):
        if board[i][j] and board[i-1][j-1] and board[i-1][j] and board[i][j-1]:
            value = min(board[i-1][j-1], board[i-1][j], board[i][j-1])
            board[i][j] = value + 1 
            
res = 0
for i in range(N):
    for j in range(M):
        res = max(res, board[i][j])
 

answer = res * res
print(answer)