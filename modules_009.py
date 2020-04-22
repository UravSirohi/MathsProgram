import operator
import random
from colorama import *


def set_restart():
    win_streak = 0
    x = 2
    y = 11
    question_number = 0
    div_set = False
    power_root_set = False
    power_root_set_2 = False
    root_set = False
    skipped = 3
    skipped_idling = 0
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow,
    }
    if_not_set_90 = False
    min_number_when_power = 0
    root_power = 0
    if_integer = False
    if_division_before_no = ''
    if_root_before_no_2 = ''
    choose_operator(power_root_set, div_set, x, y, win_streak, question_number, skipped, skipped_idling,
                    power_root_set_2, operators, if_not_set_90, min_number_when_power, root_power, root_set, if_integer,
                    if_division_before_no, if_root_before_no_2)


def choose_operator(power_root_set, div_set, x, y, win_streak, question_number, skipped, skipped_idling,
                    power_root_set_2, operators, if_not_set_90, min_number_when_power, root_power, root_set, if_integer,
                    if_division_before_no, if_root_before_no_2):
    if not div_set:
        if_idling_2 = False
        idling_7 = 0
        while True:
            if not if_idling_2:
                operators_div = input('''Do you want this program to contain irrational/hard divide questions?
>>>''').lower()
            else:
                operators_div = input('''>>>''').lower()
            if operators_div == 'yes' or operators_div == 'y' or operators_div == 'maybe':
                break
            elif operators_div == 'no' or operators_div == 'n':
                if if_division_before_no == '/':
                    pass
                elif not if_division_before_no == '/':
                    operators.pop('/')
                    if_division_before_no = '/'
                break
            else:
                idling_7 += 1
                if_idling_2 = True
                if idling_7 == 4:
                    print(f'''{Fore.RED}{Style.BRIGHT}You have failed to provide a straight answer, due to that 
the program has automatically shut down to prevent idling.''')
                    quit()
                print("Sorry I don't understand that...Yes or no please")
    div_set = True
    do_you_want_powers(operators, power_root_set, x, y, win_streak, question_number, div_set, skipped, skipped_idling,
                       power_root_set_2, if_not_set_90, min_number_when_power, root_power, root_set, if_integer,
                       if_division_before_no, if_root_before_no_2)


def do_you_want_powers(operators, power_root_set, x, y, win_streak, question_number, div_set, skipped, skipped_idling,
                       power_root_set_2, if_not_set_90, min_number_when_power, root_power, root_set, if_integer,
                       if_root_before_no, if_root_before_no_2):
    if_idling_56 = False
    idling_99 = 0
    if not power_root_set_2:
        while True:
            if not if_idling_56:
                if_power = input('''Do you want powers in this program?
>>>''').lower()
            else:
                if_power = input('''>>>''').lower()
            if if_power == 'yes' or if_power == 'y' or if_power == 'maybe':
                break
            elif if_power == 'no' or if_power == 'n':
                if if_root_before_no_2 == 'n':
                    pass
                elif not if_root_before_no_2 == 'n':
                    operators.pop('**')
                    if_root_before_no_2 = 'n'
                root_set = True
                power_root_set = True
                if_not_set_90 = True
                break
            else:
                idling_99 += 1
                if idling_99 > 3:
                    print(f'''{Fore.RED}{Style.BRIGHT}You have failed to provide a straight answer, due to that 
                    the program has automatically shut down to prevent idling.''')
                    quit()
                print("Sorry I don't understand that...Yes or no please")
    power_root_set_2 = True
    do_you_want_roots(operators, power_root_set, x, y, win_streak, question_number, div_set, skipped, skipped_idling,
                      power_root_set_2, if_not_set_90, min_number_when_power, root_power, root_set, if_integer,
                      if_root_before_no, if_root_before_no_2)


def do_you_want_roots(operators, power_root_set, x, y, win_streak, question_number, div_set, skipped, skipped_idling,
                      power_root_set_2, if_not_set_90, min_number_when_power, root_power, root_set, if_integer,
                      if_root_before_no, if_root_before_no_2):
    idling_826 = 0
    if_idling_34 = False
    if not root_set:
        while True:
            if not if_idling_34:
                are_roots_wanted = input('''Do you want roots to be included in this program?
>>>''').lower()
            else:
                are_roots_wanted = input('''>>>''').lower()
            if are_roots_wanted == 'yes' or are_roots_wanted == 'y' or are_roots_wanted == 'maybe':
                root_power = -3
                break
            elif are_roots_wanted == 'n' or are_roots_wanted == 'no':
                break
            else:
                idling_826 += 1
                if_idling_34 = True
                if idling_826 == 4:
                    print(f'''{Fore.RED}{Style.BRIGHT}You have failed to provide a straight answer, due to that 
the program has automatically shut down to prevent idling.''')
                    quit()
                print("Sorry I don't understand that...Yes or no please")
    root_set = True
    choose_power_root(operators, power_root_set, x, y, win_streak, question_number, div_set, skipped, skipped_idling,
                      power_root_set_2, if_not_set_90, min_number_when_power, root_power, root_set, if_integer,
                      if_root_before_no, if_root_before_no_2)


