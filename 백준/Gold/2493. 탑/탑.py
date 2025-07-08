import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))

stack = []
tower_lo = [0] * N

for i in range(N):
    
    while stack:
        # 이전 타워에 맞는게 있는지 확인
        if towers[i] < stack[-1][1]:
            tower_lo[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    # 위치와 타워의 위치 각각 가지고 있어야함
    stack.append((i, towers[i]))
print(' '.join(map(str, tower_lo)))