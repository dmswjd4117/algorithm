N = int(input())
M = int(input())

if M == 0:
  nums = []

else :
  nums = list( map(int, input().split()) )


# 부러져 있으면 true 멀쩡하면 false
arr = [0] * 10
for num in nums:
  arr[num] = 1 

# 숫자에 해당하는 버튼들이 부서졌는지 아닌지 체크
def check(n):
  temp = list(map(int, str(n)))
  for i in temp:
    if arr[i] == 1 :
      return False
  return len(temp)

# 0부터 100000 + 1 까지 
res = abs(N - 100)
for index in range(0, 1000000 + 1):
  count = check(index)
  if count > 0:
    temp = abs(N - index) + count 
    if res > temp :
      res = temp
    
print(res)