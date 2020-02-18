import pygame
import random
import config
from config import config_settings as cs
pygame.init()


def random_enemy(new_speed):
    enemy_list = []
    for i in range(1, 6, 1):
        # using random function to get random direction of movement
        direction = 1 if bool(random.getrandbits(1)) else -1
        # randomly chosing within the available images
        enemy_list.append(config.game_object(
            f"./images/enemy{i}.png", random.randrange(0, 750),
            665 - i*120, direction*new_speed))
    return enemy_list


def random_obstacle():
    obstacles = []
    # i value is used to displace the obstacles vertically
    for i in range(4):
        # randomly alligning enemies in the 3 divisions
        # randomly chosing the images of obstacles
        obstacle1 = config.game_object(
            f"./images/obstacle{random.randint(1, 5)}.png",
            random.randrange(0, 250), 480 - i*120)
        obstacle2 = config.game_object(
            f"./images/obstacle{random.randint(1, 5)}.png",
            random.randrange(300, 500), 480 - i*120)
        obstacle3 = config.game_object(
            f"./images/obstacle{random.randint(1, 5)}.png",
            random.randrange(550, 750), 480 - i*120)
        obstacles.extend([obstacle1, obstacle2, obstacle3])

    return obstacles
