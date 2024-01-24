def solution(priorities, location):
    cnt = 0
    N = len(priorities)
    now = 0
    while sum(priorities) != 0:
        max_value = max(priorities) 
        if priorities[now%N] == max_value:
            priorities[now%N] = 0
            cnt += 1
            if now%N == location:
                return cnt

        now += 1
    return 0