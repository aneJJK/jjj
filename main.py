from pygame import * 

font.init()

win_width = 700 
win_height = 500 

FPS = 60 

player_l_goals = 0
player_r_goals = 0

clock = time.Clock() 

exit = False 

bg = image.load("BG.png") 
bg = transform.scale(bg, (win_width, win_height)) 
player_image = ("platform.png")
window = display.set_mode((win_width, win_height)) 

display.set_caption("Ping_pong") 

lose_image = image.load("BG.png")

# Очистка экрана
window.fill((255, 255, 255))
    
# Отображение изображения на экране
window.blit(lose_image, (250, 250))
    
# Обновление экрана
display.update()

class GameSpite(sprite.Sprite): 
    def __init__(self, player_image, player_x, player_y, width, height): 
        super().__init__() 
        self.image = transform.scale(image.load(player_image), (width, height)) 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 
class Player(GameSpite): 
    def __init__(self, player_image, player_x, player_y, width, height, player_speed): 
        super().__init__(player_image, player_x, player_y, width, height)  
        self.speed = player_speed 
    def update_l(self): 
        keys = key.get_pressed() 
        if keys[K_w] and self.rect.y > 0: 
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 130: 
            self.rect.y += self.speed
    def update_r(self): 
        keys = key.get_pressed() 
        if keys[K_UP] and self.rect.y > 0: 
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 130: 
            self.rect.y += self.speed
class Ball(GameSpite): 
    def __init__(self, player_image, player_x, player_y, width, height, speed_x, speed_y): 
        super().__init__(player_image, player_x, player_y, width, height) 
        self.speed_x = speed_x 
        self.speed_y = speed_y 

    def update(self): 
        self.rect.x += self.speed_x 
        self.rect.y += self.speed_y 

player_l = Player('platform.png', 4, 100, 30, 130, 10) 
player_r = Player('platform.png', win_width - 35, 100, 30, 130, 10) 
ball = Ball("ball.png", 100, 100, 50, 50, 5, 5)

finish = False 
pause = True 
font = font.Font(None, 35) 
lose = ''

def ball_collide(): 
    if sprite.collide_rect(player_l, ball): 
        ball.speed_x *= -1 
        ball.speed_y += (ball.rect.centery - player_l.rect.centery) / 20 
    if sprite.collide_rect(player_r, ball): 
        ball.speed_x *= -1 
        ball.speed_y += (ball.rect.centery - player_r.rect.centery) / 20
    if ball.rect.y > win_height - 50 or ball.rect.y < 0: ball.speed_y *= -1 

while exit != True:
    for e in event.get():
        if e.type == QUIT:
            exit = True
        if e.type == KEYUP:
            if e.key == K_r and finish:
                ball.rect.x = 250
                ball.rect.y = 100
                ball.speed_x = 5
                ball.speed_y = 5
                finish = False
                pause = True
            if e.key == K_SPACE and not finish:
                pause = not pause

    keys = key.get_pressed()
    window.blit(bg, (0, 0))
    if not pause and not finish:
        if ball.rect.x < -50:
            lose = font.render('PLAYER 1 LOSE!', True, (255,255,255))
            press_r = font.render('Press r to restart', True,(255,255,255))
            finish = True
            player_r_goals +=1
        if ball.rect.x > win_width:
            lose = font.render('PLAYER 2 LOSE!', True, (255,255,255))
            press_r = font.render('Press r to restart', True, (255,255,255))
            finish = True
            player_l_goals +=1
        ball.update()
        player_l.update_l()
        player_r.update_r()
        ball_collide()
    if pause:
        window.blit(font.render('PING PONG', True, (255,255,255)), (285, 230))
        window.blit(font.render('Press SPACE to start.', True, (255,255,255)), (235, 260))
    if finish:
        window.blit(lose, (247, 230))
        window.blit(press_r, (250, 260))

    window.blit(font.render(f'SCORE_R: {player_l_goals}', True, (255, 255, 255)), (5, 10))
    window.blit(font.render(f'SCORE_L: {player_r_goals}', True, (255, 255, 255)), (win_width - 150, 10))

    player_r.reset()
    player_l.reset()
    ball.reset()
    display.update()
    clock.tick(FPS)

# while exit != True: 
#     for e in event.get(): 
#         if e.type == QUIT: 
#             exit = True 
#     keys = key.get_pressed() 
#     window.blit(bg, (0, 0)) 
#     if finish != True: 
#         if pause == False: 
#             ball_collide() 
#             if ball.rect.x < -50: 
#                 lose = font.render('PLAYER 1 LOSE!', True, (180, 0, 0)) 
#                 finish = True 
#                 player_r_goals +=1
#             if ball.rect.x > win_width: 
#                 lose = font.render('PLAYER 2 LOSE!', True, (180, 0, 0)) 
#                 finish = True 
#                 player_l_goals +=1
#             ball.update() 
#             player_l.update_l() 
#             player_r.update_r() 
#         else:
#             window.blit(font.render('Press SPACE to start.', True, (255, 255, 255)), (250, 250)) 
#             if  keys[K_SPACE]: 
#                 pause = False
#     else: 
#         window.blit(lose, (250, 250)) 

#         if keys[K_r]: 
#             ball.rect.x = 250 
#             ball.rect.y = 100 
#             ball.speed_x = 5 
#             ball.speed_y = 5 
#             finish = False 
#             pause = True 
#     player_r.reset() 
#     player_l.reset() 
#     ball.reset()
    window.blit(font.render(f'SCORE_R: {player_l_goals}', True, (255, 255, 255)), (5, 10))
    window.blit(font.render(f'SCORE_L: {player_r_goals}', True, (255, 255, 255)), (win_width - 150, 10))
#     display.update() 
#     clock.tick(FPS)