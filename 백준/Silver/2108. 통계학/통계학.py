N = int(input())

num_dic = {}
num_lst = []
sum = 0
max_cnt = 0

for _ in range(N):
    i = int(input())
    sum += i
    num_lst.append(i)
    num_dic[i] = num_dic.get(i, 0) + 1
    if max_cnt < num_dic[i]:
        max_cnt = num_dic[i]

num_lst.sort()
print(round(sum/N))
print(num_lst[N//2])

max_val = [num for num, count in num_dic.items() if count == max_cnt]
max_val.sort()
if len(max_val) > 1:
    print(max_val[1])
else:
    print(max_val[0])

print(num_lst[N-1] - num_lst[0])