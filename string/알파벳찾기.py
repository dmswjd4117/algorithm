import sys 

input = lambda : sys.stdin.readline().rstrip()

string = input()
ans = []

for i in range(ord('a'), ord('z')+1):
    ans.append(string.find(chr(i)))

for i in ans:
    print(i, end=" ")
