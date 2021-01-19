# -*- coding: utf-8 -*-

import random


def get_random_number():
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    # isdigit() 으로 숫자로만 구성된 문자열인지 확인
    # 불린형으로 반환됨
    result = user_input_number.isdigit()
    return result


def is_between_100_and_999(user_input_number):
    # 단순 부등식 검사
    if 100 <= int(user_input_number) < 1000:
        result = True
    else:
        result = False
    return result


def is_duplicated_number(three_digit):
    # 우선 중복 없다고 가정
    result = False
    # 중복 검사
    for i in three_digit:
        if three_digit.count(i) > 1:
            result = True
            break
    return result


def is_validated_number(user_input_number):
    result = None
    # 조건 하나라도 false 면 invalid
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
    # 첫째자리엔 0이 오면 안되므로 먼저 지정
    hundred = random.randint(1, 9)
    # 첫째자리에 들어온 숫자 제외 하고 샘플링
    candidates = set(range(0, 10)) - set([hundred])
    generated_lst = [hundred] + random.sample(candidates, 2)
    # 리스트 -> 문자열 -> 정수
    result = int(''.join(map(str, generated_lst)))
    return result


def get_strikes_or_ball(user_input_number, random_number):
    result = [0, 0]
    # 유저 넘버의 자릿수별로 검사
    for idx in range(len(user_input_number)):
        # 우선 사용자의 번호가 정답에 포함되있는지 조사
        if user_input_number[idx] in random_number:
            # 자릿수 까지 같으면 strike
            if user_input_number[idx] == random_number[idx]:
                # strike
                result[0] += 1
            # 해당 넘버에 대해 자릿수는 같지 않으면 ball
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
                # 0 입력시 프로그램 종료
                if user_input == '0':
                    break
                # validation 루프 탈출
                if is_validated_number(user_input):
                    break
                print('Wrong Input, Input again')
                user_input = input('Input guess number : ')
            # 0 입력시 프로그램 종료
            if user_input == '0':
                break
            # Strike ball 계산
            strike, ball = get_strikes_or_ball(user_input, random_number)
            print('Strikes : {} , Balls : {}'.format(strike, ball))
            # 종료 조건 1
            if strike == 3:
                break
        # 종료 조건 2
        if user_input == '0':
            break
        # input validation
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
