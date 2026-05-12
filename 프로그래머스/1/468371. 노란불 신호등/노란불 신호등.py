import math

def solution(signals):
    # 최대 검색 기간 :: 최대공배수
    cycles = []
    for signal in signals:
        cycles.append(sum(signal))

    max_time = 1
    for cycle in cycles:
        max_time = max_time * cycle // math.gcd(max_time, cycle)

    # 모두 노란불일 시간 확인
    for i in range(1, max_time + 1):
        flg = True

        for green, yellow, red in signals:
            period = green + yellow + red
            
            # 현재 상태
            state = (i - 1) % period + 1

            if state <= green or state >= (green + yellow + 1):
                flg = False
                break

        # 모두 노란불일 경우
        if flg:
            return i

    return -1