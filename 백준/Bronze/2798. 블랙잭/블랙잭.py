import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
num_lst = list(map(int, input().split()))

max_value = 0
for cards in combinations(num_lst, 3):
    value = sum(cards)

    if value <= M and value > max_value:
        max_value = value

print(max_value)
