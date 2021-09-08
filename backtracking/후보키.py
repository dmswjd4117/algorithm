from itertools import permutations, chain, combinations

N = 0
arr = []
ans_set = set([])
relation = []
answer = 0



def check(arr):
    if not arr:
        return False
    check_set = set([])
    for i in range(len(relation)):
        temp = ""
        for j in arr:
            temp += relation[i][j]
        if temp in check_set:
            return False
        check_set.add(temp)
    return True

def isin(answer_set, arr):
    for i in range(1, N+1):
        coll = list(combinations(arr, i))
        for nums in coll:
            string = "".join(map(str, nums))
            if string in answer_set:
                return True
    return False
            
def solution(parma_relation):
    global N, arr, relation, answer
    
    answer = 0
    answer_set = set()
    N = len(parma_relation[0])
    arr = [0] * (N)
    relation = parma_relation
    
    arr = [x for x in range(N)]
    
    for i in range(1, N+1):
        coll = list(combinations(arr, i))
        for nums in coll:
            if isin(answer_set, nums):
                continue
            if check(nums):
                answer_set.add("".join(map(str, nums)))

    answer = len(answer_set)
    
    return answer


