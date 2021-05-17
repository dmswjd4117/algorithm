from functools import cmp_to_key

def comp(x, y):
    a, b = int(x+y), int(y+x)
    if a > b:
        return -1
    return 1

def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))
    
    numbers.sort( key = cmp_to_key(comp))
    
    answer = str(int("".join(numbers)))
    
    return answer