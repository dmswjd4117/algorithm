def solution(books):
    answer = True
    d = {}
    for book in books:
        d[book] = 1
    
    for i in range(len(books)):
        temp = ''
        for j in range(len(books[i])):
            temp += books[i][j]
            if temp == books[i]: continue
            if temp in d: return False
            
    return True