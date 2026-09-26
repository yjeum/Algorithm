def solution(schedules, timelogs, startday):
    
    # 사람별로 확인
    cnt = 0
    for schedule, timelog in zip(schedules, timelogs):
        # 마감시간 설정
        deadline = schedule + (50 if schedule % 100 >= 50 else 10)
        
        # 7일간 마감시간 엄수 여부 확인
        flg = True
        for day in range(7):
            # 토, 일 이라면 확인하지 않음
            if (startday + day - 1) % 7 + 1 >= 6:
                continue
            
            # 마감시간을 넘었다면 제외

            if timelog[day] > deadline:
                flg = False
                break
        
        # 7일 모두 확인 결과
        if flg == True:
            cnt += 1

    return cnt