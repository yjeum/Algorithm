isp = {'(' : 0, '+': 1, '-' : 1, '*' : 2, '/' : 2}
icp = {'(' : 3, '+': 1, '-' : 1, '*' : 2, '/' : 2}

# 연산 길이
# infix_len = int(input())

# 현재 중위표기법으로 받은 연산
infix_str = input()

# 후위표기법으로 변경 된 값을 넣어주기 위한 문자열 생성
postfix_str = ''

# 연산자 가중치 비교를 위한 스택 생성
stack = []

# 후위표기방식으로 변경
for i in infix_str:

    # 숫자이면 문자열에 추가
    if i not in isp.keys() and i != ')':
        postfix_str += i
    
    # 숫자가 아닐경우 연산자 가중치 비교
    # 현재는 +만 존재한다고 문제에 주어져 있음
    else:
        if i == ')':

            while True:
                pop = stack.pop()
                if pop == '(':
                    break
                else:
                    postfix_str += pop

        else:    

            # 스택이 비어있는 경우 가중치가 가장 높으므로 스택에 추가
            if not stack:
                stack.append(i)
                # print(stack)

            # 스택이 비어있지 않는 경우 모두 +로 가중치가 동일하여
            # 비교해주는 과정 생략 후 바로 후위표기법에 넣어줌
            else:
                while stack and icp[i] <= isp[stack[-1]]:
                    postfix_str += stack.pop()
                stack.append(i)

                # postfix_str += i
    
while stack:
    postfix_str += stack.pop()

print(postfix_str)