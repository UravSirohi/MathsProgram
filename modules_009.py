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
        '%': operator.mod,
    }
    if_not_set_90 = False
    mod_set = False
    min_number_when_power = 0
    root_power = 0
    if_integer = False
    is_mod_before = False
    if_division_before_no = ''
    if_root_before_no_2 = ''
    choose_operator(power_root_set, div_set, x, y, win_streak, question_number, skipped, skipped_idling,
                    power_root_set_2, operators, if_not_set_90, min_number_when_power, root_power, root_set, if_integer,
                    if_division_before_no, if_root_before_no_2, mod_set, is_mod_before)


def choose_operator(power_root_set, div_set, x, y, win_streak, question_number, skipped, skipped_idling,
                    power_root_set_2, operators, if_not_set_90, min_number_when_power, root_power, root_set, if_integer,
                    if_division_before_no, if_root_before_no_2, mod_set, is_mod_before):
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
    do_you_want_mod(operators, power_root_set, x, y, win_streak, question_number, div_set, skipped, skipped_idling,
                    power_root_set_2, if_not_set_90, min_number_when_power, root_power, root_set, if_integer,
                    if_division_before_no, if_root_before_no_2, mod_set, is_mod_before)


def do_you_want_mod(operators, power_root_set, x, y, win_streak, question_number, div_set, skipped, skipped_idling,
                    power_root_set_2, if_not_set_90, min_number_when_power, root_power, root_set, if_integer,
                    if_root_before_no, if_root_before_no_2, mod_set, is_mod_before):
    if not mod_set:
        idling_99 = 0
        if__idling = False
        while True:
            if not if__idling:
                do_you_mod_want = input('''Would you like modular arithmetic to be in this program?
>>>''').lower()
            else:
                do_you_mod_want = input('''>>>''').lower()
            if do_you_mod_want == 'y' or do_you_mod_want == 'yes':
                break
            elif do_you_mod_want == 'n' or do_you_mod_want == 'no':
                if is_mod_before:
                    pass
                else:
                    operators.pop('%')
                    is_mod_before = True
                break
            else:
                idling_99 += 1
                if idling_99 > 3:
                    print(f'''{Fore.RED}{Style.BRIGHT}You have failed to provide a straight answer, due to that 
the program has automatically shut down to prevent idling.''')
                    quit()
                print("Sorry I don't understand that...Yes or no please")
    mod_set = True
    do_you_want_powers(operators, power_root_set, x, y, win_streak, question_number, div_set, skipped, skipped_idling,
                       power_root_set_2, if_not_set_90, min_number_when_power, root_power, root_set, if_integer,
                       if_root_before_no, if_root_before_no_2, mod_set, is_mod_before)


def do_you_want_powers(operators, power_root_set, x, y, win_streak, question_number, div_set, skipped, skipped_idling,
                       power_root_set_2, if_not_set_90, min_number_when_power, root_power, root_set, if_integer,
                       if_root_before_no, if_root_before_no_2, mod_set, is_mod_before):
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
                      if_root_before_no, if_root_before_no_2, mod_set, is_mod_before)


def do_you_want_roots(operators, power_root_set, x, y, win_streak, question_number, div_set, skipped, skipped_idling,
                      power_root_set_2, if_not_set_90, min_number_when_power, root_power, root_set, if_integer,
                      if_root_before_no, if_root_before_no_2, mod_set, is_mod_before):
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
                      if_root_before_no, if_root_before_no_2, mod_set, is_mod_before)


def choose_power_root(operators, power_root_set, x, y, win_streak, question_number, div_set, skipped, skipped_idling,
                      power_root_set_2, if_not_set_90, min_number_when_power, root_power, root_set, if_integer,
                      if_root_before_no, if_root_before_no_2, mod_set, is_mod_before):
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
    question(operators, x, y, win_streak, question_number, div_set, min_number_when_power, power_root_set, skipped,
             skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer, if_root_before_no,
             if_root_before_no_2, mod_set, is_mod_before)


def question(operators, x, y, win_streak, question_number, div_set, min_number_when_power, power_root_set, skipped,
             skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer, if_root_before_no,
             if_root_before_no_2, mod_set, is_mod_before):
    operation = random.choice(list(operators.keys()))
    first_number = operation_if_power('f', x, y, min_number_when_power, root_power, operation)
    second_number = operation_if_power('', x, y, min_number_when_power, root_power, operation)
    if skipped_idling > 3:
        print(f'''{Fore.RED}{Style.BRIGHT}You have failed to provide a straight answer, due to that 
the program has automatically shut down to prevent idling.''')
        quit()
    calc_answer = float(operators.get(operation)(first_number, second_number))
    validate_user_answer(first_number, second_number, operation, calc_answer, win_streak,
                         question_number, x, y, div_set, operators, min_number_when_power, power_root_set, skipped,
                         skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer,
                         if_root_before_no, if_root_before_no_2, mod_set, is_mod_before)


