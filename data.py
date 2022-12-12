import json
from player import game


def check_score():
    with open('player_data.json', 'r') as player_data:
        player_check = json.load(player_data)
        score_dict = {}
        for data in player_check['user_data']:
            score_dict[int(data['score'])] = data['name']
        sort_keys = sorted(score_dict.keys())
        sort_score = {key: score_dict[key] for key in sort_keys}
        first_score = list(sort_score)[-1]
        first_player = list(sort_score.values())[-1]
        second_score = list(sort_score)[-2]
        second_player = list(sort_score.values())[-2]
        third_score = list(sort_score)[-3]
        third_player = list(sort_score.values())[-3]
        return first_score, first_player, second_score, second_player, third_score, third_player


def user_check(username):
    if len(username) > 12:
        print('Username must not more than 12 characters.')
    elif len(username) < 3:
        print('Username must be more than 3 characters.')
    else:
        return True


def pass_strength(password):
    capital_alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small_alphabets = 'abcdefghijklmnopqrstuvwxyz'
    digits = '1234567890'
    if len(password) >= 8:
        cap = 0
        low = 0
        digit = 0
        invalid = []
        for check in password:
            if check in capital_alphabets:
                cap += 1
            elif check in small_alphabets:
                low += 1
            elif check in digits:
                digit += 1
            else:
                invalid.append(check)
        if cap >= 1 and low >= 1 and digit >= 1 and len(invalid) == 0:
            return True
        elif len(invalid) > 0:
            print(f'{invalid} are invalid characters')
        elif cap == 0:
            print('Password must contain at least 1 capital character')
        elif low == 0:
            print('Password must contain at least 1 lower character')
        elif digit == 0:
            print('Password must contain at least 1 digit')
    else:
        print('Password must be 8 or more character.')


class Data():
    def __init__(self):
        self.username = ''
        self.password = ''
        self.score = 0

    # game start menu when user tried to sign up or log in
    def game_start(self):
        print('@~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@')
        # story
        print("After the coming of dictatorship name Tuutle, village turtle get protest,\n"
              "civil war, everyone tried to revolutionize. all get jailed and all are\n"
              "messed up. But in the darkest night there'll always be a brightest day,\n"
              "the bravest one, "+'\33[31m'+f'{self.username}'+'\33[0m'+", get UNLEASHED!!! to help family, friends,\n"
              "and everyone else, this will get revenge.")
        print('@~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@')
        print('Press "U" to unleash.')
        select = input('Unleashed? : ')
        if select.lower() == 'u':
            # start game
            self.score = game(self.username)
        else:
            return None

    def log_in_check(self):
        with open('player_data.json', 'r') as player_data:
            player_check = json.load(player_data)
            player_and_pass = {}
            for player in player_check['user_data']:
                player_and_pass[player['name']] = player['password']
        while True:
            self.username = input('Enter Name : ')
            if self.username in player_and_pass:
                while True:
                    self.password = input('Enter password : ')
                    if self.password == player_and_pass[self.username]:
                        print('Log In successfully.')
                        # play game
                        self.game_start()
                        self.data_update()
                        return True
                    elif str(self.password).lower() == 'q':
                        break
                    else:
                        print('Wrong password, please try again.\n'
                              'Or Press Q to go back')
                break
            elif str(self.username).lower() == 'q':
                break
            else:
                print('Username not found, try again.\n'
                      'Or Press Q to go back')

    def sign_up_check(self):
        user_list = []
        with open('player_data.json', 'r') as player_data:
            player = json.load(player_data)
            for name in player['user_data']:
                user_list.append(name['name'])
        while True:
            self.username = input('Enter Your Name : ')
            if self.username not in user_list:
                if user_check(self.username):
                    while True:
                        print('Password must contain at least 8 characters, 1 digit,\n'
                              '1 capital alphabet and 1 lower alphabet.')
                        self.password = input('Enter Your Password : ')
                        if pass_strength(self.password):
                            player["user_data"].append(
                                {"name": self.username, "password":
                                    self.password, "score": 0})
                            with open('player_data.json', 'w') as player_data:
                                json.dump(player, player_data, indent=4)
                            print('Log In successfully')
                            # play game
                            self.game_start()
                            self.data_update()
                            return True
                        elif str(self.password).lower() == 'q':
                            break
                        else:
                            print('password invalid try again.\n'
                                  'Or Press Q to go back.')
                    break
                else:
                    print('please try again.\n'
                          'Or Press Q to go back.')
            elif str(self.username).lower() == 'q':
                break
            else:
                print('This username already existed.\n'
                      'Or Press Q to go back.')

    def data_update(self):
        with open('player_data.json', 'r+') as player_data:
            player = json.load(player_data)
        for user in player["user_data"]:
            if self.username == user['name']:
                if self.score > user['score']:
                    user['score'] = self.score
                    break
        with open('player_data.json', 'w') as player_data:
            json.dump(player, player_data, indent=4)