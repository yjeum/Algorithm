import sys
input = sys.stdin.readline

N = int(input())
minutes = list(map(int, input().split()))
minutes.sort()

min_minute = 0
for i in range(N):
    min_minute += minutes[i] * (N - i)
print(min_minute)