import sys
input = sys.stdin.readline


def backtracking(lst, order):
    if len(lst) == M:
        print(*lst)
        return

    cur = 0
    for i in range(order, N):
        if num_lst[i] != cur and visited[i] == 0:

            cur = num_lst[i]
            visited[i] = 1
            lst.append(cur)

            backtracking(lst, i + 1)

            lst.pop()
            visited[i] = 0


N, M = map(int, input().split())
num_lst = list(map(int, input().split()))
num_lst.sort()
visited = [0] * N
backtracking([], 0)
