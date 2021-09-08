import re
from collections import Counter, defaultdict

# 1
def solution(s):
    answer = []
    arr  = s[1:-1]
    check = dict()
    num = ""
    for index, c in enumerate(arr):
        if c == "{":
            continue

        if c.isdigit():
            num += c

        if c == "}":
            if num in check:
                check[num] += 1
            else:
                check[num] = 1
            num = ""

        if c == ",":
            if num != "":
                if num in check:
                    check[num] += 1
                else:
                    check[num] = 1
            num = ""

    res = sorted(check.items(), key=lambda x:x[1], reverse=True)
    for key, item in res:
        answer.append(int(key))
    return answer

# 2 
def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    s.sort(key = len)
    check = set()
    
    for string in s:
        numbers = string.split(",")
        for num in numbers:
            if num not in check:
                check.add(num)
                answer.append(int(num))

    return answer

# 3
def solution(s):
    answer = []
    s = s[2:-2]
    arr = s.split("},{")
    diction = defaultdict(lambda : 0)
    for string in arr:
        nums = string.split(",")
        for num in nums:
            diction[num] += 1
    res = sorted(diction.items(), key=lambda x: x[1], reverse=True)
    
    for key, value in res:
        answer.append(int(key))
        
    return answer
