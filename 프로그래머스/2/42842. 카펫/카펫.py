def solution(brown, yellow):
    answer = []
    
    for i in range(1, yellow+1):
        if yellow % i == 0:
            side1 = yellow // i
            if brown == (2 * side1) + (2 * i) + 4:
                answer = [max(side1, i)+2, min(side1, i)+2]
                break
    
    return answer