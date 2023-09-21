import heapq

def dijkstra():
    pq = []
    heapq.heappush(pq, (0, (0,0)))

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now[0]][now[1]] < dist:
            continue

        for didj in [[0,1], [1, 0], [-1, 0], [0, -1]]:
            ni, nj = now[0]+didj[0], now[1]+didj[1]

            if 0<=ni<N and 0<=nj<N:
                new_cost = dist + int(arr[ni][nj])

                if distance[ni][nj] <= new_cost:
                    continue
                
                distance[ni][nj] = new_cost
                heapq.heappush(pq, (new_cost, (ni, nj)))

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [list(input()) for _ in range(N)]

    distance = [[1e9]*N for _ in range(N)]

    dijkstra()
    print(f'#{tc}', distance[N-1][N-1])