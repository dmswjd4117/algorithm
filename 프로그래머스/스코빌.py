import heapq

def solution(scos, K):
    answer = 0
    heapq.heapify(scos)
    while 1:
        if len(scos) == 1:
            return -1
        a = heapq.heappop(scos)
        b = heapq.heappop(scos)
        heapq.heappush(scos, a+b*2)
        answer += 1
        
        flag = 1
        for num in scos:
            if num < K:
                flag = 0
                break
        if flag:
            return answer
    return answer

a = solution([1, 2, 3, 9, 10, 12] , 7)

print(a)