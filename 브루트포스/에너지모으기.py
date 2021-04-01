import sys
sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
vis = [False] * (N+2)


ans = 0
def go(index, hap):
    global ans
    if index == N-2:
        ans = max(ans, hap)
        # print(hap)
        return
    
    for i in range(1, N-1):
        if vis[i]: continue
        vis[i] = True
        left = i-1
        right = i+1

        while vis[left] == True:
            left -= 1
        while vis[right] == True:
            right += 1

        t = arr[left] * arr[right]
        go(index+1, hap+t)

        vis[i] = False



go(0, 0)
print(ans)