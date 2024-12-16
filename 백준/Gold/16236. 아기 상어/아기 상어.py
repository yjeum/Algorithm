import sys
from collections import deque
import heapq
input = sys.stdin.readline

# 상, 좌, 하, 우
didj = [(-1, 0), (0, -1), (1, 0), (0, 1)]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 아기 상어 위치 파악
fishes = {}
for i in range(N):
    for j in range(N):
        # if 1 <= arr[i][j] < 7:
        #     fishes[arr[i][j]] = fishes.get(arr[i][j], 0) + 1
        if arr[i][j] == 9:
            si, sj = i, j
            arr[i][j] = 0
            break

size = 2
cnt = 0
temp = 0
while True:
    visited = [[0] * N for _ in range(N)]
    visited[si][sj] = 1
    pq = []
    q = deque([(si, sj, 0)])
    flg = False
    # 물고기 탐색
    while q:
        ci, cj, dist = q.popleft()

        # 같은 거리에 있는 풍선팡 시작
        for di, dj in didj:
            ni, nj = ci + di, cj + dj
            # 범위 안에 존재하며, 방문하지 않았고, 물고기 크기보다 크거가 같은 경우
            if (
                0 <= ni < N
                and 0 <= nj < N
                and visited[ni][nj] == 0
                and arr[ni][nj] <= size
            ):
                # 방문처리
                visited[ni][nj] = 1
                # 갈 수 있는 곳 업데이트
                q.append((ni, nj, dist + 1))
                if 0 < arr[ni][nj] < size:
                    # 같은 거리에 있는 물고기 리스트(heapq) 업데이트
                    heapq.heappush(pq, (dist + 1, ni, nj))

    # 같은 거리 탐색 시 먹을 물고기가 존재한다면
    if pq:
        dis, ci, cj = heapq.heappop(pq)
        arr[ci][cj] = 0
        # 시간 업데이트
        cnt += dis
        # 상어 위치 업데이트
        si, sj = ci, cj
        # 상어 사이즈 업데이트
        temp += 1
        if temp == size:
            size += 1
            temp = 0
        flg = True

    if flg == False:
        print(cnt)
        sys.exit()
