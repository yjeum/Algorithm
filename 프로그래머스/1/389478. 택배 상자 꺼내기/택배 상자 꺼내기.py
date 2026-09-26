def find(cur, w):
    return (cur - 1) // w, (cur - 1) % w;

def solution(n, w, num):
    
    # 가장 높은 수와 타겟 수 위치 확인
    n_r, n_c = find(n, w);
    num_r, num_c = find(num, w);
    
    # 두 행의 홀짝 여부 확인
    answer = n_r - num_r
    
    # 두 행의 시작점이 같다면
    if (n_r + num_r) % 2 == 0:
        # 타겟보다 위치가 앞서있으면 + 1
        if n_c >= num_c:
            answer += 1
            
    # 두 행의 시작점이 다르다면
    else:
        # 위치의 합과 w와 비교
        if num_c + n_c + 1 >= w:
            answer += 1
            
    return answer