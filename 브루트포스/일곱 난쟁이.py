arr = []
for i in range(9):
    arr.append(int(input()))
arr.sort()

check = [False] * 10
answer = [0] * 10

M = 7
def find(index, selected):
    if selected == M:
        # 0 부터 M-1번 까지 숫자
        if sum(answer) == 100:
            for i in range(0, M):
                print(answer[i])
            exit(0)
        return

    if index >= 9:
        return 

    answer[selected] = 0
    find(index+1, selected)

    answer[selected] = arr[index]
    find(index+1, selected+1)

print()
find(0, 0)