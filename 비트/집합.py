import sys 

input = lambda : sys.stdin.readline().rstrip()

M = int(input())

my_set = 0
x = 0

for i in range(M):
    string = input().split(' ')

    order = string[0]
    if len(string) == 2:
        x = int(string[1])

    if order == 'add':
        my_set |= (1 << x)

    elif order == 'remove':
        my_set &= ~(1 << x)

    elif order == 'check':
        if(my_set & (1 << x)):
            print(1)
        else:
            print(0)

    elif order == 'toggle':
        my_set ^= (1 << x)

    elif order == 'all':
        my_set = (1<<21) -1

    elif order == 'empty':
        my_set= 0
