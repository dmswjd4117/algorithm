# 이산수학 5.2.2
#a의 n승을 log시간안에 계산하는 알고리즘

f = open("./main.txt", "r")
input = lambda: f.readline().rstrip()


def func(a, n):
    res = 1
    x = a

    while n != 0:
        na = n % 2
        n = n // 2
        if na == 1:
            res = res * x
        x = x ** 2

    return res


print(func(2, 7))