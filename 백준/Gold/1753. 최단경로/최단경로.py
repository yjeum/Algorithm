import sys
import heapq

input = sys.stdin.readline


def dijkstra(gp, start):
    distances = [int(1e9) for _ in range(V + 1)]
    distances[start] = 0
    q = []
    heapq.heappush(q, (distances[start], start))

    while q:
        dist, node = heapq.heappop(q)

        if distances[node] < dist:
            continue

        for next_dist, next_node in gp[node]:
            distance = dist + next_dist
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(q, (distance, next_node))

    return distances


V, E = map(int, input().split())
K = int(input())

gp = [[] for _ in range(V + 1)]
for _ in range(E):
    start_node, end_node, w = map(int, input().split())
    gp[start_node].append((w, end_node))

distances = dijkstra(gp, K)
for i in range(1, V + 1):
    if distances[i] == 1e9:
        print("INF")
    else:
        print(distances[i])
