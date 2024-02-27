from collections import deque
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    A = deque(A)
    B = deque(B)
    
    a = A.popleft()
    while B:
        b = B.popleft()
        if a < b:
            if A:
                a = A.popleft()
            answer += 1

    return answer