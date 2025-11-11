import sys
input = sys.stdin.readline

p, m = map(int, input().split())

# rooms : [[기준 레벨], [[level, n], ...]]
rooms = []
for _ in range(p):
    l, n = input().split()
    level = int(l)
    
    for cur in range(len(rooms)):
        # 방 정원 초과인 경우
        if len(rooms[cur][1]) == m:
            continue

        # 기준 레벨과 비교하여 들어갈 수 있는 방
        elif rooms[cur][0] - 10 <= level <= rooms[cur][0] + 10:
            rooms[cur][1].append([level, n])
            break

    else:
        rooms.append([level, [[level, n]]])

# 생성된 방 > 아이디 순 출력
for room in rooms:
    # 정원이 모여 게임이 시작한 경우
    if len(room[1]) == m:
        print('Started!')
    
    # 정원이 모이지 못해 대기중인 경우
    else:
        print('Waiting!')

    temp_list = sorted(room[1], key=lambda x: x[1])
    for temp in temp_list:
        print(temp[0], temp[1])
        