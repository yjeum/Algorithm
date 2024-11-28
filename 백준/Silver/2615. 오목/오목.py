import sys
input = sys.stdin.readline

didj = [(-1, 1), (1, 0), (1, 1), (0, 1)]


def check(i, j):
    for di, dj in didj:
        cnt = 1
        if not (
            0 <= i - di < 19 and 0 <= j - dj < 19 and arr[i][j] == arr[i - di][j - dj]
        ):
            k = 1
            while cnt <= 6:
                ni, nj = i + k * di, j + k * dj
                if 0 <= ni < 19 and 0 <= nj < 19 and arr[i][j] == arr[ni][nj]:
                    cnt += 1
                    k += 1
                else:
                    break

        if cnt == 5:
            print(arr[i][j])
            print(i + 1, j + 1)
            return True


arr = [list(map(int, input().split())) for _ in range(19)]
for i in range(19):
    for j in range(19):
        if arr[i][j] == 1 or arr[i][j] == 2:
            if check(i, j):
                sys.exit()
print(0)
