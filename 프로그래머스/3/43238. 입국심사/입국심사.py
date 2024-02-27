def solution(n, times):
    start, end = 1, min(times) * n
    
    while start <= end:
        middle = (start + end) // 2
        
        temp = 0
        for time in times:
            temp += middle // time
            
        if n <= temp:
            answer = middle
            end = middle - 1
        else:
            start = middle + 1
    
    return answer