# https://programmers.co.kr/learn/courses/30/lessons/84512?language=python3
# 1
arr = [0] * (5) 
char = ["A", "E", "I", "O", "U"]   
cnt = -1
answer = 0

def go(index, word):
    global cnt, answer

    cnt += 1
    temp = ""
    for i in range(index):
        temp += arr[i]
    if temp == word:
        answer = cnt
        return

    if index == 5:
        return

    for i in range(5):
        arr[index] = char[i]
        go(index+1, word)


def solution(word):

    go(0, word)

    return answer

# 2 product

from itertools import product

def solution(word):
    answer = 0
    a = []
    
    for i in range(1, 6):
        for j in product("AEIOU", repeat=i):
            print(j)
            a.append("".join(j))
    
    a.sort()

    return a.index(word)+1