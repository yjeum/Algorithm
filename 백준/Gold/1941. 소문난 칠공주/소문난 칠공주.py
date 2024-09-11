from collections import deque

didj = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def check(s):
    visited = [False for _ in range(7)]

    q = deque([s[0]])
    visited[0] = True

    count = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in didj:
            ni, nj = ci + di, cj + dj
            for i in range(7):
                if not visited[i] and s[i] == (ni, nj):
                    visited[i] = True
                    q.append((ni, nj))
                    count += 1

    return count == 7


def dfs(depth):

    global cnt

    if len(s) == 7:
        if member.count("S") >= 4 and check(s):
            cnt += 1
        return

    for i in range(depth, 25):
        x, y = idx[i]
        s.append((x, y))
        member.append(board[x][y])
        dfs(i + 1)
        s.pop()
        member.pop()


board = [list(input()) for _ in range(5)]
idx = [(i, j) for i in range(5) for j in range(5)]
s = []
member = []
cnt = 0

dfs(0)
print(cnt)
