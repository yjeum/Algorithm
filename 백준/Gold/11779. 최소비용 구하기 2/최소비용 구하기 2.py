import sys
import heapq

input = sys.stdin.readline


def dijkstra(graph, start, before):
    distances = [int(1e9)] * (N + 1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        dist, node = heapq.heappop(queue)

        if distances[node] < dist:
            continue

        for next_node, next_dist in graph[node]:
            distance = dist + next_dist
            if distance < distances[next_node]:
                distances[next_node] = distance
                before[next_node] = node
                heapq.heappush(queue, [distance, next_node])
    return distances


N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
before = [0] * (N + 1)
for _ in range(M):
    start_node, end_node, w = map(int, input().split())
    graph[start_node].append((end_node, w))
start, end = map(int, input().split())

dist_start = dijkstra(graph, start, before)
print(dist_start[end])

path = []
while end:
    path.append(end)
    end = before[end]
print(len(path))

for i in path[::-1]:
    print(i, end=" ")
