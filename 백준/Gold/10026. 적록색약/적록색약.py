import sys
input = sys.stdin.readline


didj = [[0,1],[-1,0],[0,-1],[1,0]]

N = int(input())

arr = [list(input().rstrip()) for _ in range(N)]
visited1 = [[0]*(N) for _ in range(N)]
visited2 = [[0]*(N) for _ in range(N)]
cnt1 = 0
cnt2 = 0

for i in range(N):
    for j in range(N):
        if visited1[i][j] == 0:
            q = []
            q.append((i, j))
            cnt1 += 1

            while q:
                c_i, c_j = q.pop(0)

                for k in didj:
                    ni, nj = c_i + k[0], c_j + k[1]

                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == arr[i][j] and visited1[ni][nj] == 0:
                        q.append((ni,nj))
                        visited1[ni][nj] = 1

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if visited2[i][j] == 0:
            q = []
            q.append((i, j))
            cnt2 += 1

            while q:
                c_i, c_j = q.pop(0)

                for k in didj:
                    ni, nj = c_i + k[0], c_j + k[1]

                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == arr[i][j] and visited2[ni][nj] == 0:
                        q.append((ni,nj))
                        visited2[ni][nj] = 1

print(cnt1, cnt2)