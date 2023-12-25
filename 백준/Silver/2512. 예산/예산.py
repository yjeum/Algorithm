import sys

input = sys.stdin.readline

N = int(input())

budget = list(map(int, input().split()))
total = int(input())

start, end = 1, max(budget)

while start <= end:
    mid = (start + end) // 2
    result = 0

    for i in budget:
        if i <= mid:
            result += i
        else:
            result += mid

    if result <= total:
        start = mid + 1
    else:
        end = mid - 1
print(end)
