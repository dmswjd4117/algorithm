def convert(temp):
    answer = ''
    if 'a' <= temp[0] <= 'z':
        answer += temp[0].upper()
    else:
        answer += temp[0]
    temp = temp.lower()
    answer += temp[1:]
    return answer

def solution(s):
    answer = ''
    flag = False
    temp = ''
    for i in range(len(s)):
        if s[i] == ' ':
            if flag:
                answer += convert(temp)
                temp = ''
                flag = False 
            answer += ' '
        else:
            temp += s[i]
            flag = True
            
    if flag:
        answer += convert(temp)
        
    return answer