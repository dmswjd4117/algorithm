# 2
import heapq 


def solution(jobs):
    answer = 0
    
    que = []
    
    jobs.sort()
    cur_time = 0
    job_index = 0
    
    while job_index < len(jobs) or que:
        
        while job_index < len(jobs) :
            j_start, j_cost = jobs[job_index]
            if j_start <= cur_time:
                heapq.heappush(que, (j_cost, j_start))
                job_index += 1
            else:
                break
        
        if not que:
            cost = jobs[job_index][1]
            start = jobs[job_index][0]
            cur_time = start + cost
            job_index += 1
            
            # print(cur_time , cost)
            answer += cur_time - start
            
        else:
            top_cost, top_start = heapq.heappop(que)
            cur_time += top_cost
            
            # print(cur_time, top_cost)
            answer += cur_time - top_start
    
    answer = answer // len(jobs)
    
    return answer

 
# 1
import heapq 

LEN =  500002

def solution(jobs):
    answer = 0
    
    que = []

    
    disk_time = 0
    job_index = 0
    
    jobs.sort()
    
    for cur_time in range(LEN):
        
        while job_index < len(jobs):
            start, cost = jobs[job_index]
            if start <= cur_time:
                heapq.heappush(que, (cost, start))
                job_index += 1
            else:
                break
        
        if disk_time != 0:
            disk_time -= 1
            
        elif disk_time == 0 and que:
            que_cost, que_start = heapq.heappop(que)
            disk_time = que_cost
            
            temp = cur_time + disk_time - que_start
            answer += temp
            
            disk_time -= 1
                        
    
    answer = answer // len(jobs)
    
    return answer

 