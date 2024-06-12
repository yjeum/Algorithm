def solution(bridge_length, weight, truck_weights):
    
    sec_list = [bridge_length + 1 for _ in range(len(truck_weights))]
    
    sec = 0
    temp_weight = 0
    first_truck = 0
    next_truck = 0
    
    while True:
        # print(sec, sec_list, temp_weight)
        if next_truck == len(truck_weights):
            # print("1번")
            sec += bridge_length
            break
        
        if temp_weight + truck_weights[next_truck] <= weight:
            # print("2번")
            temp_weight += truck_weights[next_truck]
            next_truck += 1
            sec += 1
            for order in range(first_truck, next_truck):
                sec_list[order] -= 1
        else:
            # print("3번")
            sec += sec_list[first_truck] 
            # print(sec_list[first_truck], first_truck)
            temp = sec_list[first_truck]
            for order in range(first_truck, next_truck):
                sec_list[order] -= temp
            if temp_weight - truck_weights[first_truck] + truck_weights[next_truck] <= weight:
                sec_list[next_truck] -= 1
                temp_weight += truck_weights[next_truck]
                next_truck += 1
        
        if sec_list[first_truck] == 0:
            # print("4번")
            temp_weight -= truck_weights[first_truck]
            first_truck += 1
            
        
    return sec