def solution(priorities, location):
    cnt = 0
    N = len(priorities)
    while sum(priorities) != 0:
        now = 0
        while 1:
            print("now",now)
            max_value = max(priorities) 
            print(max_value)
            if priorities[now%N] == max_value:
                print("들어옴")
                priorities[now%N] = 0
                cnt += 1
                if now%N == location:
                    print("now%N", now%N, "location", location)
                    return cnt

            now += 1
    return 0