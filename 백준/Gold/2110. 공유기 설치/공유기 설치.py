import sys
input = sys.stdin.readline

N, C = map(int, input().split())

house_list = [int(input()) for _ in range(N)]
house_list.sort()

# 거점 상관 없이 거리 상으로 균등하게 배분했을 경우(최상의 경우)
start, end = 1, (house_list[N - 1] - house_list[0]) // (C - 1)

while start <= end:

    mid = (start + end) // 2

    cur = house_list[0]
    cnt = 1

    for i in house_list:

        # 생각한 거리 이상인 경우 설치
        if i - cur >= mid:
            cnt += 1

            # 현재 위치 변경
            cur = i

            # 이미 공유기를 다 설치했다면 생각한 거리보다 더 멀어도 설치 가능
            if cnt >= C:
                break

    if cnt >= C:
        start = mid + 1
    else:
        end = mid - 1

print(end)
