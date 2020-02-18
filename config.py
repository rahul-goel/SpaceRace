import pygame
pygame.init()


class config_settings:

    # game screen
    screen_size = (800, 700)
    screen = pygame.display.set_mode(screen_size)

    # game colours
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    WHITE = (255, 255, 255)
    back_image = pygame.image.load("./images/background.jpg")

    # messages to be displayed
    round_success = "ROUND PASSED. NEXT PLAYER."
    obstacle_hit = "YOU GOT HIT."
    game_over_text = "GAME OVER."
    win_1 = "Player 1 Won."
    win_2 = "Player 2 Won."
    tie = "It is a tie."

    # different font sizes for different type of texts
    font50 = pygame.font.Font("freesansbold.ttf", 50)
    font40 = pygame.font.Font("freesansbold.ttf", 40)
    font25 = pygame.font.Font("freesansbold.ttf", 25)
    font20 = pygame.font.Font("freesansbold.ttf", 20)


class game_object:
    # by default, speed is set to be 3
    def __init__(self, file_path, pos_x, pos_y, speed=3):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.change_x = 0
        self.change_y = 0
        self.speed = speed
        self.img = pygame.image.load(file_path)
        self.rect = self.img.get_rect()

    def render(self, screen):
        screen.blit(self.img, (self.pos_x, self.pos_y))
