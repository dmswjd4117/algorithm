## 1

my_str = list(input().strip())

counts = {}
for i in my_str:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

counts = sorted(counts.items(), key= lambda x: x[1], reverse = 1)

big = counts[0][1]
ans = []

for arr in counts:
    if arr[1] == big:
        ans.append(arr[0])
    else:
        break
        
ans.sort()
print(''.join(ans))
    
    
## 2

from collections import Counter

my_list = list(input().strip())

counter = sorted(Counter(my_list).items(),
                key = lambda x : x[1],
                reverse = 1)

big = counter[0][1]
ans = []
for arr in counter:
    if arr[1] == big:
        ans.append(arr[0])
    else:
        break
        
ans.sort()
print(''.join(ans))
