N = int(input())
arr = list(map(int, input().split()))

arr_s = sorted(arr)
answer =1e9
for i in range(len(arr)):
    temp = arr_s[i] + arr_s[2*N-1-i]
    answer=min(answer,temp)
    
print(answer)