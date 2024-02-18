from itertools import permutations

def solution(k, dungeons):
    N = len(dungeons)
    order_lst = list(permutations(dungeons, N))
    
    answer = -1
    
    for dungeon in order_lst:
        cnt = 0
        fatigue = k
        for minimum, spend in dungeon:
            if fatigue >= minimum:
                fatigue -= spend
                cnt += 1
        answer = max(answer, cnt)   
    
    return answer