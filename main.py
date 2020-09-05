import pygame
from pygame import mixer

pygame.init()
clock = pygame.time.Clock()
pygame.font.init()

width = 1000
height = 800

vel_y = 5

score_time = None

vel_mouv_x = 8
vel_mouv_y = 8
vel_joueur = 6

pygame.display.set_caption("Le Pong")
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 25)

x1 = 40
y1 = 300
x2 = 920
y2 = 300
x_depart = 500
y_depart = 400

score_value_g = 0
score_value_d = 0


ping_sound = mixer.Sound('assets/ping.wav')
pong_sound = mixer.Sound('assets/pong.wav')

blanc = (255,255,255)

class Balle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.vel_x = vel_mouv_x
        self.vel_y = vel_mouv_y
        self.vel_joueur = vel_joueur
        self.image = pygame.image.load('assets/circle.png')
        self.rect = self.image.get_rect()
        self.rect.x = x_depart
        self.rect.y = y_depart

    def move(self):
        if self.rect.x >= 0:
            self.rect.x += self.vel_x
        if self.rect.x >= width - 32 - self.vel_x:
            self.vel_x *= -1
        if self.rect.x <= 0:
            self.vel_x *= -1

        if self.rect.y >= 0:
            self.rect.y += self.vel_y
        if self.rect.y >= height - 32 -self.vel_y:
            self.vel_y *= -1
        if self.rect.y <= 0:
            self.vel_y *= -1


    def score(self):
        self.rect.x = x_depart
        self.rect.y = y_depart

rect1 = pygame.Rect(x1, y1, 40,150)
rect2 = pygame.Rect(x2, y2, 40, 150)
font_score = pygame.font.Font('assets/font_Gamer.ttf', 25)

balle = Balle()

def screen_msg(msg, color, x, y):
    screen_text = font_score.render(msg, True, color)
    screen.blit(screen_text, (x, y))

def score_g(color, x, y):
    score = font_score.render(str(score_value_g), True, color)
    screen.blit(score, (x,y))

def score_d(color, x, y):
    score = font_score.render(str(score_value_d), True, color)
    screen.blit(score, (x,y))

current_time = pygame.time.get_ticks()

run = True
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    keys = pygame.key.get_pressed()
    screen.fill(( 30, 30, 30))

    if keys[pygame.K_UP] and rect1.y > 0:
        rect1.y -= vel_joueur
    if keys[pygame.K_DOWN] and rect1.y < height - rect1.height:
        rect1.y += vel_joueur
    
    if keys[pygame.K_s] and rect2.y > 0:
        rect2.y -= vel_joueur
    if keys[pygame.K_x] and rect2.y < height - rect2.height:
        rect2.y += vel_joueur

    if balle.rect.colliderect(rect1):
        ping_sound.play()
        balle.vel_x *= -1
    if balle.rect.colliderect(rect2):
        pong_sound.play()
        balle.vel_x *= -1

    if balle.rect.x <= 0:
        balle.score()
        score_value_d += 1
    if balle.rect.x >= width - 32 - vel_mouv_x:
        balle.score()
        score_value_g += 1


    pygame.draw.line(screen,(255,255,255), (500,0), (500,800), 3)
    screen.blit(balle.image, balle.rect)
    screen_msg("Player 1", (255,255,255), 200, 100)
    screen_msg("Player 2", (255,255,255), 700, 100)
    score_g(blanc, 230, 150)
    score_d(blanc, 730, 150)
    balle.move()
    pygame.draw.rect(screen, (255, 255, 255), rect1, 0)
    pygame.draw.rect(screen, (255, 255, 255), rect2, 0)
    pygame.display.flip()
    clock.tick(60)
