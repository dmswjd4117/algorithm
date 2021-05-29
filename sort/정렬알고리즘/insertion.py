# 삽입정렬 (오름차순)
import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

f = open("./main.txt", "r")
input = lambda: f.readline().rstrip()

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))


for point in range(1, N):
    # 앞에서 부터 검사하면 큰 데이터들을 한칸씩
    # 뒤로 shift해야한다.
    # 따라서 앞의 모든 데이터들을 건들여야한다.

    # 뒤에서부터 검사하면 point보다 큰 데이터들은
    # swap해주고, 작은 데이터를 만나면 반복문이 끝나기때문에
    # 더 효율적으로 검사할 수 있다.

    for i in range(point-1, -1, -1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            break


for a in arr:
    print(a)

# 최선의 경우 o(n)
# 최악의 경우 O(n^2)


# 2
N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

for i in range(1, N):
    j = i-1
    key = arr[i]

    while j>=0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = key

for a in arr:
    print(a)
    
