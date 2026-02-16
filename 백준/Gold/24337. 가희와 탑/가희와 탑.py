import sys
input = sys.stdin.readline

N, a, b = map(int, input().split())

if a + b - 1 > N:
    print(-1)
    exit()

H = max(a, b)
extra = N - (a + b - 1)

result = []

if a == 1:
    # 최고점 먼저
    result.append(H)
    result += [1] * extra
else:
    result += [1] * extra
    for i in range(1, a):
        result.append(i)
    result.append(H)

# 오른쪽 감소
for i in range(b-1, 0, -1):
    result.append(i)

print(*result)
