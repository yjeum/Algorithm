def solution(k, tangerine):
    tangerine_type = {}
    for i in tangerine:
        tangerine_type[i] = tangerine_type.get(i, 0) + 1

    values_lst = sorted(tangerine_type.values(), reverse = True)
    
    start = 0
    total = 0
    while True:
        total += values_lst[start]
        start += 1
        if total >= k:
            break

    return start