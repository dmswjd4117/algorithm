def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    acc = [
        [0] * (m+1)
        for _ in range(n+1)
    ]
    
    def printArr(arr):
        for i in range(n):
            for j in range(m):
                print(arr[i][j],end=' ')
            print()
        print()
        
    for type, r1, c1, r2, c2, degree in skill:
        value = degree
        if type == 1: value = -value
        
        acc[r1][c1] += value
        acc[r1][c2+1] -= value
        acc[r2+1][c1] -= value
        acc[r2+1][c2+1] += value
            
        
    for i in range(n):
        for j in range(1, m):
            acc[i][j] += acc[i][j-1] 
            
    for i in range(m):
        for j in range(1, n):
            acc[j][i] += acc[j-1][i]
    
    
    for i in range(n):
        for j in range(m):
            board[i][j] += acc[i][j]
            if board[i][j] > 0:
                answer += 1
        
    return answer