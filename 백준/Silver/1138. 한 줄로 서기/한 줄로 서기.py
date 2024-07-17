import sys
input = sys.stdin.readline

N = int(input())
check_list = list(map(int, input().split()))

answer = [0 for _ in range(N)]

# 현재가 가장 작은 수 이므로, 다음 수는 무조건 현재보다 큰 수
# 앞에 빈자리 갯수 확인
for i in range(N):
    cnt = 0

    for j in range(N):
        if answer[j] == 0:
            if cnt == check_list[i]:
                answer[j] = str(i + 1)
                break
            else:
                cnt += 1

print(" ".join(answer))
