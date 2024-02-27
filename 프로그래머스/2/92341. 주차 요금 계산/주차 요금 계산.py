from math import ceil

def solution(fees, records):
    
    answer = []
    car = []
    times = {}
    
    for record in records:
        record = record.split()
        
        if record[1] not in car: car.append(record[1])
        
        int_time = int(record[0][0:2]) * 60 + int(record[0][3:5])
        times[record[1]] = times.get(record[1], [])
        times[record[1]].append((record[2], int_time))
    print(times)
    for number, time in times.items():
        if len(time) % 2 != 0:
            time.append(('OUT', int(1439)))
        total_time = 0
        for state, num in time:
            if state == 'IN':
                total_time -= num
            else:
                total_time += num
        total_cost = 0
        if total_time > fees[0]:
            total_cost = fees[1] + (ceil((total_time - fees[0]) / fees[2])) * fees[3]
        else:
            total_cost = fees[1]
        times[number] = total_cost
    print(times)

    for car_num in sorted(car):
        answer.append(times[car_num])
    return answer