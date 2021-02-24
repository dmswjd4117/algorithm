def solution(prices):
    answer = []
    size = len(prices)
    
    for i in range(size):
        cnt = 0
        for j in range(i+1, size):
            cnt += 1
            if prices[i] > prices[j]:
                break
                
        answer.append(cnt)
    return answer