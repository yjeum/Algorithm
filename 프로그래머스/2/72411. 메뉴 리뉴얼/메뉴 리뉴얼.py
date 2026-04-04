from itertools import combinations

def solution(orders, course):
    
    answer = []
    
    for number in course:
        combi_dict = {}
        for order in orders:
            
            combis = list(combinations(''.join(sorted(order)), number))
            for combi in combis:
                combi_value = ''.join(combi)
                combi_dict[combi_value] = combi_dict.get(combi_value, 0) + 1
            
        if combi_dict:
            max_cnt = max(combi_dict.values())
            if max_cnt > 1:
                answer = answer + [k for k, v in combi_dict.items() if v == max_cnt]
    
    return sorted(answer)