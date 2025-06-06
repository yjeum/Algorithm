# 참고 코드(python 통과 다른사람풀이)

def Queen(row):
    global count, board
    if row == N:
        count += 1
        return

    for col in range(N):
        if cols[col] and diagonal_1[row + col] and diagonal_2[row - col + N]:
            cols[col] = False
            diagonal_1[row + col] = False
            diagonal_2[row - col + N] = False       

            Queen(row + 1)

            cols[col] = True
            diagonal_1[row + col] = True
            diagonal_2[row - col + N] = True

N = int(input())
count = 0
cols = [True for _ in range(N)]
diagonal_1 = [True] * 2*N
diagonal_2 = [True] * 2*N

Queen(0)
print(count)