import sys
input = sys.stdin.readline


def backtraking(lst):
    if len(lst) == M:
        print(*lst)
        return

    for cur in num_lst:
        lst.append(cur)
        backtraking(lst)
        lst.pop()


N, M = map(int, input().split())
num_lst = list(map(int, input().split()))
num_lst.sort()
backtraking([])
