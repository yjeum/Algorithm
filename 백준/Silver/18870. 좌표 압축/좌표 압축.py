import sys
input = sys.stdin.readline

N = int(input())
num_lst = list(map(int, input().split()))

# 중복 제거 및 정렬
s_num_lst = sorted(set(num_lst))

# 인덱스 라벨링
num_dic = {}
for idx, val in enumerate(s_num_lst):
    num_dic[val] = num_dic.get(val, idx)

# 위치 출력
for i in num_lst:
    print(num_dic[i], end=" ")
