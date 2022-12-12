from turtle import *
import random
import math


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.life = 5
        self.shield = 0
        self.shoot = True
        self.buff = []
        self.score = 0

    def get_buff(self):
        if self.buff[-1] == 'star':
            self.score += 100

        elif self.buff[-1] == 'shield':
            if self.shield < 1:
                self.shield = 1
            else:
                self.score += 10

        elif self.buff[-1] == 'heart':
            if self.life <= 4:
                self.life += 1
            else:
                self.score += 10

    # Fire weapon
    def fire(self, enemy):
        if self.shoot:
            self.shoot = False
            gun = Bullet(self)
            enemy = gun.fire(enemy)
            self.shoot = True
            return enemy

    # move set
    def move_south(self):
        self.seth(270)
        self.forward(20)

    def move_east(self):
        self.seth(0)
        self.forward(20)

    def move_west(self):
        self.seth(180)
        self.forward(20)

    def move_north(self):
        self.seth(90)
        self.forward(20)


class Enemy(Turtle):
    def __init__(self, enemy_life, enemy_score, size):
        super().__init__(visible=False)
        self.speed(5)
        self.shape('turtle')
        enemy_color = ["red", "purple", "orange"]
        self.shapesize(size)
        self.enemy_life = enemy_life
        self.enemy_score = enemy_score
        self.size = size
        self.color(random.choice(enemy_color))
        self.penup()
        side_spawn = random.randint(1, 4)
        if side_spawn == 1:
            self.setpos(500, random.randint(-300, 300))
        elif side_spawn == 2:
            self.setpos(random.randint(-500, 500), 300)
        elif side_spawn == 3:
            self.setpos(-500, random.randint(-300, 300))
        elif side_spawn == 4:
            self.setpos(random.randint(-500, 500), -300)

    def move(self, target):
        if self.xcor() >= target.xcor():
            self.setheading(180 + (math.degrees(math.atan((target.ycor() - self.ycor())
                                                          / (target.xcor() - self.xcor())))))
            self.forward(10)
        else:
            self.setheading(math.degrees(math.atan((target.ycor() - self.ycor())
                                                   / (target.xcor() - self.xcor()))))
            self.forward(10)

    def is_collide(self, other):
        return abs(self.xcor() - other.xcor()) < 20 and abs(self.ycor() - other.ycor()) < 20


class Bullet(Turtle):
    def __init__(self, player):
        super().__init__(visible=False)
        self.player = player
        self.penup()
        self.speed(0)
        self.pensize(10)
        self.color("red")
        self.setpos(self.player.xcor(), self.player.ycor())
        self.seth(self.player.heading())

    def fire(self, enemy_list):
        self.pendown()
        check_distance = 30
        if self.heading() == 90:
            while self.ycor() < 300:
                for enemy in range(len(enemy_list)):
                    if isinstance(enemy_list[enemy], Enemy):
                        if abs(enemy_list[enemy].xcor() - self.xcor()) < enemy_list[enemy].size * 20 and abs(
                                enemy_list[enemy].ycor() - self.ycor()) < enemy_list[enemy].size * 20:
                            self.hideturtle()
                            enemy_list[enemy].hideturtle()
                            return enemy
                self.forward(check_distance)
                self.clear()
            return None

        elif self.heading() == 270:
            while self.ycor() > -300:
                for enemy in range(len(enemy_list)):
                    if isinstance(enemy_list[enemy], Enemy):
                        if abs(enemy_list[enemy].xcor() - self.xcor()) < 20 and abs(
                                enemy_list[enemy].ycor() - self.ycor()) < 20:
                            self.hideturtle()
                            enemy_list[enemy].hideturtle()
                            return enemy
                self.forward(check_distance)
                self.clear()
            return None

        elif self.heading() == 0:
            while self.xcor() < 500:
                for enemy in range(len(enemy_list)):
                    if isinstance(enemy_list[enemy], Enemy):
                        if abs(enemy_list[enemy].xcor() - self.xcor()) < 20 and abs(
                                enemy_list[enemy].ycor() - self.ycor()) < 20:
                            self.hideturtle()
                            enemy_list[enemy].hideturtle()
                            return enemy
                self.forward(check_distance)
                self.clear()
            return None

        elif self.heading() == 180:
            while self.xcor() > -500:
                for enemy in range(len(enemy_list)):
                    if isinstance(enemy_list[enemy], Enemy):
                        if abs(enemy_list[enemy].xcor() - self.xcor()) < 20 and abs(
                                enemy_list[enemy].ycor() - self.ycor()) < 20:
                            self.hideturtle()
                            enemy_list[enemy].hideturtle()
                            return enemy
                self.forward(check_distance)
                self.clear()
            return None


