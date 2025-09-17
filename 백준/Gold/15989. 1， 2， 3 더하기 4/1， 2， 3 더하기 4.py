import sys

input = sys.stdin.readline

T = int(input())
num_list = [int(input()) for _ in range(T)]

dp = [1 for _ in range(10001)]

for i in range(2, max(num_list) + 1):
    dp[i] = 1 + dp[i - 2]

for j in range(3, max(num_list) + 1):
    dp[j] += dp[j - 3]

for num in num_list:
    print(dp[num])
