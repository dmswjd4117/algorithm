def solution(skill, trees):
    answer = 0
    leng = len(skill)
    
    for tree in trees: # "BACDE", "CBADF", "AECB", "BDA"
        order = [30] * leng
        index = 0
        for i in range(len(skill)): # 3개
            for j in range(len(tree)): 
                if tree[j] == skill[i]:
                    order[index] = j
            index += 1
        if order == sorted(order):
            answer += 1
                    
            