class Boost(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.shape("circle")
        self.penup()
        self.type = random.choice(["shield", "star", "heart"])
        if self.type == "shield":
            self.color("blue")
        elif self.type == "star":
            self.color("yellow")
        elif self.type == "heart":
            self.color("red")
        self.speed(0)
        self.goto(random.randint(-300, 300), random.randint(-200, 200))
        self.showturtle()

    def boost_collide(self, player):
        return abs(self.xcor() - player.xcor()) < 20 and abs(self.ycor() - player.ycor()) < 20


# Run the mainloop and create game object
def game(name):
    # Create player
    player = Player()
    player.penup()
    player.color("green")
    player.shape("turtle")
    player.speed(0)

    # screen setup
    screen = Screen()
    screen.bgcolor('burlywood1')
    screen.setup(1200, 800)

    # creating border
    border = Turtle(visible=False)
    border.speed(0)
    border.color('black')
    border.pensize(3)
    border.penup()
    border.setposition(-500, -300)
    border.pendown()
    for _ in range(2):
        border.forward(1000)
        border.left(90)
        border.forward(600)
        border.left(90)

    # Create enemies up to 4
    enemy1 = Enemy(enemy_life=1, enemy_score=25, size=random.randint(1, 4))
    enemy1.showturtle()
    enemy1.penup()

    enemy2 = Enemy(enemy_life=1, enemy_score=25, size=random.randint(1, 4))
    enemy2.showturtle()

    enemy3 = Enemy(enemy_life=1, enemy_score=25, size=random.randint(1, 4))
    enemy3.showturtle()

    enemy4 = Enemy(enemy_life=1, enemy_score=25, size=random.randint(1, 4))
    enemy4.showturtle()

    # Create buff object
    buffs = Boost()
    boost_list = [buffs]

    # Create enemy list
    enemy_list = [enemy1, enemy2, enemy3, enemy4]

    # Create UI
    player_score = 0
    score = Turtle(visible=False)
    score.penup()
    score.goto(450, 320)
    score.write(f"Score: {player.score}", align='center', font=('Arial', 20, 'normal'))
    player_life = 5
    life = Turtle(visible=False)
    life.penup()
    life.goto(-450, 340)
    life.write(f"Life: {player.life}", align='center', font=('Arial', 20, 'normal'))
    player_shield = 0
    shield = Turtle(visible=False)
    shield.penup()
    shield.goto(-450, 315)
    shield.write(f"Shield: {player.shield}", align='center', font=('Arial', 20, 'normal'))
    player_name = Turtle(visible=False)
    player_name.penup()
    player_name.goto(0, 320)
    player_name.write(f"{name}", align='center', font=('Arial', 30, 'normal'))


    def shoot():
        enemy = player.fire(enemy_list)
        if enemy is not None:
            player.score += enemy_list[enemy].enemy_score
            enemy_list[enemy] = None

    # Player key binding
    onkey(player.move_north, "w")
    onkey(player.move_south, "s")
    onkey(player.move_west, 'a')
    onkey(player.move_east, 'd')
    onkey(shoot, 'Return')
    screen.listen()

    # Main loop
    while True:
        if player.life <= 0:
            break
        for enemy in range(len(enemy_list)):
            if isinstance(enemy_list[enemy], Enemy):
                enemy_list[enemy].move(player)
                try:
                    if enemy_list[enemy].is_collide(player):
                        if player.shield == 1:
                            player.shield -= 1
                        elif player.shield == 0:
                            player.life -= 1
                        enemy_list[enemy].hideturtle()
                        enemy_list[enemy] = None

                except AttributeError:
                    pass
        for boost in range(len(boost_list)):
            if boost_list[boost].boost_collide(player):
                player.buff.append(boost_list[boost].type)
                player.get_buff()
                boost_list[boost].hideturtle()
                boost_list[boost] = Boost()
        if player_score != player.score:
            player_score = player.score
            score.clear()
            score.write(f"Score: {player.score}", align='center', font=('Arial', 20, 'normal'))
        if player_life != player.life:
            player_life = player.life
            life.clear()
            life.write(f"Life: {player.life}", align='center', font=('Arial', 20, 'normal'))
        if player_shield != player.shield:
            player_shield = player.shield
            shield.clear()
            shield.write(f"Shield: {player.shield}", align='center',
                         font=('Arial', 20, 'normal'))

        if all(enemy is None for enemy in enemy_list):
            for enemy in range(len(enemy_list)):
                enemy_list[enemy] = Enemy(enemy_life=1, enemy_score=25, size=random.randint(1, 4))
                enemy_list[enemy].showturtle()
        screen.update()

    print()
    print('GAME OVER!!!')
    exit()
    return player.score
