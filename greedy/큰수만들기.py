def solution(number, k):
    answer = ''
    # 총 길이
    n = len(number)
    # 구해야하는 자릿 수
    m = n - k
    
    print(n, m)
    
    def find_max(a, b):
        ans = number[a]
        index = a
        for i in range(a, b+1):
            if number[i] == '9':
                return i
            if ans < number[i]:
                index = i
                ans = number[i]
        return index

    left = -n
    for i in range(-m, 0):
        index = find_max(left, i)
        # print(left, i, number[index])
        answer += number[index]
        left = index+1
        
    return answer