def choose_power_root(operators, power_root_set, x, y, win_streak, question_number, div_set, skipped, skipped_idling,
                      power_root_set_2, if_not_set_90, min_number_when_power, root_power, root_set, if_integer,
                      if_root_before_no, if_root_before_no_2):
    if not power_root_set:
        idling_8 = 0
        if_idling_3 = False
        while True:
            if not if_idling_3:
                power_root = input('''Do you want this program to contain negative squares or cubes?
>>>''').lower()
            else:
                power_root = input('''>>>''').lower()
            if power_root == 'yes' or power_root == 'Maybe' or power_root == 'y':
                min_number_when_power = -10
                break
            elif power_root == 'no' or power_root == 'n':
                break
            else:
                idling_8 += 1
                if_idling_3 = True
                if idling_8 == 4:
                    print(f'''{Fore.RED}{Style.BRIGHT}You have failed to provide a straight answer, due to that 
the program has automatically shut down to prevent idling.''')
                    quit()
                print("Sorry I don't understand that...Yes or no please")
    power_root_set = True
    operation_if_power(operators, min_number_when_power, x, y, win_streak, question_number, div_set, power_root_set,
                       skipped, skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer,
                       if_root_before_no, if_root_before_no_2)


def operation_if_power(operators, min_number_when_power, x, y, win_streak, question_number, div_set, power_root_set,
                       skipped, skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer,
                       if_root_before_no, if_root_before_no_2):
    operation = random.choice(list(operators.keys()))
    if operation == '**':
        first_number = random.randint(min_number_when_power, 9)
        second_number = random.randint(root_power, 3)
    else:
        first_number = random.randint(x, y)
        second_number = random.randint(x, y)
    question(first_number, second_number, operation, operators, x, y, win_streak,
             question_number, div_set, min_number_when_power, power_root_set, skipped, skipped_idling, power_root_set_2,
             if_not_set_90, root_power, root_set, if_integer, if_root_before_no, if_root_before_no_2)


def question(first_number, second_number, operation, operators, x, y, win_streak,
             question_number, div_set, min_number_when_power, power_root_set, skipped, skipped_idling,
             power_root_set_2, if_not_set_90, root_power, root_set, if_integer, if_root_before_no, if_root_before_no_2):
    if skipped_idling > 3:
        print(f'''{Fore.RED}{Style.BRIGHT}You have failed to provide a straight answer, due to that 
the program has automatically shut down to prevent idling.''')
        quit()
    calc_answer = operators.get(operation)(first_number, second_number)
    calc_answer_2 = str(round(calc_answer, 2))
    validate_user_answer(first_number, second_number, operation, calc_answer_2, calc_answer, win_streak,
                         question_number, x, y, div_set, operators, min_number_when_power, power_root_set, skipped,
                         skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer,
                         if_root_before_no, if_root_before_no_2)


def validate_user_answer(first_number, second_number, operation, calc_answer_2, calc_answer, win_streak,
                         question_number, x, y, div_set, operators, min_number_when_power, power_root_set, skipped,
                         skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer,
                         if_root_before_no, if_root_before_no_2):
    idling_6 = 0
    if_idling = False
    while True:
        try:
            if not if_idling:
                user_answer = input(f'''What is {first_number} {operation} {second_number}?
>>>''').lower()
                if user_answer == 'quit' or user_answer == 'settings' or user_answer == 'setting' or user_answer == \
                        'restart' or user_answer == 'help' or user_answer == '.help' or user_answer == 'skip':
                    pass
                else:
                    user_answer = float(user_answer)
            else:
                user_answer = input('''>>>''').lower()

                if user_answer == 'quit' or user_answer == 'settings' or user_answer == 'setting' or user_answer == \
                        'restart' or user_answer == 'help' or user_answer == '.help':
                    user_answer = user_answer
                else:
                    user_answer = float(user_answer)
        except ValueError:
            idling_6 += 1
            if_idling = True
            if idling_6 == 4:
                print(f'''{Fore.RED}{Style.BRIGHT}You have failed to provide a straight answer, due to that 
the program has automatically shut down to prevent idling.''')
                quit()
            print("Sorry I don't understand that...Only numbers please")
        else:
            break
    check_user_answer(calc_answer_2, calc_answer, user_answer, win_streak, question_number,
                      x, y, div_set, operators, min_number_when_power, power_root_set, skipped, first_number,
                      second_number, operation, skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set,
                      if_integer, if_root_before_no, if_root_before_no_2)


