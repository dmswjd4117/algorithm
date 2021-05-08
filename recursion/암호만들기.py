
L, C = map(int, input().split())

arr = list(input().split())
arr.sort()

aeiou = ['a', 'e', 'i', 'o', 'u']
res = [0] * 20


def find(index, a, b):
    if(index == L):
        if a >= 1 and b >= 2 : 
            for i in range(L):
                print(res[i],end="")
            print()
        return 

    for i in range(C):
        # 감소하면 아웃
        if(index != 0 and res[index-1] >= arr[i]):
             continue

        res[index] = arr[i]
        if res[index] in aeiou :
            find(index+1, a+1, b)
        else:
            find(index+1, a, b+1)


find(0, 0, 0)