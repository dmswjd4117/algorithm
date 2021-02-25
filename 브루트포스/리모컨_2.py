MAX = 10000000

N = int(input())
leng = len(str(N))

M = int(input())
if(M):
    broken = list(map(int, input().split()))
else:
    broken = []

buttons = [x for x in range(0, 10) if x not in broken]

## 1
ans = [0] * 100
close = MAX
def find(index, M):
    global close
    if index == M:
        num = ""
        for i in range(M):
            num += str(ans[i])

        num = int(num)
        # print(abs(close-N) , abs(num-N))
        if abs(close-N) > abs(num-N):
            close = num

        return

    for i, button in enumerate(buttons):
        ans[index] = button
        find(index+1, M)


if leng >= 2:
    for i in range(leng-1, leng+2):
        find(0, i)
elif leng == 1:
    for i in range(1, leng+2):
        find(0, i)

ans1 = len(str(close)) + abs(close-N)

## 2
ans2 = abs(N - 100)


# print(close,  abs(close-N))
# print(ans1, ans2)

if close == MAX:
    print(ans2)
else:
    print(min(ans1, ans2))