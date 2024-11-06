import sys

input = sys.stdin.readline

N, K = map(int, input().split())
belt = list(map(int, input().split()))
robots = [0] * (N)

start = 0
cnt = 0
zero = 0

while True:
    # 0. 횟수 증가
    cnt += 1

    # 1. 벨트 회전
    start = (start - 1) % (2 * N)

    # 1-2. 벨트 회전에 따른 로봇 이동
    robots = [0] + robots[:-1]
    robots[N - 1] = 0

    # 2. 로봇 이동
    for cur in range(N - 1, 0, -1):
        # 벨트의 내구도, 현재 위치의 로봇 여부 확인
        if (
            belt[(start + cur) % (2 * N)] > 0
            and robots[cur] == 0
            and robots[cur - 1] == 1
        ):
            # 로봇 이동
            robots[cur] = robots[cur - 1]
            robots[cur - 1] = 0
            # 내구도 약화
            belt[(start + cur) % (2 * N)] -= 1
    # 2-2. 로봇 내리기
    robots[N - 1] = 0

    # 3. 내구도 확인 후 상자 올리기
    if belt[start] > 0:
        robots[0] = 1
        belt[start] -= 1

    # 4. 내구도 0인 자리 갯수 확인
    if belt.count(0) >= K:
        print(cnt)
        break
