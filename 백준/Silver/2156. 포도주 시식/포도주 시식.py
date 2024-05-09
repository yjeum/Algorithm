import sys


input = sys.stdin.readline

N = int(input())

grape = []

for _ in range(N):
    grape.append(int(input()))

dp = [0] * N
dp[0] = grape[0]

if N > 1:
    dp[1] = grape[0] + grape[1]

if N > 2:
    dp[2] = max(grape[0] + grape[2], grape[1] + grape[2])

for i in range(3, N):
    dp[i] = max(max(dp[:i-1]), max(dp[:i-2]) + grape[i-1]) + grape[i]

print(max(dp))
