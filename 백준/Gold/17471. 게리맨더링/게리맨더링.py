import sys
input = sys.stdin.readline
from collections import deque

def bfs(sub1, sub2, start):
    flg = True
    visited = [0]*(spot+1)

    for i in sub2:
        visited[i] = 1
    visited[start] = 1
    
    q = deque()
    q.append(start)
    while q:
        current = q.popleft()
        for next in arr[current]:
            if next in sub1 and visited[next] == 0:
                q.append(next)
                visited[next] = 1

    p = 0
    if visited.count(0) != 1:
        flg = False
        return flg, p

    # sub에 있는 요소가 전부 연결되어 있는지 확인
    # 연결되어 있다면 사람 수 구하기
    p = 0
    for v in sub1:
        p += people[v]

    return flg, p


spot = int(input())
people = [0] + list(map(int, input().split()))

arr = [[] for _ in range(spot + 1)]
for i in range(spot):
    edges = list(map(int, input().split()))
    arr[i+1] = edges[1:]

min_people = 1e9

for i in range(1, (1<<spot)//2):
    sub1 = []
    sub2 = []
    for j in range(spot):
        if i&(1<<j):
            sub1.append(j+1)
        else:
            sub2.append(j+1)
    # print('sub1, sub2', sub1, sub2)


    # 연결여부 확인
    flg1, p1 = bfs(sub1, sub2, sub1[0])
    if flg1 != False:
        flg2, p2 = bfs(sub2, sub1, sub2[0])

        if flg2 != False:
            if min_people > abs(p1-p2):
                min_people = abs(p1-p2)
    
if min_people == 1e9:
    print(-1)
else:
    print(min_people)