import pygame
import config
from config import config_settings as cs
pygame.init()


def key_check1(running, player):
    for event in pygame.event.get():
        # exiting the game
        if event.type == pygame.QUIT:
            running[0] = False

        # taking in keystrokes
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT and
                    player.pos_x + player.change_x > 0):
                player.change_x -= player.speed
            elif (event.key == pygame.K_RIGHT and
                  player.pos_x + player.change_x < cs.screen_size[0]-50):
                player.change_x += player.speed
            elif (event.key == pygame.K_UP and
                  player.pos_y + player.change_y > 0):
                player.change_y -= player.speed
            elif (event.key == pygame.K_DOWN and
                  player.pos_y + player.change_y < cs.screen_size[1]-90):
                player.change_y += player.speed
            else:
                pass

        # upon lifting no change should take place
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.change_x = 0
            elif event.key == pygame.K_RIGHT:
                player.change_x = 0
            elif event.key == pygame.K_UP:
                player.change_y = 0
            elif event.key == pygame.K_DOWN:
                player.change_y = 0
            else:
                pass

        # apply the changes which have been recorded for this event
        player.pos_x += player.change_x
        player.pos_y += player.change_y

        # should not go out of window for this event
        player.pos_x = min(player.pos_x, cs.screen_size[0]-50)
        player.pos_x = max(player.pos_x, 0)
        player.pos_y = min(player.pos_y, cs.screen_size[1]-90)
        player.pos_x = max(player.pos_x, 0)

    # apply the changes recorded till now
    player.pos_x += player.change_x
    player.pos_y += player.change_y

    # should not go out of the window
    player.pos_x = min(player.pos_x, cs.screen_size[0]-50)
    player.pos_x = max(player.pos_x, 0)
    player.pos_y = min(player.pos_y, cs.screen_size[1]-50)
    player.pos_x = max(player.pos_x, 0)


def key_check2(running, player):
    for event in pygame.event.get():
        # exiting the game
        if event.type == pygame.QUIT:
            running[0] = False

        # taking in keystrokes
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_a and
                    player.pos_x + player.change_x > 0):
                player.change_x -= player.speed
            elif (event.key == pygame.K_d and
                    player.pos_x + player.change_x < cs.screen_size[0]-50):
                player.change_x += player.speed
            elif (event.key == pygame.K_w and
                    player.pos_y + player.change_y > 0):
                player.change_y -= player.speed
            elif (event.key == pygame.K_s and
                    player.pos_y + player.change_y < cs.screen_size[1]-90):
                player.change_y += player.speed
            else:
                pass

        # upon lifting no change should take place
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.change_x = 0
            elif event.key == pygame.K_d:
                player.change_x = 0
            elif event.key == pygame.K_w:
                player.change_y = 0
            elif event.key == pygame.K_s:
                player.change_y = 0
            else:
                pass

        # apply the changes which have been recorded for this event
        player.pos_x += player.change_x
        player.pos_y += player.change_y

        # should not go out of window for this event
        player.pos_x = min(player.pos_x, cs.screen_size[0]-50)
        player.pos_x = max(player.pos_x, 0)
        player.pos_y = min(player.pos_y, cs.screen_size[1]-90)
        player.pos_x = max(player.pos_x, 0)

    # apply the changes recorded till now
    player.pos_x += player.change_x
    player.pos_y += player.change_y

    # should not go out of the window
    player.pos_x = min(player.pos_x, cs.screen_size[0]-50)
    player.pos_x = max(player.pos_x, 0)
    player.pos_y = min(player.pos_y, cs.screen_size[1]-50)
    player.pos_x = max(player.pos_x, 0)


def move_enemy(enemy):
    # increase the coordinate. if touches boundary, reverse
    enemy.pos_x += enemy.speed
    if enemy.pos_x > cs.screen_size[0]-50 or enemy.pos_x < 0:
        enemy.speed *= -1


def is_collision(player, obstacle):
    value = False
    # 'if' condition checks the overlapping of boxes
    if (player.pos_x + 47 > obstacle.pos_x and
            player.pos_x < obstacle.pos_x + 47 and
            player.pos_y + 47 > obstacle.pos_y and
            player.pos_y < obstacle.pos_y + 47):
        value = True
    return value


def check_collision(player, enemies, obstacles):
    # iterate through all enemies and obstacles and check collisions
    bool_value = False
    for enemy in enemies:
        bool_value = bool_value or is_collision(
            player, enemy)
    for obstacle in obstacles:
        bool_value = bool_value or is_collision(
            player, obstacle)
    return bool_value


def crash_player1(player2):
    # player 1 crashed, player 2 spawns
    # function is called irrespective of collision or completion
    player2.pos_x = 370
    player2.pos_y = 0
    player2.change_x = 0
    player2.change_y = 0
    pygame.event.clear()


def crash_player2(player1):
    # player 2 crashed, player 1 spawns
    # function is called irrespective of collision or completion
    player1.pos_x = 370
    player1.pos_y = 660 - 50
    player1.change_x = 0
    player1.change_y = 0
    pygame.event.clear()
