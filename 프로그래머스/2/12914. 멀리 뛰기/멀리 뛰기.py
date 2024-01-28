def solution(n):
    if n == 1:
        return 1
    step = [0]*(n+1)
    step[1], step[2] = 1, 2
    for i in range(3, n+1):
        step[i] = step[i-2] + step[i-1]
    return step[n] % 1234567