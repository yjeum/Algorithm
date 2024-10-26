from collections import deque

# 입력 처리
N, M = map(int, input().split())
hands = deque()

# 각 참가자의 손 높이를 큐에 추가 (높이, 참가자 번호)
for i in range(M):
    H1, H2 = map(int, input().split())
    hands.append((H1, i + 1))
    hands.append((H2, i + 1))

# 손 높이 기준으로 정렬
hands = deque(sorted(hands))

# N번 반복하여 가장 아래 손을 위로 올리기
for _ in range(N):
    hand = hands.popleft()  # 가장 아래 손을 꺼내서
    hands.append(hand)      # 맨 위에 다시 쌓기

# N번째로 쌓인 손의 참가자 번호 출력
print(hands[-1][1])
