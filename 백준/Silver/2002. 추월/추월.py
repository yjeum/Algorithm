import sys

input = sys.stdin.readline

N = int(input())

input_cars = {}
for i in range(N):
    input_cars[input().rstrip()] = i

output_cars = []
for i in range(N):
    output_cars.append(input().rstrip())

cnt = 0
for i in range(N - 1):
    for j in range(i, N):
        if input_cars[output_cars[i]] > input_cars[output_cars[j]]:
            cnt += 1
            break
print(cnt)
