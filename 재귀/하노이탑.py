N = int(input())
count = 0
res = []

def func(index, start, middle, end):
    global count
    if(index == 1):
        # print(start , end)
        res.append([start, end])
        count += 1
        return 
    
    func(index-1, start , end, middle)
    # print(start, end)
    res.append([start, end])
    count += 1
    func(index-1, middle, start, end)


func(N, 1, 2, 3)
print(count)   
for i in range(len(res)):
    print(res[i][0], res[i][1])