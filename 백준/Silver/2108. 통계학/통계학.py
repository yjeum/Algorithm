import sys

input = sys.stdin.readline

N = int(input())
nums = []
nums_dic = {}
max_cnt = 0

for _ in range(N):
    num = int(input())
    nums.append(num)
    nums_dic[num] = nums_dic.get(num, 0) + 1
    if max_cnt < nums_dic[num]:
        max_cnt = nums_dic[num]
nums.sort()

print(round(sum(nums) / N))
print(nums[N // 2])

max_val = []
for key, val in nums_dic.items():
    if val == max_cnt:
        max_val.append(key)
max_val.sort()
if len(max_val) > 1:
    print(max_val[1])
else:
    print(max_val[0])

print(nums[-1] - nums[0])
