import sys
input = sys.stdin.readline
N = int(input().strip())
S = set()

for _ in range(N):
    cal_list = input().split()

    if len(cal_list) == 1:
        if cal_list[0] == "all":
            S = set(list(range(1, 21)))
        else:
            S = set()
    
    else:
        cal, num = cal_list[0], cal_list[1]
        num = int(num)
        
        if cal == "add":
            S.add(num)
        elif cal == "remove":
            S.discard(num)
        elif cal == "check":
            print(1 if num in S else 0)
        elif cal == "toggle":
            if num in S:
                S.discard(num)
            else:
                S.add(num)