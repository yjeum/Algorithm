import heapq

def solution(jobs):
    ready_q = []
    cur = 0
    time = 0
    answer = 0
    
    # 1. 작업을 시작하는 시간을 기준으로 정렬
    jobs = sorted(jobs, key = lambda x : x[0])

    while cur < len(jobs) or ready_q:
        
        # 2. 작업 가능한 디스크 ready_q에 넣어주기
        while cur < len(jobs) and jobs[cur][0] <= time:
            heapq.heappush(ready_q, (jobs[cur][1], jobs[cur][0]))
            cur += 1
        
        # 3. ready_q에 있는 작업 실행
        if ready_q:
            work_time, in_time = heapq.heappop(ready_q)
            time += work_time
            answer += (time - in_time)
        else:
            time += 1
            
    return answer // len(jobs)