import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
lst = list(map(int, input().split()))

# 초기 세팅
min_value = max(lst[0], N - lst[-1])

# 구현
before = 0
for cur in lst:
    min_value = max(min_value, int((cur - before + 1) // 2))
    before = cur
print(min_value)
