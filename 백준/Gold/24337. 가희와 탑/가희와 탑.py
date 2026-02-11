import sys
input = sys.stdin.readline

N, a, b = map(int, input().split())
heights = [0] * N

# 범위이상
if a + b - 1 > N:
    print(-1)
    exit()

# 맨앞에 가장 높은 건물일경우
if a == 1:
    heights[0] = b
    for i in range(1, N - b + 1):
        heights[i] = 1
    cur = b - 1
    for i in range(N - b + 1, N):
        heights[i] = cur
        cur -= 1
    print(*heights)
    exit()
    
# 가장 높은 높이
max_h = max(a, b)

# 오른쪽부터 진행
for j in range(b):
    heights[N - j - 1] = j + 1
heights[N - b] = max_h

# 가희가 보이는 것
cur = 1
for i in range(N - b - a + 1, N - b):
    heights[i] = cur
    cur += 1

# 나머지 채워넣기
for k in range(N - b - a + 1):
    heights[k] = 1
print(*heights)
