def solution(v):
    answer = []
    
    x, y = [], []
    for i in range(len(v)):
        for j in range(i+1, len(v)):
            # x값 같다
            if v[i][0] == v[j][0]:
                x = set([i, j])
            # y값 같다
            if v[i][1] == v[j][1]:
                y = set([i, j])
     
    z = x & y
    x = list(x - z)[0]
    y = list(y - z)[0]
    #print(x, y, z)
    answer = [ v[y][0], v[x][1] ]
    return answer


# Counter 

from collections import Counter

def solution(v):
    answer = []
    
    z = zip(*v)
    for arr in z:
        counter = Counter(arr)
        for k in counter:
            if counter[k] == 1:
                answer.append(k)
            
        
    return answer