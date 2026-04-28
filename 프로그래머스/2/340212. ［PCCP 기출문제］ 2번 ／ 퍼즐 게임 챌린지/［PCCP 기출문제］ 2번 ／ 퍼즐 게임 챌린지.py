def solution(diffs, times, limit):
    left, right = 1, limit
    
    while left <= right:
        mid = (left + right) // 2
        
        temp = 0
        for i in range(len(diffs)):
            if diffs[i] <= mid:
                temp += times[i]
            else:
                temp += (diffs[i] - mid) * (times[i] + times[i-1]) + times[i]
            
            if temp > limit:
                break
        
        if temp > limit:
            left = mid + 1
        else:
            right = mid - 1
            
    answer = left
    return answer