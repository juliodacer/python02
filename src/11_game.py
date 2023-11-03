import random

rounds = 1
user_win = 0
computer_win = 0


def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('Piedra, papel o tijera: ').lower()

    if not user_option in options:
        print('Esta opción no es valida')
        return None, None

    computer_option = random.choice(options)

    print('User option => ', user_option)
    print('Computer option => ', computer_option)
    return user_option, computer_option


def check_rules(user_option, computer_option):
    if user_option == computer_option:
        print('Empate!')
        continue
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('user gano!')
            user_win += 1
        else:
            print('papel gana a piedra')
            print('Computer gano!')
            computer_win += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel ganaa piedra')
            print('user gano!')
            user_win += 1
        else:
            print('tijera gana a papel')
            print('computer gano!')
            computer_win += 1
    elif user_option == 'tijera':
        if computer_option == 'piedra':
            print('piedra gana a tijera')
            print('computer gano!')
            computer_win += 1
        else:
            print('tijera gana a papel')
            print('user gano!')
            user_win += 1

while user_win < 2 and computer_win < 2:
    print('RONDA', rounds)
    print('USER_WIN', user_win)
    print('COMPUTER_WIN', computer_win)
    rounds += 1

    user_option, computer_option = choose_options()

    if (user_win == 2):
        print('Ganó el juego USUARIO')
    if (computer_win == 2):
        print('Ganó el juego COMPUTER')
