import sys

def plus(num):
    dp = [0] * num
    if num >= 1:
        dp[0] = 1
    if num >= 2:
        dp[1] = 2
    if num >= 3:
        dp[2] = 4
    if num >= 4:
        for i in range(3,num):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    return dp[-1]


N = int(input())

for _ in range(N):
    num = int(input())
    print(plus(num))