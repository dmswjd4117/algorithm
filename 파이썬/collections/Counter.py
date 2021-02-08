from collections import Counter 

my_list = [1, 2, 4, 5, 6, 7, 8, 7, 9, 1, 2, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]


print(Counter(my_list))

# 가장 많이 등장하는 순대로 정렬하기 
# 1
ans = sorted(
 Counter(my_list).items(),
 key = lambda x : x[1], 
 reverse = 1)

print(ans)

# 2
ans = Counter(my_list).most_common()
print(ans)

# 가장 많이 등장한거 1개
big = Counter(my_list).most_common(1)
print(big)