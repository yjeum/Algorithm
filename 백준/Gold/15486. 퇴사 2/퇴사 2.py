import sys

input = sys.stdin.readline

N = int(input())
table = [map(int, input().split()) for _ in range(N)]
dp = [0]*(N + 1)

day = 1
for t, p in table:
    dp[day] = max(dp[day - 1], dp[day])
    if day + t - 1 <= N:
        dp[day + t - 1] = max(dp[day + t - 1], dp[day - 1] + p)
    day += 1
print(max(dp))

