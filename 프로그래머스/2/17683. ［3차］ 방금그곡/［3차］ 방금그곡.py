def solution(m, musicinfos):
    answer = ''
    answer_time = 0
    
    for music in musicinfos:
        
        start, end, title, code = music.split(",")
        
        # 실행시간 구하기
        start_H, start_M = map(int, start.split(":"))
        end_H, end_M = map(int, end.split(":"))
        time = (end_H - start_H) * 60 + (end_M - start_M)
        
        # 코드를 시간만큼 재생
        time_temp = 0
        m_temp = 0
        code_temp = 0
        n = len(code)
        while time_temp <= time:
            
            if m_temp == len(m):
                if code[code_temp%n] != "#":
                    if answer_time < time:
                        answer = title
                        answer_time = time
                    break
                else:
                    m_temp = 0
                    
            print(m[m_temp], code[code_temp%n])    
            if m[m_temp] == code[code_temp%n]:
                m_temp += 1
                code_temp += 1
            else:
                m_temp = 0
                if m[0] != code[code_temp%n]:
                    code_temp += 1 
                    
            
            if code[code_temp%n] != "#":
                time_temp += 1
            

    if answer == "":
        answer = "(None)"
    return answer