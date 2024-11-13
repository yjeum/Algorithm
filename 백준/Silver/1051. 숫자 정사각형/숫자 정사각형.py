import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [input() for _ in range(N)]

temp = 1
# 왼쪽 위
for i in range(N - 1):
    for j in range(M - 1):
        std = arr[i][j]
        # 왼쪽 아래
        for a in range(1, N - i + 1):
            try:
                if std == arr[i + a][j] and std == arr[i][j + a] and std == arr[i + a][j + a]:
                    temp = max(temp, (a + 1) ** 2)
            except:
                continue
print(temp)
