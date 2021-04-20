f = open("main.txt", 'r')
input = lambda : f.readline().rstrip()


N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

def merge(start, mid, end):
    index = 0
    ans =[0] * (end-start+2)
    left = start
    right = mid+1

    while True:
        if left > mid or right > end: break
        if arr[left] < arr[right]:
            ans[index] = arr[left]
            left += 1
            index += 1
        else:
            ans[index] = arr[right]
            right += 1
            index += 1
    
    for i in range(left, mid+1):
        ans[index] = arr[i]
        index += 1
    
    for i in range(right, end+1):
        ans[index] = arr[i]
        index += 1

    j = 0
    for i in range(start, end+1):
        arr[i] = ans[j]
        j += 1
    
    
def mergeSort(start, end):
    if start >= end: return
    # start == end 인경우 무한재귀에 들어감 

    mid = (start+end)//2
    mergeSort(start, mid)
    mergeSort(mid+1, end)
    merge(start, mid, end)


mergeSort(0, N-1)


for a in arr:
    print(a)