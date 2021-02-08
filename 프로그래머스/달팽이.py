from itertools import chain
moving = [[1, 0], [0, 1], [-1, -1]]

def moveIndex(n):
    if n == 2:
        return 0
    return n+1

def solution(n):
    answer = []
    N = n
    graph = [[ 0 for j in range(i+1)] for i in range(n)]
    x, y = -1, 0
    index = 0
    num = 0
    while(n != 0):
        for i in range(n):
            x += moving[index][0]
            y += moving[index][1]
            num += 1
            graph[x][y] = num
        
        index = moveIndex(index)
        n -= 1
    
    
    # for i in range(N):
    #     for j in range(i+1):
    #         answer.append(graph[i][j])

    answer = list(chain(*graph))

    return answer

