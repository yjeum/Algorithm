import sys
import heapq

input = sys.stdin.readline

N = int(input())

q = []
minus_dict = {}

for _ in range(N):
    num = int(input())
    # 출력을 원할 경우
    if num == 0:
        if q:
            temp = heapq.heappop(q)
            if minus_dict[temp] > 0:
                minus_dict[temp] -= 1
                print(-temp)
            else:
                print(temp)
        else:
            print(0)

    # 수 입력 받는 경우
    else:
        heapq.heappush(q, abs(num))
        if num < 0:
            minus_dict[-num] = minus_dict.get(-num, 0) + 1
        else:
            minus_dict[num] = minus_dict.get(num, 0)
