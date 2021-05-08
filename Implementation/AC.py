from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

f = open("./main.txt", "r")
input = lambda : f.readline().rstrip()

FRONT = 1
BACK = 2

test = int(input())

for _ in range(test):
    # 명령
    p = list(input())
    #숫자 개수
    n = int(input())
    # 정수들
    string = input()[1:-1]
    nums = []
    if string:
        nums = deque(string.split(","))

    env = FRONT
    for index in range(len(p)):
        order = p[index]
        if order == 'R':
            env = 3 - env
        elif order == 'D':
            if not nums:
                print("error")
                break
            if env == FRONT:
                nums.popleft()
            else:
                nums.pop()
    else:
        if env == BACK:
            print('['+ ','.join(list(nums)[::-1])+ ']')
        else:
            print('[' + ','.join(nums) + ']')