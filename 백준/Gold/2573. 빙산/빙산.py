from collections import deque

def bfs(i, j):
    queue = deque([(i, j)])
    visited[i][j] = 1

    while queue:
        i, j = queue.popleft()
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if arr[ni][nj] and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
year = 0

while 1:
    new_arr = [[0] * M for _ in range(N)]
    # 매 1년마다 빙산 녹이기
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                cnt = 0
                for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    ni, nj = i + di, j + dj
                    if arr[ni][nj] == 0:
                        cnt += 1
                # if cnt: 를 넣으면 상하좌우 전부 수에 둘려쌓여 있어서 
								# 안 녹는 경우를 처리 못함.
                # 안 녹으면 숫자 그대로 new_arr에 넣어줘야 되는데 
								# cnt가 안쌓여서 재할당이 안되니까
                # 처음 new_arr 만들 때 넣어놓은 0으로 유지되기 때문
                new = arr[i][j] - cnt
                if new < 0:
                    new = 0
                new_arr[i][j] = new

    year += 1
    arr = new_arr

    num_ice = 0
    visited = [[0] * M for _ in range(N)]
    flag = False
    
    # 빙산 개수 세기
    for k in range(N):
        for l in range(M):
            if arr[k][l] and visited[k][l] == 0:
                bfs(k, l)
                num_ice += 1
                flag = True
    
    if num_ice >= 2:
        print(year)
        break

    if flag is False:
        print(0)
        break