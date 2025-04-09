import sys
input = sys.stdin.readline

N = int(input())

# 양수이면 1팀, 음수이면 2팀
score = 0
team_1 = 0
team_2 = 0
before = 0


def time_trans(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)


def time_retrans(time):
    return ":".join(time // 60, time % 60)


def time_cal(team, goal_time):
    global score, team_1, team_2, before

    cur = time_trans(goal_time)

    # 지금까지의 이기고 있던 팀에게 시간 부여
    if score > 0:
        team_1 += cur - before
    elif score < 0:
        team_2 += cur - before

    if team == "1":
        score += 1
    else:
        score -= 1

    # 이전 시간 변경
    before = cur


for i in range(N):
    team, goal_time = input().split()
    time_cal(team, goal_time)

# 종료 시 계산
time_cal("1", "48:00")


print(f"{team_1 // 60:02}:{team_1 % 60:02}")
print(f"{team_2 // 60:02}:{team_2 % 60:02}")
