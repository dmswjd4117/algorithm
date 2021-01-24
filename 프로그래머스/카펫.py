def solution(brown, yellow):
    answer = []
    hap = int((brown-4)/2)
    a, b = hap-1 ,1
    while a != 0:
        if a*b == yellow:
            answer = [a+2, b+2]
            return answer
        b += 1
        a -= 1
        
    return answer