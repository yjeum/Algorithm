import sys
input = sys.stdin.readline

def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if size[x] < size[y]:
        parent[x] = y
        size[y] += size[x]

    else:
        parent[y] = x
        size[x] += size[y]

city_num = int(input())
travel_city_num = int(input())

parent = [i for i in range(city_num)]
size = [1]*city_num

city_map = [list(map(int,input().split())) for _ in range(city_num)]

for i in range(city_num):
    for j in range(i+1, city_num):
        if city_map[i][j] == 1:
            union(i, j)

for i in range(city_num):
    find_set(i)

travel_city = list(map(int, input().split()))
for i in travel_city:
    if parent[i-1] != parent[travel_city[0]-1]:
        print('NO')
        break
else:
    print('YES')