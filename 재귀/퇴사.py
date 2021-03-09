

N = int(input())

days = []
pays = []
for i in range(N):
    a, b = map(int, input().split())
    days.append(a)
    pays.append(b)

ans = 0
moneys = [0] * 100
def find(index, day):
    global ans
    # 0일부터 6일까지 가능, 7일부터는 상담불가능
    if day >= N:
        hap = 0
        for i in range(N):
            hap += moneys[i]
        if hap > ans:
            ans = hap
        return
    
    # 0일에서 6일이내에 있다면,
    if (day + days[day] -1) <= N-1: 
        moneys[index] = pays[day]
        find(index+1, day + days[day])
        moneys[index] = 0
    
    find(index, day+1)
    


find(0, 0)
print(ans)


## 2


N = int(input())

days = [0] * (N+1)
pays = [0] * (N+1) 
for i in range(1,N+1):
    days[i], pays[i] = map(int, input().split())

ans = 0
moneys = [0] * 100
def find(day, hap):
    global ans
    if day == N + 1:
        ans = max(ans, hap)
        return
    if day > N + 1:
        return

    find(day+1, hap)
    find(day+days[day], hap+pays[day])


find(1, 0)
print(ans)
