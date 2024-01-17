def solution(n):
    answer = 0
    
    for i in range(1, n//2 + 1):
        temp = 0
        current = i
        
        while temp < n:
            temp += current
            current += 1

            if temp == n:
                answer += 1
                break

    return answer+1