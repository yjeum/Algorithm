def solution(s):
    num = list(map(int, s.split()))
    nums = [str(min(num)), str(max(num))]
    answer = ' '.join(nums)
    return answer