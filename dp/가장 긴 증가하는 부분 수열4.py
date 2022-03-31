import sys
 

sys.setrecursionlimit(10000)

input = lambda : sys.stdin.readline().rstrip()

 
INF = float('inf')


N = int(input())
arr = list(map(int, input().split()))
sub = [(0, arr[0])]
pre = [0] * (N)

def lower_bound(l, r, arr, key):
    while l < r:
        m = ( l + r ) // 2
        if arr[m][1] < key:
            l = m + 1
        else:
            r = m
    return l


def find(x):
    if x == pre[x]:
        print(arr[x], end=' ')
        return 
    find(pre[x])
    print(arr[x], end=' ')

for i in range(1, N):
    index = lower_bound(0, len(sub), sub, arr[i])
    if index == len(sub):
        sub.append((i, arr[i]))
    else:
        sub[index] = (i, arr[i])
        
    if index == 0:
        pre[i] = i
    else:
        pre[i] = sub[index-1][0]
        

print(len(sub))   
find(sub[-1][0])