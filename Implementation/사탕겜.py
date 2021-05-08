

N = int(input())
board = []
for i in range(N):
    board.append(list(input()))

def find():
    res = 1
    for i in range(N):
        count = 0
        color = board[i][0]
        for j in range(N):
            if color == board[i][j]:
                count += 1
            else:
                color = board[i][j]
                count = 1
            res = max(count, res)

    for i in range(N):
        count = 0
        color = board[0][i]
        for j in range(N):
            if color == board[j][i]:
                count += 1
            else:
                color = board[j][i]
                count = 1
            res = max(count, res)

    return res  


answer = 0
for i in range(N):
    for j in range(N):

        tx = i
        ty = j + 1
        if ty < N and board[i][j] != board[tx][ty] :
            board[tx][ty], board[i][j] = board[i][j], board[tx][ty]

            answer = max(answer, find())
            board[tx][ty], board[i][j] = board[i][j], board[tx][ty]

     
        tx = i+1
        ty = j
        if tx < N and board[i][j] != board[tx][ty]:
            board[tx][ty], board[i][j] = board[i][j], board[tx][ty]   

            answer = max(answer, find())
            board[tx][ty], board[i][j] = board[i][j], board[tx][ty]


print(answer)