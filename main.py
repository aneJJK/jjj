from pygame import *

init()

window = display.set_mode((920, 750))
display.set_caption("Ping Pong")

bg = image.load("BG.png")
bg = transform.scale(image.load("BG.png"), (1920, 1080))


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x, player_y,player_speed,wight,height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Platform(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 5:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 5:
            self.rect.y += self.speed

platform_r = Platform("platform.png", 20,-10, 100, 100, 100)
platform_l = Platform("platform.png", 200,-10, 100, 100, 100)

exit = False

while not exit:
    for e in event.get():
        if e.type == QUIT:
            exit = True
    window.blit(bg,(0,0))
    platform_r.update_r()
    platform_r.reset()
    platform_l.update_l()
    platform_l.reset()
    display.update()
   

