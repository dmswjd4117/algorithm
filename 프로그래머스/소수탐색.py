from itertools import permutations

def solution(numbers):
    answer = 0
    length = len(numbers)
    
    s = set()
    for count in range(1,length+1):
        s |= set(map(int, map("".join, permutations(numbers, count))))
        
    end = max(s)
    s -= {0,1}
    for index in range(2, end+1):
        s -=  set(range(index*2, end+1, index))
    
    answer = len(s)
    return answer

