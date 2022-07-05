from collections import deque

def toM(time):
    a, b = time.split(":")
    return int(a) * 60 + int(b)

def toHandM(minute):
    h = str(minute // 60)
    m = str(minute % 60)
    if len(h) < 2:
        h = '0' + h
    if len(m) < 2:
        m = '0' + m

    return ":".join([h, m])

def solution(n, t, m, timetable):        
    timetable.sort()
    timetable = list(map(toM, timetable))
    
    time_index = 0
    cur = toM("09:00")
    lines = []
    for i in range(n):
        crew_count = 0
        while crew_count < m and time_index != len(timetable):
            time = timetable[time_index]
            if time <= cur:
                time_index += 1
                if i == n-1:
                    lines.append(time)
            crew_count += 1
        cur += t
    
    last_time = cur - t
    if len(lines) < m:
        return toHandM(last_time)
    return toHandM(lines[-1]-1)