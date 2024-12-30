import sys
from collections import defaultdict
input = sys.stdin.readline


# 시간 계산 함수
def calculate_minutes(start, end):
    sh, sm = map(int, start.split(":"))
    eh, em = map(int, end.split(":"))
    return (eh * 60 + em) - (sh * 60 + sm)


# 총 횟수, 날짜
N, M = map(int, input().split())

# 주 단위로 확인
# 일주일동안 방송 횟수와 시간 확인
# dict - key : name, value : [[cnt, total_time], ...]
real_youtuber = defaultdict(lambda: defaultdict(lambda: [0, 0]))
for i in range(N):
    name, day, start, end = input().split()
    week = (int(day) - 1) // 7
    minutes = calculate_minutes(start, end)
    real_youtuber[name][week][0] += 1
    real_youtuber[name][week][1] += minutes

# 유효 유투버 확인
valid_youtubers = []
for name, weeks in real_youtuber.items():
    is_valid = True
    for cnt, total_time in weeks.values():
        if cnt < 5 or total_time < 60 * 60:
            is_valid = False
            break
    if is_valid and len(weeks) == (M // 7):
        valid_youtubers.append(name)

valid_youtubers.sort()
if valid_youtubers:
    for youtuber in valid_youtubers:
        print(youtuber)
else:
    print(-1)
