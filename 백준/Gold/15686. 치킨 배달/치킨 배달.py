import sys
from itertools import combinations

input = sys.stdin.readline


def length(pick):
    pick_dis = 0
    for hi, hj in house:
        cur_dis = 1e9
        for pi, pj in pick:
            temp = abs(pi - hi) + abs(pj - hj)
            cur_dis = min(cur_dis, temp)
        pick_dis += cur_dis

        if pick_dis > min_len:
            return min_len
    return pick_dis


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

house = []
store = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            store.append((i, j))

min_len = 1e9
for pick in combinations(store, M):
    min_len = min(length(pick), min_len)

print(min_len)
