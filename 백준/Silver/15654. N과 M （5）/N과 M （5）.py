import sys
input = sys.stdin.readline


def backtracking(lst):
    if len(lst) == M:
        print(*lst)
        return

    for i in num_lst:
        if i not in lst:
            lst.append(i)
            backtracking(lst)
            lst.pop()


N, M = map(int, input().split())
num_lst = list(map(int, input().split()))
num_lst.sort()
backtracking([])
