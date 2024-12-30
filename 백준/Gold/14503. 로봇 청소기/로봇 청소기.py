import sys
input = sys.stdin.readline

# 북, 동, 남, 서(시계방향)
didj = [[-1, 0], [0, 1], [1, 0], [0, -1]]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
while True:
    # 청소 여부 확인
    if arr[r][c] == 0:
        cnt += 1
        arr[r][c] = 2
        continue

    # 방이 깨끗하다면 풍선팡
    flg = False
    for i in range(1, 5):
        nd = (d - i) % 4
        ni, nj = r + didj[nd][0], c + didj[nd][1]
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
            r, c, d = ni, nj, nd
            flg = True
            break

    if not flg:
        # 풍선팡 시 주변이 다 깨끗하다면 후진
        r, c = r - didj[d][0], c - didj[d][1]
        # 후진 시 벽이라면 끝내기
        if arr[r][c] == 1:
            break

print(cnt)
