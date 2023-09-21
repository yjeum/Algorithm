# 모든 간선들 중 비용이 가장 적은 걸 우선으로 선택

# 환경 부담금 -> 환경 부담 세율(rate)과 각 해저터널 길이(L)의 제곱의 곱(E * L^2)
def cost_p(i, j):
    x_1, y_1, x_2, y_2 = x_lst[i], y_lst[i], x_lst[j], y_lst[j]
    return rate*((x_1 - x_2)**2 + (y_1 - y_2)**2)

# 부모 탐색 함수
def find_set(x):
    if parents[x] != x:
        parents[x] = find_set(parents[x])
    return parents[x]

# 집합 연결 함수
def union(x, y):
    x, y = find_set(x), find_set(y)

    # 사이클 발생 시 반환
    if x == y:
        return

    if x<y:
        parents[y] = x
    else:
        parents[x] = y

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x_lst = list(map(int,input().split()))
    y_lst = list(map(int,input().split()))
    rate = float(input())

    length = []
    for i in range(N-1):
        for j in range(i+1, N):
            length.append((cost_p(i, j), i, j))
    # cost를 기준으로 정렬
    length.sort()

    # 사이클 발생 여부를 union find로 해결
    parents = [i for i in range(N)]

    # 현재 방문한 정점 수
    cnt = 0
    sum_w = 0

    for cost, i, j in length:
        # 싸이클이 발생하지 않는다면
        if find_set(i) != find_set(j):
            union(i, j)
            cnt += 1
            sum_w += cost

            # MST 구성이 끝나면
            if cnt == N:
                break

    print(f'#{tc}', round(sum_w))