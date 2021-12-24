from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,image_x,image_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(image_x,image_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= 10
        if keys_pressed[K_DOWN] and self.rect.y < 250:
            self.rect.y += 10
class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= 10 
        if keys_pressed[K_s] and self.rect.y < 250:
            self.rect.y += 10
class mych(GameSprite):
    def update(self): 
        
            
        pass         
chel1 = Player1("chel1.png",50,100,10,160,250)
chel2 = Player2("chel2.png",500,100,10,160,250)
wind_mych = mych("windows_ball.png",350,200,10,70,70)
font.init()
font = font.Font(None,70)
ottt = font.render("",True,(255,215,0))
window = display.set_mode((700,500))
display.set_caption('пинг-конг')        
background = transform.scale(image.load("blackground.png"),(700,500))
clock = time.Clock()
fps = 60
game = True
st = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        if stm == True:
            ball.rect.x += speed_x
            ball.rect.y += speed_y
    if ball.rect
    keys_pressed = key.get_pressed()
    if keys_pressed[K_SPACE] and st == False:
        st = True
        ottt = font.render("3",True,(255,215,0))
        window.blit(ottt,(250,100))
        display.update()
        time.delay(1000)
        window.blit(background,(0,0))
        ottt = font.render("2",True,(255,215,0))
        window.blit(ottt,(250,100))
        display.update()
        time.delay(1000)
        window.blit(background,(0,0))
        ottt = font.render("1",True,(255,215,0))
        window.blit(ottt,(250,100))
        display.update()
        time.delay(1000)
        window.blit(background,(0,0))
        ottt = font.render("start!",True,(255,215,0))
        window.blit(ottt,(250,100))
        display.update()
        stm = True
        time.delay(1000)
        window.blit(background,(0,0))
    wind_mych.update()
    chel1.update()
    chel2.update()
    wind_mych.reset()
    chel1.reset()
    chel2.reset()
    display.update()
    clock.tick(fps)
    window.blit(background,(0,0))