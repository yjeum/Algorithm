def solution(players, m, k):
    
    server = [[0, 0] for _ in range(24)] # 증설된 서버 수, 증설 횟수
    cnt = 0
    
    for i, player in enumerate(players):
        # 현재 서버로 player 감당 가능 여부 확인
        if (server[i][0] + 1) * m > player:
            continue
        
        # 감당 불가 경우 서버 증설
        addition = (player // m) - server[i][0]
        server[i][1] = addition
        cnt += addition
        
        for j in range(k):
            if i + j >= 24:
                break
            
            server[i + j][0] += addition

    return cnt