def validate_user_answer(first_number, second_number, operation, calc_answer, win_streak,
                         question_number, x, y, div_set, operators, min_number_when_power, power_root_set, skipped,
                         skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer,
                         if_root_before_no, if_root_before_no_2, mod_set, is_mod_before):
    idling_6 = 0
    if_idling = False
    while True:
        try:
            if not if_idling:
                if operation == '%':
                    user_answer = input(f'''What is {first_number} mod({second_number})?
>>>''').lower()
                else:
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
                        'restart' or user_answer == 'help' or user_answer == '.help' or user_answer == 'stop':
                    pass
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
    check_user_answer(calc_answer, user_answer, win_streak, question_number, x, y, div_set, operators,
                      min_number_when_power, power_root_set, skipped, skipped_idling, power_root_set_2, if_not_set_90,
                      root_power, root_set, if_integer, if_root_before_no, if_root_before_no_2, mod_set, is_mod_before)


def check_user_answer(calc_answer, user_answer, win_streak, question_number, x, y, div_set, operators,
                      min_number_when_power, power_root_set, skipped, skipped_idling, power_root_set_2, if_not_set_90,
                      root_power, root_set, if_integer, if_root_before_no, if_root_before_no_2, mod_set, is_mod_before):
    if user_answer == 'quit' or user_answer == 'stop':
        quit_0(operators, x, y, win_streak, question_number, div_set, min_number_when_power, power_root_set, skipped,
               skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer, if_root_before_no,
               if_root_before_no_2, mod_set, is_mod_before)
    elif user_answer == 'settings' or user_answer == 'setting':
        settings(operators, min_number_when_power, x, y, win_streak, question_number, div_set, power_root_set, skipped,
                 skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer, if_root_before_no,
                 if_root_before_no_2, mod_set, is_mod_before)
    elif user_answer == 'restart':
        set_restart()
    elif user_answer == 'skip' or user_answer == 'skip question':
        skip_max(win_streak, question_number, x, y, power_root_set, skipped, skipped_idling, operators,
                 min_number_when_power, div_set, power_root_set_2, if_not_set_90,
                 root_power, root_set, if_integer, if_root_before_no, if_root_before_no_2, mod_set, is_mod_before)
    elif user_answer == 'help' or user_answer == '.help':
        help_0(operators, x, y, win_streak, question_number, div_set, min_number_when_power, power_root_set, skipped,
               skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer, if_root_before_no,
               if_root_before_no_2, mod_set, is_mod_before)
    elif round(calc_answer, 2) == float(user_answer) or calc_answer == float(user_answer):
        correct(win_streak, question_number, operators, min_number_when_power, div_set, x, y, power_root_set, skipped,
                skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer, if_root_before_no,
                if_root_before_no_2, mod_set, is_mod_before)
    else:
        wrong_answer(win_streak, calc_answer)


def correct(win_streak, question_number, operators, min_number_when_power, div_set, x, y, power_root_set, skipped,
            skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer, if_root_before_no,
            if_root_before_no_2, mod_set, is_mod_before):
    print("Well done.")
    win_streak += 1
    question_number += 1
    if question_number == 8:
        was_that_easy(x, y, operators, div_set, win_streak, min_number_when_power, question_number, power_root_set,
                      skipped, skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer,
                      if_root_before_no, if_root_before_no_2, mod_set, is_mod_before)
    choose_operator(power_root_set, div_set, x, y, win_streak, question_number, skipped, skipped_idling,
                    power_root_set_2, operators, if_not_set_90, min_number_when_power, root_power, root_set, if_integer,
                    if_root_before_no, if_root_before_no_2, mod_set, is_mod_before)