def check_user_answer(calc_answer_2, calc_answer, user_answer, win_streak, question_number,
                      x, y, div_set, operators, min_number_when_power, power_root_set, skipped, first_number,
                      second_number, operation, skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set,
                      if_integer, if_root_before_no, if_root_before_no_2):
    if user_answer == 'quit' or user_answer == 'stop':
        quit_0(first_number, second_number, operation, operators, x, y, win_streak,
               question_number, div_set, min_number_when_power, power_root_set, skipped, skipped_idling,
               power_root_set_2, if_not_set_90, root_power, root_set, if_integer, if_root_before_no,
               if_root_before_no_2)
    elif user_answer == 'settings' or user_answer == 'setting':
        settings(operators, min_number_when_power, x, y, win_streak, question_number, div_set, power_root_set, skipped,
                 skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer, if_root_before_no,
                 if_root_before_no_2)
    elif user_answer == 'restart':
        set_restart()
    elif user_answer == 'skip' or user_answer == 'skip question':
        skip_max(win_streak, question_number, x, y, power_root_set, skipped, skipped_idling, operators,
                 min_number_when_power, div_set, first_number, second_number, operation, power_root_set_2,
                 if_not_set_90, root_power, root_set, if_integer, if_root_before_no, if_root_before_no_2)
    elif user_answer == 'help' or user_answer == '.help':
        print('''
quit - End program
settings - Change answer to hard/irrational division question
restart - Restart program
skip - Skip the question, use this wisely you have only start with 3
                ''')
        question(first_number, second_number, operation, operators, x, y, win_streak,
                 question_number, div_set, min_number_when_power, power_root_set, skipped, skipped_idling,
                 power_root_set_2, if_not_set_90, root_power, root_set, if_integer, if_root_before_no,
                 if_root_before_no_2)
    elif round(calc_answer, 2) == user_answer or calc_answer == user_answer:
        # noinspection PyArgumentList
        correct(win_streak, question_number, operators, min_number_when_power, div_set, calc_answer, calc_answer_2,
                user_answer, x, y, power_root_set, skipped, skipped_idling, power_root_set_2, if_not_set_90, root_power,
                root_set, if_integer, if_root_before_no, if_root_before_no_2)
    else:
        wrong_answer(win_streak, calc_answer, if_integer)


def correct(win_streak, question_number, operators, min_number_when_power, div_set, calc_answer, calc_answer_2,
            user_answer, x, y, power_root_set, skipped, skipped_idling, power_root_set_2, if_not_set_90, root_power,
            root_set, if_integer, if_root_before_no, if_root_before_no_2):
    print("Well done.")
    win_streak += 1
    question_number += 1
    if question_number == 8:
        was_that_easy(x, y, calc_answer, calc_answer_2, user_answer, win_streak, question_number, power_root_set,
                      skipped, skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer,
                      if_root_before_no, if_root_before_no_2)
    operation_if_power(operators, min_number_when_power, x, y, win_streak, question_number, div_set, power_root_set,
                       skipped, skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer,
                       if_root_before_no, if_root_before_no_2)


def wrong_answer(win_streak, calc_answer, if_integer):
    try:
        round(int(calc_answer))
    except ValueError:
        if_integer = True
    if if_integer:
        print(f"Incorrect, the correct answer was {calc_answer} or rounded to nearest integer {round(calc_answer)}."
              f" Your win streak was {win_streak}.")
    else:
        print(f"Incorrect, the correct answer was {calc_answer}."
              f" Your win streak was {win_streak}.")
    idling = 0
    if_idling__4 = False
    while True:
        if not if_idling__4:
            restart = input('''Would you like to play again?
>>>''').lower()
        else:
            restart = input('''>>>''').lower()
        if restart == "yes" or restart == 'y':
            set_restart()
        elif restart == "no" or restart == 'n':
            quit()
        else:
            idling += 1
            if idling > 3:
                print(f'''{Fore.RED}{Style.BRIGHT}You have failed to provide a straight answer, due to that 
the program has automatically shut down to prevent idling.''')
                quit()
            print('''Sorry I don't understand that...Yes or no please''')


