import sys

input = lambda : sys.stdin.readline().rstrip()


# f = open("./file.txt", "r")
# input = lambda: f.readline().rstrip()


K = int(input())

arr = list(input().split())

vis = set([])

N = 10
M = K + 1
ans = [0] * (M)


def check(a, c, b):
    if c == '<':
        return a < b
    return a > b

def find_max(index):
    if index == M:
        return "".join(map(str, ans))
    
    for i in range(N-1, -1, -1):
        if i in vis: continue
        vis.add(i)

        if index == 0:
            ans[index] = i
            tmp = find_max(index + 1)
            if tmp: return tmp

        else:
            ans[index] = i
            if check(ans[index-1], arr[index-1], ans[index]):
                tmp = find_max(index + 1)
                if tmp: return tmp

        vis.remove(i)

    return False


def find_min(index):
    if index == M:
        return "".join(map(str, ans))
    
    for i in range(N):
        if i in vis: continue

        vis.add(i)

        if index == 0:
            ans[index] = i
            tmp = find_min(index + 1)
            if tmp: return tmp

        else:
            ans[index] = i
            if check(ans[index-1], arr[index-1], ans[index]):
                tmp = find_min(index + 1)
                if tmp: return tmp
        
        vis.remove(i)

    return False
        

max_ans = find_max(0)
vis = set([])
min_ans = find_min(0)

print(max_ans)
print(min_ans)
 