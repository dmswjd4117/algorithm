def go(pre, ino):
    if not pre:
        return

    root = pre[0]
    root_index = ino.index(root)
    #왼쪽 트리 개수
    L = root_index
    #오른쪽 트리 개수
    R = len(ino) - 1 - L

    go(pre[1:L+1], ino[0:root_index])
    go(pre[L+1:], ino[root_index+1: ])

    print(root, end=' ')



T = int(input())

for test in range(T):
    N = int(input())
    pre = list(map(int ,input().split()))
    ino = list(map(int, input().split()))
    go(pre, ino)
