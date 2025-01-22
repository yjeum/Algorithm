import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    teams, problems, team_id, logs = map(int, input().split())
    score_lst = [[0] * (problems + 2) for _ in range(teams)]

    for log in range(logs):
        team, problem, score = map(int, input().split())
        # 횟수 관리
        score_lst[team - 1][0] += 1
        # 점수 관리
        score_lst[team - 1][problem] = max(score_lst[team - 1][problem], score)
        # 마지막 제출 시간 관리
        score_lst[team - 1][problems + 1] = log

    # 등수 관리
    total_score = [[0, 0, 0, i + 1] for i in range(teams)]
    for i, score in enumerate(score_lst):
        total_score[i][0] = sum(score[1 : problems + 1])
        total_score[i][1] = score_lst[i][0]
        total_score[i][2] = score_lst[i][problems + 1]
    sorted_lst = sorted(total_score, key=lambda x: (-x[0], x[1], x[2]))
    for i in range(teams):
        if sorted_lst[i][3] == team_id:
            print(i + 1)
