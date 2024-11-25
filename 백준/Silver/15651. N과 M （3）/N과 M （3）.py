import sys
input = sys.stdin.readline


def backtracking(N, M, lst):
    if len(lst) == M:
        print(*lst)
        return

    for i in range(1, N + 1):
        lst.append(i)
        backtracking(N, M, lst)
        lst.pop()


N, M = map(int, input().split())
backtracking(N, M, [])
