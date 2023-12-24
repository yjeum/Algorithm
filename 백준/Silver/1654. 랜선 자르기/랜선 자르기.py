import sys

input = sys.stdin.readline

N, K = map(int, input().split())

cable = [int(input()) for _ in range(N)]

start, end = 1, max(cable)

result = 0
while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for i in cable:
        cnt += i // mid

    if cnt >= K:
        start = mid + 1
        result = mid

    else:
        end = mid - 1


print(result)
