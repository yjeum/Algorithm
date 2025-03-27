import sys
input = sys.stdin.readline

M, N = map(int, input().split())
snacks = list(map(int, input().split()))

left, right = 1, 1000000000
max_len = 0
while left <= right:
    mid = (left + right) // 2
    cnt = 0

    # 현재 mid의 길이로 과자를 몇개 만들 수 있는지 확인
    for snack in snacks:
        cnt += snack // mid

        if cnt >= M:
            break

    if cnt >= M:
        left = mid + 1
        max_len = mid
    else:
        right = mid - 1

print(max_len)
