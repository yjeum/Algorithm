import sys
input = sys.stdin.readline


def backtracking(lst):
    if len(lst) == M:
        print(*lst)
        return

    cur = 0
    for num in num_lst:
        if num != cur:
            cur = num
            lst.append(num)
            backtracking(lst)
            lst.pop()


N, M = map(int, input().split())
num_lst = list(map(int, input().split()))
num_lst.sort()
backtracking([])
