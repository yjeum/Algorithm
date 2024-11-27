import sys
input = sys.stdin.readline


def backtracking(lst, order):
    if len(lst) == M:
        print(*lst)
        return

    cur = 0
    for i in range(order, N):
        if cur != num_lst[i]:
            cur = num_lst[i]
            lst.append(num_lst[i])
            backtracking(lst, i)
            lst.pop()


N, M = map(int, input().split())
num_lst = list(map(int, input().split()))
num_lst.sort()
backtracking([], 0)
