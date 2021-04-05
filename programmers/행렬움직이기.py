# MAX = 10 ** 9
arr = []

def move(m):
    x1, y1 = m[0]-1, m[1]-1
    x2, y2 = m[2]-1, m[3]-1

    x_move = x2 - x1
    y_move = y2 - y1

    move = 1
    x, y = x1, y1

    cnt = 0
    temp1 = arr[x][y]
    ans = temp1
    while cnt != 2:
        for i in range(y_move):
            y += 1 * move
            temp2 = arr[x][y]
            arr[x][y] = temp1
            temp1 = temp2
            ans = min(ans, temp1)
            # print(arr[x][y])

        for i in range(x_move):
            x += 1 * move
            temp2 = arr[x][y]
            arr[x][y] = temp1
            temp1 = temp2
            ans = min(ans, temp1)
            # print(arr[x][y])

        move *= -1
        cnt += 1

    return ans


def solution(rows, columns, queries):
    global arr
    answer = []

    arr = [[0]*columns for _ in range(rows)]
    index = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = index
            index += 1

    # move(queries[0])
    # for i in range(rows):
    #     for j in range(columns):
    #         print(arr[i][j], end=' ')
    #     print()


    for m in queries:
        a = move(m)
        answer.append(a)

    return answer