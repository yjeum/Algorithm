import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))

    max_v = max(q)
    cur = 0
    cnt = 1

    while True:

        if q[cur] == max_v:
            if cur == M:
                print(cnt)
                break
            q[cur] = 0
            cnt += 1
            max_v = max(q)

        cur = (cur + 1) % N
