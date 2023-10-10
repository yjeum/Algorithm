def cal(n, tmp):
    if n == N:
        result_lst.append(tmp)
        return

    for i in range(4):
        if cal_lst[i]:
            cal_lst[i] -= 1

            if i == 0:
                cal(n+1, tmp + num_lst[n])
            elif i == 1:
                cal(n+1, tmp - num_lst[n])
            elif i == 2:
                cal(n+1, tmp * num_lst[n])
            else:
                cal(n+1, int(tmp / num_lst[n]))
            
            cal_lst[i] += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cal_lst = list(map(int, input().split()))
    num_lst = list(map(int, input().split()))
    result_lst = []
    cal(1, num_lst[0])

    res = max(result_lst) - min(result_lst)
    print(f'#{tc}', res)