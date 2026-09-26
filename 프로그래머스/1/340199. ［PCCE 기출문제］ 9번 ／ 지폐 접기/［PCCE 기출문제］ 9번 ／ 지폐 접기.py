def solution(wallet, bill):
    # 1.
    answer = 0
    
    # 2.
    wallet.sort()
    
    while True:
        bill.sort()
        if wallet[0] >= bill[0] and wallet[1] >= bill[1]:
            break
        
        bill[1] //= 2
        answer += 1
        
    return answer