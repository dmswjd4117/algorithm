# 문자열의 위치를 인자로 넘기기
aeiou = ['a', 'e', 'i', 'o', 'u']


L, C = map(int, input().split())

arr = list(input().split())
arr.sort()

def check(string):
    mo = 0
    za = 0
    for c in string:
        if c in aeiou:
            mo += 1
        else:
            za += 1
    return mo >= 1 and za >= 2


# index = 문자열의 위치
def find(index, string):
    if(len(string) == L):
        if check(string):
            print(string)
        return
    
    if index >= C:
        return 

    find(index+1, string + arr[index])
    find(index+1, string)

find(0,"")