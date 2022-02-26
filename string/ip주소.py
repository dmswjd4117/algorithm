import sys
 
sys.setrecursionlimit(10000)

input = lambda : sys.stdin.readline().rstrip()

INF = float('inf')

def convert(num):
    temp = str(bin(num)[2:])
    r = 8 - len(temp)
    temp = "0" * r + temp
    return temp

def printIp(b):
    res = []
    for i in range(4):
        start = i * 8
        end = start + 8
        res.append(str(int(b[start : end], 2)))
            
    print(".".join(res))


n  = int(input())
ip = [ "" for _ in range(n) ]
for i in range(n):
    s = input().split('.')
    for j in range(4):
        ip[i] += convert(int(s[j]))

 
res = 32
fix = ip[0]
for i in range(1, n):
    temp = 32
    comp = ip[i]
    for j in range(len(fix)):
        if fix[j] != comp[j]:
            temp = j
            break
    res = min(res, temp)
    
M = 32 - res

address = ip[0][0:res] + "0" * (M)
mask = "1" * res + "0" * M

printIp(address)
printIp(mask)

