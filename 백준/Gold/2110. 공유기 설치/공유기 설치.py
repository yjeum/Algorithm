import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = list(int(input()) for _ in range(N))
house.sort()

start, end = 1, (house[-1] - house[0]) // (C - 1)
while start <= end:
    mid = (start + end) // 2
    cur = house[0]
    cnt = 0
    for i in house:
        if i - cur >= mid:
            cnt += 1
            cur = i
            if cnt >= C - 1:
                break

    if cnt >= C - 1:
        start = mid + 1
    else:
        end = mid - 1

print(end)
