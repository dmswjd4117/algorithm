def lower(user_arr, start, end , target):
    mid = (start + end) // 2
    if start >= end:
        return end
    
    mid_value = user_arr[mid]
    
    if mid_value >= target:
        return lower(user_arr, start, mid, target)
    
    return lower(user_arr, mid+1, end, target)

scoreMap = dict([])

def dfs(index, arr, string):
    if index == 4:
        score = int(arr[4])
        if string in scoreMap:
            scoreMap[string].append(score)
        else:
            scoreMap[string] = [score]
        return
    
    dfs(index+1, arr, string+'-')
    dfs(index+1, arr, string+arr[index])
    

    
def solution(info_user_arr, query_arr):
    answer = []
    
    for info in info_user_arr:
        splited = info.split()
        dfs(0, splited, "")
        
    for string in scoreMap:
        scoreMap[string].sort()
 
        
    for query in query_arr:
        query = query.replace("and", "").split()
        string = "".join(query[0:4])
        score = int(query[4])
        if string in scoreMap:
            user_arr = scoreMap[string]
            low_index = lower(user_arr, 0, len(user_arr), score)
            res = len(user_arr) - low_index
            answer.append(res)
        else:
            answer.append(0) # !!.. 
    
    return answer


