import pygame
import config
from config import config_settings as cs
pygame.init()


def background():
    cs.screen.blit(cs.back_image, (0, 0))


def you_got_hit():
    game_over_text_display = cs.font50.render(cs.obstacle_hit, True, cs.WHITE)
    cs.screen.blit(game_over_text_display, (220, 290))
    pygame.display.update()
    pygame.time.delay(1000)


def round_passed():
    game_over_text_display = cs.font40.render(
        cs.round_success, True, cs.WHITE)
    cs.screen.blit(game_over_text_display, (70, 290))
    pygame.display.update()
    pygame.time.delay(1000)


def bottom_display(
        total_score1, total_score2, round, which_player,
        curr_time, start_time1, start_time2):
    # score 1
    score1_disp = cs.font25.render(
        "Score 1: " + str(total_score1), True, cs.WHITE)
    cs.screen.blit(score1_disp, (10, 660))
    # score 2
    score2_disp = cs.font25.render(
        "Score 2: " + str(total_score2), True, cs.WHITE)
    cs.screen.blit(score2_disp, (180, 660))
    # round value
    round1_display = cs.font25.render("Round: " + str(round), True, cs.WHITE)
    cs.screen.blit(round1_display, (500, 660))
    # time
    if which_player:
        time_display = cs.font25.render(
            "Time: " + str(int(curr_time - start_time1)), True, cs.WHITE)
        cs.screen.blit(time_display, (620, 660))
    else:
        time_display = cs.font25.render(
            "Time: " + str(int(curr_time - start_time2)), True, cs.WHITE)
        cs.screen.blit(time_display, (620, 660))


def game_over(score1, score2):
    game_over_text_display = cs.font50.render(
        cs.game_over_text, True, cs.WHITE)
    cs.screen.blit(game_over_text_display, (240, 290))
    if score1 > score2:
        disp = cs.font20.render(cs.win_1, True, cs.WHITE)
        cs.screen.blit(disp, (330, 350))
    elif score1 < score2:
        disp = cs.font20.render(cs.win_2, True, cs.WHITE)
        cs.screen.blit(disp, (330, 350))
    else:
        disp = cs.font20.render(cs.tie, True, cs.WHITE)
        cs.screen.blit(disp, (330, 350))
    score1_disp = cs.font20.render("Score 1: " + str(score1), True, cs.WHITE)
    cs.screen.blit(score1_disp, (260, 400))
    score2_disp = cs.font20.render("Score 2: " + str(score2), True, cs.WHITE)
    cs.screen.blit(score2_disp, (410, 400))

    pygame.display.update()
    pygame.time.delay(2000)
