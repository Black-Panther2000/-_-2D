from pygame import *
from random import *

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('fon.jpg'), (win_width, win_height))

speed_x = 10
speed_y = 10

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
   def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5 :
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
        



class Enemy(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5 :
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed


class Ball(GameSprite):
    def update(self):
        ball.rect.x += speed_x
        ball.rect.y += speed_y



game = True

clock = time.Clock()
FPS = 60
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
                
    display.update()
    clock.tick(FPS)