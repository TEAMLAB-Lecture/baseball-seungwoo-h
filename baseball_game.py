# -*- coding: utf-8 -*-

import random


def get_random_number():
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    result = user_input_number.isdigit()
    return result


def is_between_100_and_999(user_input_number):
    if 100 <= int(user_input_number) < 1000:
        result = True
    else:
        result = False
    return result


def is_duplicated_number(three_digit):
    result = False
    for i in three_digit:
        if three_digit.count(i) > 1:
            result = True
            break
    return result


def is_validated_number(user_input_number):
    result = None
    if not is_digit(user_input_number):
        result = False
    elif not is_between_100_and_999(user_input_number):
        result = False
    elif is_duplicated_number(user_input_number):
        result = False
    else:
        result = True
    return result


def get_not_duplicated_three_digit_number():
    hundred = random.randint(1, 9)
    candidates = set(range(0, 10)) - set([hundred])
    generated_lst = [hundred] + random.sample(candidates, 2)
    result = int(''.join(map(str, generated_lst)))
    return result


def get_strikes_or_ball(user_input_number, random_number):
    result = [0, 0]
    for idx in range(len(user_input_number)):
        if user_input_number[idx] in random_number:
            if user_input_number[idx] == random_number[idx]:
                # strike
                result[0] += 1
            else:
                # ball
                result[1] += 1
    return result


def is_yes(one_more_input):
    result = one_more_input.lower() in ['y', 'yes']
    return result


def is_no(one_more_input):
    result = one_more_input.lower() in ['n', 'no']
    return result


def main():
    print("Play Baseball")
    while True:
        random_number = str(get_not_duplicated_three_digit_number())
        print("Random Number is : ", random_number)
        while True:
            user_input = input('Input guess number : ')
            # 사용자 입력 숫자 validation
            while True:
                if user_input == '0':
                    break
                if is_validated_number(user_input):
                    break
                print('Wrong Input, Input again')
                user_input = input('Input guess number : ')
            # if user_input == '0':
            #     break
            # Strike ball 계산
            strike, ball = get_strikes_or_ball(user_input, random_number)
            print('Strikes : {} , Balls : {}'.format(strike, ball))
            # 종료 조건
            if strike == 3:
                break
        if user_input == '0':
            break
        while True:
            continue_check = input('You win, one more(Y/N)?')
            if is_no(continue_check) or is_yes(continue_check):
                break
            print('Wrong Input, Input again')
        if is_no(continue_check):
            break
        else:
            continue
        
    print("Thank you for using this program")
    print("End of the Game")

if __name__ == "__main__":
    main()
