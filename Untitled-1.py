from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        if keys_pressed[K_UP]:
            self.rect.x -= 10
        if keys_pressed[K_DOWN]:
            self.rect += 10
        if keys_pressed[K_w]:
            self.rect -= 10
        if keys_pressed[K_s]:
            self.rect += 10
window = display.set_mode((700,500))
display.set_caption('пинг-конг')        
background = transform.scale(image.load("blackground.png"),(700,500))

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    keys_pressed = key.get_pressed()
    window.blit(background,(0,0))