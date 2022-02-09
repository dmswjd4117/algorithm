import sys
 
input = lambda : sys.stdin.readline().rstrip()
 

f = open("./file.txt", "r")
input = lambda: f.readline().rstrip()
 
INF = float("inf")

N = int(input())

arr = list(map(int, input().split()))
arr.sort()


left ,right = 0, N-1

res = [0, 0]
answer = INF
 
while True:
    if left == right:
        break

 
    temp = arr[left] + arr[right]
    if abs(temp) == 0:
        res = [arr[left], arr[right]]
        break
    elif abs(temp) < answer:
        answer = abs(temp)
        res = [arr[left], arr[right]]

    if temp < 0:
        left += 1
    else: 
        right -= 1

res.sort()
print(res[0], res[1])