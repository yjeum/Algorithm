def solution(array, commands):
    
    answer = []
    
    for now in commands:
        i, j, k = now[0], now[1], now[2]
        new_array = sorted(array[i-1:j])
        answer.append(new_array[k-1])
    return answer