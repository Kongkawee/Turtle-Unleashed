#TURTLE UNLEASHED

###Overview

#####This is an adventure-rpg game that roles players as a Turtle to fight against the endless of the evil enemies. Get points as much as enemies you’ve defeated and buff you’ve collected.


###Features

#####How game work?

    1. After run the program player can make a decision.
        1 is log In to the game if player already have username and password
        2 is Sign up for the new player who wants to play the game and the program will create a new account.
        3 is tutorial.
        4 is buff and enemy guide.
        5 is quit the program.
    2. If a player wants to play the game choose Log In or Sign Up.
    3. You can press U (or u) to run the game.
    4. When the game starts, the enemies are spawning and trying to catch you. 
    5. Players can choose to either run or fight them back.
    6. Players also can pick buffs to provide advantages against them.
    7. After players have been catched by specific amounts, the game will automatically end. and exit the program.
    8. Try to run the program again the top three players who got the most score will be shown on the leaderboard.


###Program’s Requirements

#####There are 4 Python Modules & Libraries required in this program.

    turtle: Used for Gameplay and Graphic
    math: Used for some of mathematic movement in the game
    json: Used for storing user data included username, password and score
    random: Used for Gameplay


###Program Design

#####There are 5 classes in this program

    Player: This class is used for creating and controlling player character status.
    Boost: This class is used for creating buffs and spawn at random positions.
    Bullet: This class is used for creating a player's gun and bullet.
    Enemy: This class is used for creating enemies and set spawn at random positions.
    Data: This class is used for running all the game stuff and collecting players data.


###Code Structure

#####main_menu.py: Contain the main menu of the game.

    player.py: Contains all game stuff.
    data.py: Contains and manages player’s data.
    player_data.json: Contains player’s data in json format.