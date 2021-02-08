# for else를 이용해
# for 루프중간에 break로 빠져나왔는지 아닌지 판단할 수 있다.

arr = []
for i in range(5):
    arr.append(int(input()))
    
num = 1

for n in arr:
    num *= n
    
    temp = num ** (1/2)
    if temp == int(temp):
        print('found')
        break   

else:
    print('not found')
    
    
    