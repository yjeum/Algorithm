import sys
input = sys.stdin.readline

num = int(input())

# 리스트 생성 후 중복제거와 정렬
ori_num_list = list(map(int, input().split()))
num_list = sorted(set(ori_num_list))

# 딕셔너리에 저장
num_dic = {}
for i in range(len(num_list)):
    num_dic[num_list[i]] = num_dic.get(num_list[i], i)

for i in ori_num_list:
    print(num_dic[i], end=" ")

# 시간초과
# list의 index의 경우 시간복잡도 O(n)이기 때문에
# 자료의 제한범위가 크면 시간초과가 나타남

# num = int(input())
# num_list = list(map(int, input().split()))

# for i in range(num):
#     cnt = 0
#     for j in range(num):
#         if num_list[i] > num_list[j]:
#             cnt += 1
#     print(cnt, end=" ")