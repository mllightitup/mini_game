import pygame
import time

pygame.init()
win = pygame.display.set_mode((800, 450))

pygame.display.set_caption("GAME")

walk_right = [
    pygame.image.load('adventurer-run3-00.png'),
    pygame.image.load('adventurer-run3-01.png'),
    pygame.image.load('adventurer-run3-02.png'),
    pygame.image.load('adventurer-run3-03.png'),
    pygame.image.load('adventurer-run3-04.png'),
    pygame.image.load('adventurer-run3-05.png'),
    ]
    
walk_left = [
    pygame.image.load('left0.png'),
    pygame.image.load('left1.png'),
    pygame.image.load('left2.png'),
    pygame.image.load('left3.png'),
    pygame.image.load('left4.png'),
    pygame.image.load('left5.png'),
    ]
    
bow_shoot = [
    pygame.image.load('adventurer-bow-00.png'),
    pygame.image.load('adventurer-bow-01.png'),
    pygame.image.load('adventurer-bow-02.png'),
    pygame.image.load('adventurer-bow-03.png'),
    pygame.image.load('adventurer-bow-04.png'),
    pygame.image.load('adventurer-bow-05.png'),
    pygame.image.load('adventurer-bow-06.png'),
    pygame.image.load('adventurer-bow-07.png'),
    pygame.image.load('adventurer-bow-08.png'),
    ]

bg = pygame.image.load('background.png')
player_stand = pygame.image.load('adventurer-idle-00.png')
player_stand_left = pygame.image.load('idle_left.png')
player_arrow = pygame.image.load('arrow_1.png')
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Some Text', False, (0, 0, 0))
clock = pygame.time.Clock()

x = 50
y = 390
width = 50 
height = 37
speed = 2

is_shooting = False
is_jump = False
jump_count = 30

left = False
right = False
anim_count = 0
last_move = 'right'
class snaryad():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
    def draw(self, win):
        win.blit(player_arrow, (self.x, self.y))

def draw_window():
    global anim_count
    global last_move
    win.blit(bg, (0, 0))
    if anim_count + 1 >= 30:
        anim_count = 0
    # if is_shooting:
        # win.blit(bow_shoot[anim_count // 9], (x, y))
        # anim_count += 1
    if left:
        win.blit(walk_left[anim_count // 5], (x, y))
        anim_count += 1
    elif right:
        win.blit(walk_right[anim_count // 5], (x, y))
        anim_count += 1
    elif last_move == 'left':
        win.blit(player_stand_left, (x, y))
    else:
        win.blit(player_stand, (x, y))
        
    for bullet in bullets:
        bullet.draw(win)
        
    pygame.display.update()

run = True
bullets = []
while run:
    clock.tick(240)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 800 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_q]:
        screen.blit(win, textsurface,(0,0))
        pygame.quit()
    if keys[pygame.K_f]:
        time.sleep(0.01)
        is_shooting = True
        if last_move == "right":
            facing = 1
        else:
            facing = -1
        if len(bullets) < 1:
            bullets.append(snaryad(round(x + width // 2), round(y + height // 2), 5, (255,0,0), facing))
            
    if keys[pygame.K_LEFT] and x > 1:
        x -= speed
        left = True
        right = False
        last_move = 'left'
    elif keys[pygame.K_RIGHT] and x < 800 - width - 1:
        x += speed
        left = False
        right = True
        last_move = 'right'
    else:
        left = False
        right = False
        anim_count = 0
    if not(is_jump):
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -30:
            if jump_count < 0:
                y += (jump_count ** 2) / 150
            else:
                y -= (jump_count ** 2) / 150
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 30

    draw_window()
    
pygame.quit()