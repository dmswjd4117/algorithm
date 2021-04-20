
S = input()

dic = {}

for c in S:
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1

#                             !!!!!!!!!! 
for index in range(ord('a'), ord('z')+1):
    alpha = chr(index)
    if alpha in dic:
        print(dic[alpha], end=" ")
    else:
        print(0, end=" ")


# 2

S = input()

count = [0] * 26

for alpha in S:
    index = ord(alpha) - ord('a')
    count[index] += 1

for n in count:
    print(n, end=" ")