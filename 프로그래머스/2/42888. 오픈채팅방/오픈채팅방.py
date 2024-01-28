def solution(record):
    answer = []
    nickname = {}
    
    for user in record:
        user_info = user.split()
        if user_info[0] != "Leave":
            nickname[user_info[1]] = user_info[2]
            
    for user in record:
        user_info = user.split()
        if user_info[0] == "Enter":
            answer.append(nickname[user_info[1]] + '님이 들어왔습니다.')
        elif user_info[0] == "Leave":
            answer.append(nickname[user_info[1]] + '님이 나갔습니다.')

    return answer