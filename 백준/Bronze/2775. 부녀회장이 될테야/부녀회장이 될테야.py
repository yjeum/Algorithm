T = int(input())

for _ in range(T):  
    floor = int(input())
    num = int(input())
    info = [x for x in range(1, num+1)]
    for i in range(floor):
        for j in range(1, num):
            info[j] += info[j-1]
    print(info[-1])