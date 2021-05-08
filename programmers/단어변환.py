MAX = 987654321

def check(A, B):
    cnt = 0
    for i in range(len(A)):
        if A[i] != B[i]: cnt += 1
        if cnt >= 2: return False
    return True

def solution(begin, target, words):
    ans = MAX
    vis = [False] * 60
    N = len(words)
    
    def go(cur, cnt):
        nonlocal ans
        if cur == target:
            ans = min(ans, cnt)
            return True
        if cnt == N:
            return False

        for i in range(N):
            if vis[i]: continue
            if not check(cur, words[i]) : continue
            vis[i] = True
            go(words[i], cnt + 1)
            vis[i] = False
            
        return False
    
    go(begin, 0)
    
    if ans == MAX: ans = 0
    return ans
