from collections import deque

N = int(input())

arr = deque(input())

nums = []
for i in range(N):
    nums.append(int(input()))

stack = []

while len(arr) != 0:
    t = arr.popleft()
    if t == '*' :
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)
    elif t == '/' :
        b = stack.pop()
        a = stack.pop()
        stack.append(a / b)
    elif t == '-' :
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)
    elif t == '+':
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)
    else:
        index = ord(t) - 65
        stack.append(nums[index])

print('%.2f'%stack.pop())