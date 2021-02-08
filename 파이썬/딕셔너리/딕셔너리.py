
dict = {'E' : 1, 'A' : 4, 'C' : 3, 'B' : 2}

# print(list(dict.keys()))
# print(list(dict.values()))
# print(list(dict.items()))

# 키캆기준으로 정렬
temp = list(sorted(dict.items()))
print(temp)

print()
print(dict)
# value값으로 정렬
temp = list(sorted(dict.items(), key=lambda x:x[1]))
print(temp)