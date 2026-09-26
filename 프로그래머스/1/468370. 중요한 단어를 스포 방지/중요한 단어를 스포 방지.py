def solution(message, spoiler_ranges):
    
    spoilers = []    # 스포일러 포함 단어
    normal = set()     # 일반 단어
    message += ' '
    
    # 스포일러 위치 전처리
    spoiler_lo = [0 for _ in range(len(message))]
    for spoiler_range in spoiler_ranges:
        for i in range(spoiler_range[0], spoiler_range[1] + 1):
            spoiler_lo[i] = 1
    
    word = ''
    flg = False
    for j in range(len(message)):
        # 단어가 종료된 경우 스포 방지 단어 여부 확인
        if message[j] == ' ':
            # 스포방지 단어인 경우
            if flg == True:
                spoilers.append(word)
            # 스포방지 단어가 아닌경우
            else:
                normal.add(word)
            word = ''
            flg = False
            
        # 단어가 종료되지 않았을 경우
        else:
            word = word + message[j]
            if spoiler_lo[j] == 1:
                flg = True

    # 스포일러 단어를 돌아가며 확인
    answer = 0
    for spoiler in spoilers:
        if spoiler not in normal:
            answer += 1
            normal.add(spoiler)
    
    return answer