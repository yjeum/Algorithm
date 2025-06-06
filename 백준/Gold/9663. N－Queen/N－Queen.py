import sys
input = sys.stdin.readline

# 상하 -> 백트래킹으로 관리
# 좌우 -> index를 리스트로 관리
# 대각선 -> x1 - x2 != abs(y1 - y2)로 관리


def check_diagonal(c_level):
    # 대각선 확인
    for p_level in range(c_level):
        if c_level - p_level == abs(visited_i[p_level] - visited_i[c_level]):
            return False
    return True


def backtracking(level):
    global cnt

    # 마지막 행을 지나갔다면 횟수 증가 후 마침
    if level == N:
        cnt += 1
        return

    # 아직 진행 중이라면 col을 돌며 둘 수 있는 위치 확인
    for j in range(N):
        # 해당 인덱스를 쓴 적이 있는지 확인
        if visited_d[j] == -1:
            visited_d[j] = level
            visited_i[level] = j

            if check_diagonal(level):
                backtracking(level + 1)

            visited_d[j] = -1
            visited_i[level] = -1


N = int(input())

cnt = 0
visited_i = [-1] * N
visited_d = {_: -1 for _ in range(N)}

backtracking(0)
print(cnt)
