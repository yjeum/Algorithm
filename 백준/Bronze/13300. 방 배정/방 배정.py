N, K = map(int, input().split())

student = [0]*13

for i in range(N):
    sex, grade = map(int, input().split())
    if sex == 0:
        student[grade] += 1
    else:
        student[grade+6] += 1

room = 0
for i in student:
    if i%K == 0:
        room += i//K
    else:
        if i != 0:
            room += i//K + 1
print(room)