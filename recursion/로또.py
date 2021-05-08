import sys
input = lambda : sys.stdin.readline().rstrip()

f = open("./main.txt", "r")
input = lambda : f.readline().rstrip()


ans = [0] * 6
def go(index, start):
    if index == 6:
        for i in range(6):
            print(ans[i], end=' ')
        print()
        return 

    for i in range(start, N):
        ans[index] = arr[i]
        go(index+1, i+1)


while 1:
    t = list(map(int, input().split()))
    N, arr = t[0], t[1:]
    if N == 0:
        break
    go(0, 0)
    print()



