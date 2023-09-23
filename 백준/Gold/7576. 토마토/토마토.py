from collections import deque

col, row = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(row)]

q = deque()

for i in range(row):
    for j in range(col):
        if box[i][j] == 1:
            q.append((i, j))
            
max_day = 1
while q:
    c_i, c_j = q.popleft()

    for di, dj in [[0,1], [1,0], [-1,0], [0,-1]]:
        ni, nj = c_i + di, c_j + dj
        if 0<= ni < row and 0<= nj < col and box[ni][nj] == 0:
            q.append((ni, nj))
            box[ni][nj] = box[c_i][c_j] + 1
            
            if max_day < box[ni][nj]:
                max_day = box[ni][nj]

flg = True
for i in range(row):
    for j in range(col):
        if box[i][j] == 0:
            flg = False
            break
if flg == True:
    print(max_day-1)
else:
    print(-1)