# max heap 만들기

f = open("main.txt", 'r')
input = lambda : f.readline().rstrip()


N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

def heapify(arr, index, heap_size):
    p_index = index
    left_index = index*2+1
    right_index = index*2+2

    if left_index < heap_size and arr[left_index]>arr[p_index]:
        p_index = left_index
    if right_index < heap_size and arr[right_index]>arr[p_index]:
        p_index = right_index
    
    if p_index != index:
        arr[p_index],arr[index] = arr[index],arr[p_index]
        heapify(arr, p_index, heap_size)


def max_heap(arr):

    for i in range( N // 2 -1, -1 , -1):
        heapify(arr , i, N)

    return arr


ans = max_heap(arr)

for a in ans:
    print(a)