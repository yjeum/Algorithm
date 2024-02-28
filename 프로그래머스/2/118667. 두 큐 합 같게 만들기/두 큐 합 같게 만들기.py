from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    min_cnt = len(queue1) * 3
    cnt = 0
    sum1, sum2 = sum(queue1), sum(queue2)
    
    if (sum1 + sum2) // 2 == 1:
        return -1
    
    while cnt < min_cnt:
        if sum1 == sum2:
            return cnt
        elif sum1 > sum2:
            element = queue1.popleft()
            queue2.append(element)
            sum1 -= element
            sum2 += element
        else:
            element = queue2.popleft()
            queue1.append(element)
            sum2 -= element
            sum1 += element
        cnt += 1
    return -1