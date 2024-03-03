def solution(sticker):
    if len(sticker) == 1:
        return sum(sticker)
    
    max_sum = [0] * len(sticker)
    
    max_sum[0], max_sum[1] = sticker[0], max(sticker[0], sticker[1])
     
    for i in range(2, len(sticker)-1):
        max_sum[i] = max(max_sum[i-2] + sticker[i], max_sum[i-1])
    
    temp_max1 = max(max_sum)
    
    max_sum = [0] * len(sticker)
    max_sum[0], max_sum[1] = 0, sticker[1]
    
    for i in range(2, len(sticker)):
        # print(max_sum)
        # print(max_sum[i-2], sticker[i])
        max_sum[i] = max(max_sum[i-2] + sticker[i], max_sum[i-1])
    
    temp_max2 = max(max_sum)
    temp_max = max(temp_max1, temp_max2)
    
    return temp_max