def wrong_answer(win_streak, calc_answer):
    calc_answer_2 = isinstance(calc_answer, int)
    if calc_answer_2:
        print(f"Incorrect, the correct answer was {calc_answer}."
              f" Your win streak was {win_streak}.")
    elif not calc_answer_2:
        calc_answer_2_1 = round(calc_answer)
        print(f'''Incorrect, the correct answer was {calc_answer} or rounded to down nearest integer {calc_answer_2_1}.
Your win streak was {win_streak}.''')
    idling = 0
    while True:
        restart = input('''Would you like to play again?
>>>''').lower()
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
             if_root_before_no_2, mod_set, is_mod_before):
    idling_3 = 0
    print(f'{Fore.RED}{Style.BRIGHT}_______________________________________________________________________')
    print(f'''Notice: {Style.NORMAL}{Fore.LIGHTCYAN_EX} you will have to complete the maths question after specifying 
which setting/settings you would like to change.''')
    while True:
        setting_which = input('''Which setting would you like to change(P for powers settings, M for mod, 
D for division or A for all three)?
>>>''').lower()
        if setting_which == 'd':
            div_set = False
            break
        elif setting_which == 'a' or setting_which == 'all':
            power_root_set_2 = False
            power_root_set = False
            div_set = False
            mod_set = False
            break
        elif setting_which == 'p':
            power_root_set_2 = False
            power_root_set = False
            root_set = False
            break
        elif setting_which == 'm':
            mod_set = False
        else:
            idling_3 += 1
            if idling_3 == 3:
                print(f'''{Fore.RED}{Style.BRIGHT}You have failed to provide a straight answer, due to that 
the program has automatically shut down to prevent idling.''')
                quit()
            print("Sorry I don't understand that...P, D, M or A please")
    question(operators, x, y, win_streak, question_number, div_set, min_number_when_power, power_root_set, skipped,
             skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer, if_root_before_no,
             if_root_before_no_2, mod_set, is_mod_before)


def was_that_easy(x, y, operators, div_set, win_streak, min_number_when_power, question_number, power_root_set, skipped,
                  skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer, if_root_before_no,
                  if_root_before_no_2, mod_set, is_mod_before):
    idling_2 = 0
    while True:
        harder = input('''Was that easy?
>>>''').lower()
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
            if idling_2 == 4:
                print(f'''{Fore.RED}{Style.BRIGHT}You have failed to provide a straight answer, due to that 
the program has automatically shut down to prevent idling.''')
                quit()
            print("Sorry I don't understand that...Yes or no please")
    if x < 2:
        x = 2
    if y < 6:
        y = 6
    question(operators, x, y, win_streak, question_number, div_set, min_number_when_power, power_root_set, skipped,
             skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer, if_root_before_no,
             if_root_before_no_2, mod_set, is_mod_before)


def skip_max(win_streak, question_number, x, y, power_root_set, skipped, skipped_idling, operators,
             min_number_when_power, div_set, power_root_set_2, if_not_set_90,
             root_power, root_set, if_integer, if_root_before_no, if_root_before_no_2, mod_set, is_mod_before):
    skipped -= 1
    if skipped >= 0:
        print(f"You have {skipped} skip powers left")
        question(operators, x, y, win_streak, question_number, div_set, min_number_when_power, power_root_set, skipped,
                 skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer, if_root_before_no,
                 if_root_before_no_2, mod_set, is_mod_before)
    else:
        skipped_idling += 1
        print('You have no skip powers left')
    question(operators, x, y, win_streak, question_number, div_set, min_number_when_power, power_root_set, skipped,
             skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer, if_root_before_no,
             if_root_before_no_2, mod_set, is_mod_before)


def quit_0(operators, x, y, win_streak, question_number, div_set, min_number_when_power, power_root_set, skipped,
           skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer, if_root_before_no,
           if_root_before_no_2, mod_set, is_mod_before):
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
            question(operators, x, y, win_streak, question_number, div_set, min_number_when_power, power_root_set,
                     skipped, skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer,
                     if_root_before_no, if_root_before_no_2, mod_set, is_mod_before)
        else:
            idling_101 += 1
            if idling_101 > 3:
                print(f'''{Fore.RED}{Style.BRIGHT}You have failed to provide a straight answer, due to that 
the program has automatically shut down to prevent idling.''')
                quit()
            print("Sorry I don't understand that...Yes or No please")


def help_0(operators, x, y, win_streak, question_number, div_set, min_number_when_power, power_root_set, skipped,
           skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer, if_root_before_no,
           if_root_before_no_2, mod_set, is_mod_before):
    print('''
quit - End program
settings - Change answer to hard/irrational division question
restart - Restart program
skip - Skip the question, use this wisely you have only start with 3
    ''')
    question(operators, x, y, win_streak, question_number, div_set, min_number_when_power, power_root_set, skipped,
             skipped_idling, power_root_set_2, if_not_set_90, root_power, root_set, if_integer, if_root_before_no,
             if_root_before_no_2, mod_set, is_mod_before)


def operation_if_power(which_number, x, y, min_number_when_power, root_power, operation):
    if operation == '**':
        if which_number == 'f':
            return random.randint(min_number_when_power, 9)
        else:
            return random.randint(root_power, 3)
    else:
        return random.randint(x, y)
