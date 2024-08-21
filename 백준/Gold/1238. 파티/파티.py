import sys
import heapq

input = sys.stdin.readline


def dijkstra(start):
    w_list[start][start] = 0
    q = [(0, start)]

    while q:
        w, cur_n = heapq.heappop(q)

        if w_list[start][cur_n] < w:
            continue

        for next_n, next_w in gp[cur_n]:
            temp_w = w + next_w
            if temp_w > w_list[start][next_n]:
                continue

            w_list[start][next_n] = temp_w
            heapq.heappush(q, (temp_w, next_n))
    return


N, M, X = map(int, input().split())

gp = [[] for _ in range(N + 1)]
for _ in range(M):
    start_n, end_n, w = map(int, input().split())
    gp[start_n].append((end_n, w))

w_list = [[1e9] * (N + 1) for _ in range(N + 1)]

for start in range(1, N + 1):
    dijkstra(start)

answer = 0
for i in range(1, N + 1):
    answer = max(w_list[i][X] + w_list[X][i], answer)

print(answer)
