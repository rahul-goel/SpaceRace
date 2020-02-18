import pygame
import random
import math
import mechanics
import config
import texts
import obstacle_enemy
from time import time
from config import config_settings as cs

# initialise the pygame module
random.seed(time())
pygame.init()

clock = pygame.time.Clock()
start_time1 = time()
start_time2 = 0

# title and icon and music
pygame.display.set_caption("SPACE RACE")
music = "./sounds/music.mp3"
pygame.mixer.music.load(music)
pygame.mixer.music.play()

# score and rounds
time1 = time2 = 0
total_score1 = total_score2 = 0
score1 = score2 = 0
round = 1
which_player = True
# true means player 1 and false means player 2 above

# objects in the game, and the speed control
new_speed = 2
player1 = config.game_object("./images/player1.png", 370, 660 - 50)
player2 = config.game_object("./images/player2.png", 370, 0)
enemies = obstacle_enemy.random_enemy(new_speed)
obstacles = obstacle_enemy.random_obstacle()

# game loop
# running is a list so that it is passed by reference
running = [True]
while running[0]:
    # fill the screen with black colour and put the background
    cs.screen.fill(cs.BLACK)
    texts.background()

    # key in put for each player individually
    if which_player:
        mechanics.key_check1(running, player1)
    else:
        mechanics.key_check2(running, player2)

    # move the enemies around
    for enemy in enemies:
        mechanics.move_enemy(enemy)

    # checking collisions between player and enemy/obstacle
    collision_occurence_1 = mechanics.check_collision(
        player1, enemies, obstacles)
    collision_occurence_2 = mechanics.check_collision(
        player2, enemies, obstacles)

    # when the player1 dies or completes
    if which_player is True and (collision_occurence_1 or player1.pos_y <= 23):
        # change the player, no change in round, curr_score = 0
        which_player = not which_player
        round += 0
        score1 = 0
        end_time1 = time()

        # it has reached the opposite side then
        if player1.pos_y <= 23:
            total_score1 += max(0, 10 - int(end_time1 - start_time1)) * 5

        mechanics.crash_player1(player2)

        if collision_occurence_1:
            texts.you_got_hit()
        elif player1.pos_y <= 23:
            texts.round_passed()

        start_time2 = time()
        obstacles = obstacle_enemy.random_obstacle()
        enemies = obstacle_enemy.random_enemy(new_speed)

    # when the player2 dies or completes
    if (which_player is False and
            (collision_occurence_2 or player2.pos_y >= 578)):
        # change the player, round++, curr_score = 0
        which_player = not which_player
        round += 1
        new_speed += 5
        score2 = 0
        end_time2 = time()

        # it has reached the opposite side then
        if player2.pos_y >= 578:
            total_score2 += max(0, 10 - int(end_time2 - start_time2)) * 5

        mechanics.crash_player2(player1)

        if collision_occurence_2:
            texts.you_got_hit()
        elif player2.pos_y >= 578:
            texts.round_passed()

        start_time1 = time()
        obstacles = obstacle_enemy.random_obstacle()
        enemies = obstacle_enemy.random_enemy(new_speed)

    if which_player:
        player1.render(cs.screen)
    else:
        player2.render(cs.screen)

    for enemy in enemies:
        enemy.render(cs.screen)
    for obstacle in obstacles:
        obstacle.render(cs.screen)

    # player1 case -
    if which_player:
        prev = score1
        score1 = 0
        for enemy in enemies:
            if player1.pos_y < enemy.pos_y:
                score1 += 10
        for obstacle in obstacles:
            if player1.pos_y < obstacle.pos_y:
                score1 += 5
        if prev is not score1:
            total_score1 = total_score1 - prev + score1
    # player 2 case -
    else:
        prev = score2
        score2 = 0
        for enemy in enemies:
            if player2.pos_y > enemy.pos_y:
                score2 += 10
        for obstacle in obstacles:
            if player2.pos_y > obstacle.pos_y:
                score2 += 5
        if prev is not score2:
            total_score2 = total_score2 - prev + score2

    texts.bottom_display(total_score1, total_score2, round,
                         which_player, time(), start_time1, start_time2)

    if round > 3:
        texts.background()
        texts.game_over(total_score1, total_score2)
        running[0] = False

    pygame.display.update()
    clock.tick(60)
