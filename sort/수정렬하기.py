from collections import deque
import sys
sys.setrecursionlimit(10000000)
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
arr = [0]

def heapify(index, size):
    p_index = index
    left, right = p_index*2, p_index*2+1
    if left <= size and arr[left] < arr[p_index]:
        p_index = left
    if right <= size and arr[right] < arr[p_index]:
        p_index = right
    if p_index != index:
        arr[index],arr[p_index]=arr[p_index],arr[index]
        heapify(p_index,size)

for i in range(N):
    arr.append(int(input()))
    L = len(arr)-1
    while L != 1:
        p_index = L // 2
        if arr[p_index] > arr[L]:
            arr[p_index],arr[L]=arr[L],arr[p_index]
            L = L // 2
        else:
            break

# @,,@
index = 1
for i in range(N, 0, -1):
    # 시작 번호 0번 아님 1번임
    # arr[i],arr[0] = arrr[0],arr[1]
    arr[i],arr[1]=arr[1],arr[i]
    heapify(1, N-index)
    index += 1

for i in range(N, 0, -1):
    print(arr[i])

