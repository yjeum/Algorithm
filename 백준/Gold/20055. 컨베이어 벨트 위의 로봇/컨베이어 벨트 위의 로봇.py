import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
belt = deque(map(int, input().split()))  # 벨트를 deque로 변경
robots = deque([0] * N)  # 로봇도 deque로 변경

cnt = 0

while True:
    # 0. 횟수 증가
    cnt += 1

    # 1. 벨트 회전 (deque.rotate(1) 사용)
    belt.rotate(1)  # 벨트를 한 칸 회전
    robots.rotate(1)  # 로봇도 한 칸 회전
    robots[N-1] = 0

    # 2. 로봇 이동
    for cur in range(N - 1, 0, -1):
        if (
            belt[cur] > 0
            and robots[cur] == 0
            and robots[cur - 1] == 1
        ):
            # 로봇 이동
            robots[cur] = robots[cur - 1]
            robots[cur - 1] = 0
            # 내구도 약화
            belt[cur] -= 1

    # 2-2. 로봇 내리기
    robots[N - 1] = 0

    # 3. 내구도 확인 후 상자 올리기
    if belt[0] > 0:
        robots[0] = 1
        belt[0] -= 1

    # 4. 내구도 0인 자리 갯수 확인
    if belt.count(0) >= K:
        print(cnt)
        break
