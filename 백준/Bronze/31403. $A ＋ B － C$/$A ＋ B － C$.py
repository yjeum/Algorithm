import sys
input = sys.stdin.readline

num_list = []

for _ in range(3):
    num_list.append(int(input()))
    
print(num_list[0] + num_list[1] - num_list[2])

temp = str(num_list[0]) + str(num_list[1])
print(int(temp) - num_list[2])