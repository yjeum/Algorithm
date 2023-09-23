from collections import deque

col, row, height = map(int, input().split())

box = [[list(map(int, input().split())) for _ in range(row)] for __ in range(height)]

q = deque()
for k in range(height):
    for i in range(row):
        for j in range(col):
            if box[k][i][j] == 1:
                q.append((k, i, j))

max_day = 1
while q:
    c_k, c_i, c_j = q.popleft()

    for dk in [1, -1]:
        nk = c_k + dk
        if 0<= nk < height and box[nk][c_i][c_j] == 0:
            q.append((nk, c_i, c_j))
            box[nk][c_i][c_j] = box[c_k][c_i][c_j] + 1

            if max_day < box[nk][c_i][c_j]:
                max_day = box[nk][c_i][c_j]

    for di, dj in [[0,1], [1,0], [-1,0], [0,-1]]:
        ni, nj = c_i + di, c_j + dj
        if 0<= ni < row and 0<= nj < col and box[c_k][ni][nj] == 0:
            q.append((c_k, ni, nj))
            box[c_k][ni][nj] = box[c_k][c_i][c_j] + 1
            
            if max_day < box[c_k][ni][nj]:
                max_day = box[c_k][ni][nj]

flg = True
for k in range(height):
    for i in range(row):
        for j in range(col):
            if box[k][i][j] == 0:
                flg = False
                break
if flg == True:
    print(max_day-1)
else:
    print(-1)