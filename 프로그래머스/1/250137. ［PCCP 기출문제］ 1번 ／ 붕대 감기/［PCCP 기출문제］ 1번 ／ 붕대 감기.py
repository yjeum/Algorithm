def solution(bandage, health, attacks):
    
    cur_h = health
    before_t = 0
    
    for attack in attacks:
        
        gap = attack[0] - before_t - 1
        
        # 현재 체력 세팅
        cur_h = min(cur_h + (gap * bandage[1]) + (gap // bandage[0]) * bandage[2], health)

        # 괴수의 어택
        cur_h = cur_h - attack[1]

        if cur_h <= 0:
            return -1
        
        before_t = attack[0]
    
    return cur_h