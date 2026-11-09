def solution(board, moves):
    
    stack = []
    cnt = 0
    for move in moves:
        for lo in range(len(board)):
            if board[lo][move - 1] != 0:
                cur = board[lo][move - 1]
                if stack and stack[-1] == cur:
                    stack.pop()
                    cnt += 2
                else:
                    stack.append(cur)
                board[lo][move - 1] = 0
                break
    return cnt