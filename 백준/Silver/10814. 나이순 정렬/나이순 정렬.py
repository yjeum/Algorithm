N = int(input())

q = []
for i in range(N):
    age, name = input().split()
    q.append((int(age), name))

q.sort(key=lambda x: x[0])
for i in range(N):
    print(*q[i])