def settings(operators, min_number_when_power, x, y, win_streak, question_number, div_set, power_root_set, skipped,
             skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer, if_root_before_no,
             if_root_before_no_2):
    idling_3 = 0
    if_idling___3 = False
    while True:
        if not if_idling___3:
            setting_which = input('''Which setting would you like to change(P for powers settings, 
D for division or B for both)?
>>>''').lower()
        else:
            setting_which = input('''>>>''').lower()
        if setting_which == 'd':
            div_set = False
            choose_operator(power_root_set, div_set, x, y, win_streak, question_number, skipped, skipped_idling,
                            power_root_set_2, operators, if_not_set_90, min_number_when_power, root_power, root_set,
                            if_integer, if_root_before_no, if_root_before_no_2)
            break
        if setting_which == 'b':
            power_root_set = False
            div_set = False
            do_you_want_powers(operators, power_root_set, x, y, win_streak, question_number, div_set, skipped,
                               skipped_idling,
                               power_root_set_2, if_not_set_90, min_number_when_power, root_power, root_set,
                               if_integer, if_root_before_no, if_root_before_no_2)
        if setting_which == 'p':
            power_root_set_2 = False
            power_root_set = False
            root_set = False
            do_you_want_powers(operators, power_root_set, x, y, win_streak, question_number, div_set, skipped,
                               skipped_idling,
                               power_root_set_2, if_not_set_90, min_number_when_power, root_power, root_set,
                               if_integer, if_root_before_no, if_root_before_no_2)
        else:
            idling_3 += 1
            if idling_3 == 3:
                print(f'''{Fore.RED}{Style.BRIGHT}You have failed to provide a straight answer, due to that 
the program has automatically shut down to prevent idling.''')
                quit()
            print("Sorry I don't understand that...P, D or B please")
    operation_if_power(operators, min_number_when_power, x, y, win_streak, question_number, div_set, power_root_set,
                       skipped, skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer,
                       if_root_before_no, if_root_before_no_2)


def was_that_easy(x, y, calc_answer, calc_answer_2, user_answer, win_streak, question_number, power_root_set, skipped,
                  skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer, if_root_before_no,
                  if_root_before_no_2):
    idling_2 = 0
    if_idling___4 = False
    while True:
        if not if_idling___4:
            harder = input('''Was that easy?
>>>''').lower()
        else:
            harder = input('''>>>''').lower()
        if harder == 'yes' or harder == 'maybe' or harder == 'y':
            x += 1
            y += 2
            break
        elif harder == 'no' or harder == 'n':
            x -= 1
            y -= 1
            break
        else:
            idling_2 += 1
            if_idling___4 = True
            if idling_2 == 4:
                print(f'''{Fore.RED}{Style.BRIGHT}You have failed to provide a straight answer, due to that 
the program has automatically shut down to prevent idling.''')
                quit()
            print("Sorry I don't understand that...Yes or no please")
    if x < 2:
        x = 2

    if y < 6:
        y = 6
    operation_if_power(calc_answer, calc_answer_2, user_answer, win_streak, question_number, x, y, power_root_set,
                       skipped, skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer,
                       if_root_before_no, if_root_before_no_2)


def skip_max(win_streak, question_number, x, y, power_root_set, skipped, skipped_idling, operators,
             min_number_when_power, div_set, first_number, second_number, operation, power_root_set_2, if_not_set_90,
             root_power, root_set, if_integer, if_root_before_no, if_root_before_no_2):
    skipped -= 1
    if skipped >= 0:
        print(f"You have {skipped} skip powers left")
        operation_if_power(operators, min_number_when_power, x, y, win_streak, question_number, div_set, power_root_set,
                           skipped, skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer,
                           if_root_before_no, if_root_before_no_2)
    else:
        skipped_idling += 1
        print('You have no skip powers left')
    question(first_number, second_number, operation, operators, x, y, win_streak, question_number,
             div_set, min_number_when_power, power_root_set, skipped, skipped_idling, power_root_set_2, if_not_set_90,
             root_power, root_set, if_integer, if_root_before_no, if_root_before_no_2)


def quit_0(first_number, second_number, operation, operators, x, y, win_streak,
           question_number, div_set, min_number_when_power, power_root_set, skipped, skipped_idling, power_root_set_2,
           if_not_set_90, root_power, root_set, if_integer, if_root_before_no, if_root_before_no_2):
    idling_101 = 0
    if_idling_101 = False
    while True:
        if not if_idling_101:
            should_quit_2 = input('''Are you sure you would like to quit?
>>>''').lower()
            if_idling_101 = True
        else:
            should_quit_2 = input('''>>>''').lower()
        if should_quit_2 == 'yes' or should_quit_2 == 'y':
            print(Fore.RED, Style.BRIGHT + '''Game ended''')
            quit()
        elif should_quit_2 == 'no' or should_quit_2 == 'n':
            question(first_number, second_number, operation, operators, x, y, win_streak,
                     question_number, div_set, min_number_when_power, power_root_set, skipped, skipped_idling,
                     power_root_set_2, if_not_set_90, root_power, root_set, if_integer, if_root_before_no,
                     if_root_before_no_2)
        else:
            idling_101 += 1
            if idling_101 > 3:
                print(f'''{Fore.RED}{Style.BRIGHT}You have failed to provide a straight answer, due to that 
the program has automatically shut down to prevent idling.''')
                quit()
            print("Sorry I don't understand that...Yes or No please")
