import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    values = list(map(int, input().split()))

    max_val = values[N - 1]
    profit = 0
    for value in values[::-1]:

        if max_val <= value:
            max_val = value
        else:
            profit += max_val - value
    print(profit)
