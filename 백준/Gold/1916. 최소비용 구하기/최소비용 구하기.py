import sys
import heapq

input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for cost, next_node in city_map[node]:
            if distance[node] + cost < distance[next_node]:
                distance[next_node] = distance[node] + cost
                heapq.heappush(q, (distance[node] + cost, next_node))


node = int(input())
edge = int(input())
city_map = [[] for _ in range(node + 1)]
for _ in range(edge):
    start, end, cost = map(int, input().split())
    city_map[start].append((cost, end))
start, end = map(int, input().split())

distance = [1e9] * (node + 1)
dijkstra(start)

print(distance[end])
