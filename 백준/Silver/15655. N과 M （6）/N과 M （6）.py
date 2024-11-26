import sys
input = sys.stdin.readline


def backtracking(i, lst):
    if len(lst) == M:
        print(*lst)
        return

    for cur in range(i, N):
        lst.append(num_lst[cur])
        backtracking(cur + 1, lst)
        lst.pop()


N, M = map(int, input().split())
num_lst = list(map(int, input().split()))
num_lst.sort()
backtracking(0, [])
