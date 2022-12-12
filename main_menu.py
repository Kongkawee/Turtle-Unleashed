from data import *


first_score, first_player, second_score, second_player, third_score, third_player = check_score()
data = Data()

while True:
    print()
    print('-------------------------------')
    title = '|      TURTLE UNLEASHED       |'
    score = '----------LEADERBOARD----------'
    print(f'{title:^30}')
    print(f'{score:^30}')
    print(f'| 1. {first_player:<15}{first_score:>9} |\n'
          f'| 2. {second_player:<15}{second_score:>9} |\n'
          f'| 3. {third_player:<15}{third_score:>9} |')
    print('-------------------------------')
    print('Make Your Choice!')
    print('1.Log In')
    print('2.Sign Up')
    print('3.How to play?')
    print('4.Adventure book')
    print('5.Quit')
    choice_input = input('Enter Your Choice : ')

    if choice_input in ['1', '2', '3', '4', '5']:
        choice = int(choice_input)
        if choice == 1:
            data.log_in_check()

        elif choice == 2:
            data.sign_up_check()

        elif choice == 3:
            print()
            print('This is an adventure game that allows\n'
                  'the player to move in any direction.\n'
                  '( Press "W" for North, "D" for East,\n'
                  '"A" for West, and "S" for South ) to\n'
                  'control your character and press "Enter"\n'
                  'to fire your weapon against enemies.\n'
                  'try to survive as long as you can to\n'
                  'get as many points. You can also pick up\n'
                  'the buff to provide an advantage against them.')
            print()

        elif choice == 4:
            print('@~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@')
            print('\33[40m'+'  Buff            name           ability                       '+'\33[0m\n'
                  '\33[33m'+'  yellow dot      star           gain 100 score                '+'\33[0m\n'
                  '\33[34m'+'  blue dot        shield         Immune Damage once            '+'\33[0m\n'
                  '\33[31m'+'  red dot         heart          gain an extra life            '+'\33[0m\n'
                  '\n'
                  '\33[40m'+'  Enemy           name          '+'\33[0m\n'
                  '\033[38:5:208m'+'  orange turtle   police     '+'\33[0m\n'
                  '\33[31m'+'  red turtle      soldier           '+'\33[0m\n'
                  '\33[35m'+'  purple turtle   evil_council      '+'\33[0m')
            print('@~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@')

        elif choice == 5:
            print("Farewell, Bravest one, world still need you.")
            print('See you again.')
            exit()

        else:
            print('invalid choice try again')
    else:
        print('invalid choice try again')