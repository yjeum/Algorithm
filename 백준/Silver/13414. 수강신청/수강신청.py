import sys

input = sys.stdin.readline

K, N = map(int, input().split())

students = {}
cnt = 1
for _ in range(N):
    student = input().rstrip()
    students[student] = cnt
    cnt += 1

sort_students = sorted(students.items(), key=lambda x: x[1])

temp = 1
for key, value in sort_students:
    print(key)
    if temp == K:
        break
    temp += 1
