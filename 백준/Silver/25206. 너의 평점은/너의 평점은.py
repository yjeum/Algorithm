import sys
input = sys.stdin.readline

grade = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}
total_time = 0
total_point = 0

for _ in range(20):
    title, time, point = input().split()

    if point == "P":
        continue

    total_time += float(time)
    total_point += float(grade.get(point)) * float(time)

print(round(total_point / total_time, 6))
