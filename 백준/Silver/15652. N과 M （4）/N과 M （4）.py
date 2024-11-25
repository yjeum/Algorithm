import sys
input = sys.stdin.readline


def backtracking(N, M, cur, lst):
    if len(lst) == M:
        print(*lst)
        return

    for i in range(cur, N + 1):
        lst.append(i)
        backtracking(N, M, i, lst)
        lst.pop()


N, M = map(int, input().split())
backtracking(N, M, 1, [])
