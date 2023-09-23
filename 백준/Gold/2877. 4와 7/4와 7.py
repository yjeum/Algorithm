K = int(input())

cnt = 1
std = 1

# 자리수와 2진수 변환
while True:
    if std * 2 < K:
        cnt += 1
        std *= 2
        K -= std
    else:
        K_2 = bin(K-1)[2:]
        break

# 자리수만큼 0 채워주기
min_str = []
for i in K_2:
    min_str += i

for i in range(cnt-len(min_str)):
    min_str = ['0'] + min_str

# 결과 출력
res = ''
for i in min_str:
    if i == '0':
        res += '4'
    else:
        res += '7'
print(res)
