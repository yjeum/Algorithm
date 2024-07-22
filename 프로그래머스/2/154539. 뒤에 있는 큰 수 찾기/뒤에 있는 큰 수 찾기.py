def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    stack = []
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack[-1]] = numbers[i]
            stack.pop()
        stack.append(i)
    
    
    return answer