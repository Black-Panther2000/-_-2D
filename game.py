from pygame import *
from random import *

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('fon.jpg'), (win_width, win_height))

speed_x = 3
speed_y = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, plaeyr_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (plaeyr_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed







font.init()
font = font.SysFont("Arial", 50)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
player = Player("player.png", 10, 200, 25, 150, 150)
enemy  = Player("enemy.png", 525, 200, 25, 200, 150)
ball = GameSprite("ball.png", 350, 250, 15, 45, 25)

game = True

clock = time.Clock()
FPS = 90
finish = False
mixer.init()
mixer.music.load('sound.ogg')
mixer.music.play()

 


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0, 0))
        player.update_l()
        enemy.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(player, ball) or sprite.collide_rect(enemy, ball):
           speed_x *= -1
           speed_y *= 1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
           speed_y *= -1

        if ball.rect.x < 0:
           finish = True
           window.blit(lose1, (200, 200))
           game_over = True


        if ball.rect.x > win_width:
           finish = True
           window.blit(lose2, (200, 200))
           game_over = True   


        player.reset()
        enemy.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)