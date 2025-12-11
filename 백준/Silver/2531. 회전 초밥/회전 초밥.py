import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())

num_list = [int(input()) for _ in range(N)]
num_list.extend(num_list)

max_num = 0
for i in range(N):
    cur_list = num_list[i : i + k] + [c]
    max_num = max(len(set(cur_list)), max_num)
    
    if max_num == k + 1:
        break
        
print(max_num)
