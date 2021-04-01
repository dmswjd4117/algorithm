cnt = 0
def go(index, M, numbers, target):
    global cnt
    if index == M:
        if target == 0:
            cnt += 1
        return 
    
    # -1 * 숫자
    go(index+1, M, numbers, target-numbers[index])
    
    # 1 * 숫자
    go(index+1, M, numbers, target+numbers[index])
    
    
def solution(numbers, target):
    global cnt

    go(0, len(numbers), numbers, target)
    
    return cnt