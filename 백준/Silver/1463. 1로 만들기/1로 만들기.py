import sys

input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)

for i in range(2, N+1):
    temp = [dp[i - 1]]
    if i % 2 == 0:
        temp.append(dp[i // 2])
    if i % 3 == 0:
        temp.append(dp[i // 3])
    dp[i] = min(temp) + 1
print(dp[N])