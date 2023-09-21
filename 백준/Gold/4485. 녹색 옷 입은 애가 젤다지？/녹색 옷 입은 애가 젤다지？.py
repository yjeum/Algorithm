import heapq

def dijkstra():
    pq = []
    heapq.heappush(pq, (arr[0][0], (0, 0)))

    while pq:
        current_rupi, now = heapq.heappop(pq)

        if rupi[now[0]][now[1]] < current_rupi:
            continue

        for didj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni, nj = now[0]+didj[0], now[1]+didj[1]
            # 범위 안에 존재한다면
            if 0<=ni<N and 0<=nj<N:
                new_cost = current_rupi + arr[ni][nj]

                if rupi[ni][nj] <= new_cost:
                    continue
                
                rupi[ni][nj] = new_cost
                heapq.heappush(pq, (new_cost, (ni, nj)))

tc = 0
while True:
    tc += 1
    N = int(input())
    if N == 0:
        break
    
    arr= [list(map(int,input().split())) for _ in range(N)]

    rupi = [[1e9]*N for _ in range(N)]

    dijkstra()
    print(f'Problem {tc}: {rupi[N-1][N-1]}')