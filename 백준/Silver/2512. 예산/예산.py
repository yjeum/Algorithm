import sys
input = sys.stdin.readline

N = int(input())
budget_lst = list(map(int, input().split()))
total = int(input())

start, end = 1, max(budget_lst)

while start <= end:
    mid = (start + end) // 2
    temp_budget = 0

    for budget in budget_lst:
        if budget <= mid:
            temp_budget += budget
        else:
            temp_budget += mid

    if temp_budget <= total:
        start = mid + 1
    else:
        end = mid - 1
print(end)
