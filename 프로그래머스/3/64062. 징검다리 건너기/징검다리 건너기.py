# def solution(stones, k):
#     min_val = 1e9
#     for i in range(len(stones) - k + 1):
#         min_val = min(min_val, max(stones[i:i+k]))
#     return min_val

def solution(stones, k):
    left, right = 1, 200000000
    
    while left <= right:
        
        mid = (left + right) // 2
        cnt = 0
        
        for stone in stones:
            if stone <= mid:
                cnt += 1
                if cnt == k:
                    break
            else:
                cnt = 0
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
            
    return left