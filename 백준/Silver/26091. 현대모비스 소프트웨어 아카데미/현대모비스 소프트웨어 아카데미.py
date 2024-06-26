import sys

input = sys.stdin.readline

N, M = map(int, input().split())
ability = list(map(int, input().split()))

ability.sort()

start, end = 0, N - 1

cnt = 0

while start < end:

    for cur in range(start, end):
        if ability[end] + ability[cur] >= M:
            cnt += 1
            start = cur + 1
            end -= 1
            break
    else:
        break

print(cnt)
