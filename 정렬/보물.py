N = int(input())

A = sorted(list(map(int, input().split())), reverse = 1)

B = sorted(list(map(int, input().split())))

ans = 0
for i in range(N):
    ans += A[i] * B[i]

print(ans)