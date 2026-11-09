def move_left(number, answer):
    return answer+'L', ((number - 1) // 3, (number - 1) % 3)

def move_right(number, answer):
    return answer+'R', ((number - 1) // 3, (number - 1) % 3)

def check_di(number, left_hand, right_hand, hand):
    number_lo = ((number - 1) // 3, (number - 1) % 3)
    left_diff = abs(left_hand[0] - number_lo[0]) + abs(left_hand[1] - number_lo[1])
    right_diff = abs(right_hand[0] - number_lo[0]) + abs(right_hand[1] - number_lo[1])
    print(number, left_diff, right_diff)
    if left_diff > right_diff:
        return "right"
    elif left_diff == right_diff:
        return hand
    else:
        return "left"

def solution(numbers, hand):
    answer = ''
    left_hand, right_hand = (3, 0), (3, 2)
    for number in numbers:
        if number in [1, 4, 7]:
            answer, left_hand = move_left(number, answer)
        elif number in [3, 6, 9]:
            answer, right_hand = move_right(number, answer)
        else:
            if number == 0:
                number = 11
            
            di = check_di(number, left_hand, right_hand, hand)
            
            if di == "left":
                answer, left_hand = move_left(number, answer)
            else:
                answer, right_hand = move_right(number, answer)
    return answer