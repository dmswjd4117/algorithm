import sys
input = lambda : sys.stdin.readline().rstrip()


f = open("./main.txt", "r")
input = lambda : f.readline().rstrip()


N = int(input())

arr = list(map(int, input().split()))

nums = [False] * (100000 * 21)

def go(index, hap):
    if index == N:
        nums[hap] = True 
        return
    
    go(index+1, hap)

    go(index+1, hap+arr[index])

go(0, 0)


for index in range(1, 100000 * 21):
    if not nums[index]:
        print(index)
        break

    # if index not in nums:
    #     print(index)
    #     break

# The complexity of in depends entirely on what L is. 
# e in L will become L.__contains__(e).

# See this time complexity document 
# for the complexity of several built-in types.

# Here is the summary for in:

# list - Average: O(n)
# set/dict - Average: O(1), Worst: O(n)
# The O(n) worst case for sets and dicts is very uncommon, 
# but it can happen if __hash__ is implemented poorly.
#  This only happens if everything in your set has the same hash value.
#https://stackoverflow.com/questions/13884177/complexity-of-in-operator-in-python