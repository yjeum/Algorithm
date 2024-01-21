def solution(clothes):
    clothes_type = {}
    for clothe in clothes:
        if clothe[1] in clothes_type:
            clothes_type[clothe[1]] += 1
        else:
            clothes_type[clothe[1]] = 1
    
    answer = 1
    for value in clothes_type.values():
        answer *= (value + 1)
    print(answer)
    
    return answer - 1