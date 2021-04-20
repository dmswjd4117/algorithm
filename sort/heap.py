# 0번, 1번, ---- 
f = open("main.txt", 'r')
input = lambda : f.readline().rstrip()


N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

# O(log(heap_size)) 대략 o(logN)
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


def heap_sort(arr):

    for i in range( N // 2 -1, -1 , -1):
        heapify(arr , i, N)

    for i in range(N-1, 0, -1):
        # 루트 노드 빼고 max_heap 충족한다.
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr, 0, i)
        
    
    return arr


ans = heap_sort(arr)

for a in ans:
    print(a)


# 2 1번, 2번 ....

import sys
input = lambda : sys.stdin.readline().rstrip()

f = open("main.txt", 'r')
input = lambda : f.readline().rstrip()

N = int(input())
arr = [0]
for i in range(N):
    arr.append(int(input()))

# O(log(heap_size)) 대략 o(logN)
def heapify(arr, index, heap_size):
    p_index = index
    left_index = index*2
    right_index = index*2+1

    if left_index <= heap_size and arr[left_index]>arr[p_index]:
        p_index = left_index
    if right_index <= heap_size and arr[right_index]>arr[p_index]:
        p_index = right_index
    
    if p_index != index:
        arr[p_index],arr[index] = arr[index],arr[p_index]
        heapify(arr, p_index, heap_size)



def heap_sort(arr):

    for i in range( N // 2 , 0 , -1):
        heapify(arr , i, N)


    for i in range(N , 0, -1):
        # 루트 노드 빼고 max_heap 충족한다.
        arr[1],arr[i] = arr[i],arr[1]
        heapify(arr, 1, i-1)
         
    return arr


heap_sort(arr)

for i in range(1,N+1):
    print(arr[i])

