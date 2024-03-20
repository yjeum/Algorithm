def DFS(temp, cnt, numbers, target):
    global target_cnt
    if cnt == len(numbers):
        if temp == target:
            target_cnt += 1
        return target_cnt
    
    DFS(temp - numbers[cnt], cnt + 1, numbers, target)
    
    DFS(temp + numbers[cnt], cnt + 1, numbers, target)
    pass

def solution(numbers, target):
    global target_cnt
    target_cnt = 0
    DFS(0, 0, numbers, target)
    return target_cnt