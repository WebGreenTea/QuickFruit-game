import pgzrun
import random
import time
import pygame
import random

WIDTH = 640
HEIGHT = 480
apple = Actor('apple')
orange = Actor('orange')
pineapple = Actor('pineapple')
startB = Actor('startb',center=(WIDTH//2,HEIGHT//2))
tryB = Actor('try',center=(WIDTH/4,(HEIGHT/4)*3))
exB = Actor('exit',center=((WIDTH/4)*3,(HEIGHT/4)*3))
mainB = Actor('main',center=(WIDTH/2,(HEIGHT/6)*5))
Bback = Actor('back',center=(WIDTH-(WIDTH-50),HEIGHT-25))
sett = Actor('setting',center=(WIDTH-50,HEIGHT-25))
p1080 = Actor('1080p',center=(WIDTH/4,HEIGHT/3))
p720 = Actor('720p',center=((WIDTH/4)*3,HEIGHT/3))
p16 = Actor('1600p',center=(WIDTH/4,(HEIGHT/3)*2))
p640 = Actor('640p',center=((WIDTH/4)*3,(HEIGHT/3)*2))
start_time = float(0)
now_time = 0
time_O = 0
gamescreen = 0
end_time = 0
fullsc = 0
tryG = 0
ranspeed = 5
def draw():
    global gamescreen
    if gamescreen == 1:
        play_screen()
    elif gamescreen == 2:
        end_game()
        #os.system("pause")
    elif gamescreen == 0:
        start_gameSC()
    elif gamescreen == 4:
        setting_sc()

def on_mouse_down(pos):
    global gamescreen,WIDTH,HEIGHT,fullsc,start_time,tryG
    if gamescreen == 1:
        if apple.collidepoint(pos):
            print("Good Chot!(Apple)")
            apple_bom()
            #place_apple()
        elif orange.collidepoint(pos):
            print("Good Chot!(Orange)")
            orange_bom()
            #place_orange()
        elif pineapple.collidepoint(pos):
            print("Good Chot!(Pineapple)")
            pineapple_bom()
            #place_pineapple()
        else:
            print("You Missed")
    if gamescreen == 0:
        if startB.collidepoint(pos):
            print("START!!")
            start_gameAC()
        if sett.collidepoint(pos):
            gamescreen = 4
    if gamescreen == 2:
        if tryB.collidepoint(pos):
            gamescreen = 1
            tryG += 1
            start_time = time.time()
            '''exec(open("main.py").read())
            quit()'''
        if exB.collidepoint(pos):
            quit()
        if mainB.collidepoint(pos):
            gamescreen = 0  
    if gamescreen == 4:
        if Bback.collidepoint(pos):
            gamescreen = 0
        if p1080.collidepoint(pos):
            if fullsc == 1:
                fullsc = 10
            WIDTH = 1920
            HEIGHT = 1080
            place_B()      
        if p720.collidepoint(pos):
            if fullsc == 1:
                fullsc = 10
            WIDTH = 1280
            HEIGHT = 720
            place_B()
        if p16.collidepoint(pos):
            if fullsc == 1:
                fullsc = 10
            WIDTH = 1600
            HEIGHT = 900
            place_B()
        if p640.collidepoint(pos):
            if fullsc == 1:
                fullsc = 10
            WIDTH = 640
            HEIGHT = 480 
            place_B()
def apple_bom():
    apple.image = 'bom'
    sounds.dbl.play()
    clock.schedule_unique(place_apple, 0.1)
def orange_bom():
    orange.image = 'bom'
    sounds.dbl.play()
    clock.schedule_unique(place_orange,0.1)
def pineapple_bom():
    pineapple.image = 'bom'
    sounds.dbl.play()
    clock.schedule_unique(place_pineapple,0.1)
            
def on_key_down(key):
    global fullsc
    if key == keys.F:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        fullsc = 1
    elif key == keys.W:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        fullsc = 0

def update():
    global gamescreen,fullsc
    if gamescreen == 1  :
        play_ac()
    if fullsc > 1:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        fullsc -= 1

def place_apple():
    apple.image = 'apple'
    apple.x = random.randint(40,WIDTH-40)
    apple.y = -60
def place_orange():
    orange.image = 'orange'
    orange.x = random.randint(40,WIDTH-40)
    orange.y = -60
def place_pineapple():
    pineapple.image = 'pineapple'
    pineapple.x = random.randint(40,WIDTH-40)
    pineapple.y = -60
def place_B():
    p1080.pos = WIDTH/4,HEIGHT/3
    p720.pos = (WIDTH/4)*3,HEIGHT/3
    p16.pos = WIDTH/4,(HEIGHT/3)*2
    p640.pos = (WIDTH/4)*3,(HEIGHT/3)*2
    Bback.pos = WIDTH-(WIDTH-50),HEIGHT-25
    tryB.pos = WIDTH/4,(HEIGHT/4)*3
    exB.pos = (WIDTH/4)*3,(HEIGHT/4)*3
    startB.pos = WIDTH/2,HEIGHT/2
    sett.pos = WIDTH-50,HEIGHT-25
    mainB.pos = WIDTH/2,(HEIGHT/6)*5
def update_time():
    global time_O
    now_time = time.time()
    time_O = now_time-start_time

def end_game():
    screen.clear()
    screen.draw.text("Your Time : "+str(end_time),center=(WIDTH/2,HEIGHT/4),fontsize=30)
    tryB.draw()
    exB.draw()
    mainB.draw()

def start_gameSC():
    screen.clear()
    screen.fill((0, 0, 0))
    startB.draw()
    sett.draw()
def start_gameAC():
    global gamescreen,start_time
    gamescreen += 1
    start_time = time.time()

def play_screen():
    global gamescreen,end_time
    screen.clear()
    screen.fill((174, 255, 182))
    apple.draw()
    orange.draw()
    pineapple.draw()
    screen.draw.text(str(time_O),topleft=(10,10),fontsize=30,color="black")
    end_time = time_O 
def setting_sc():
    global gamescreen
    screen.clear()
    screen.fill((0, 0, 0))
    p1080.draw()
    p720.draw()
    p16.draw()
    p640.draw()
    Bback.draw()

def play_ac():
    global time_O,gamescreen,ranspeed
    if int(time_O) % 6 == 0:
        ranspeed = random.randrange(2,8)
        print('random speed')
        print(ranspeed)
    if time_O <= 5:
        apple.y += 1
        orange.y += 1
        pineapple.y += 1
    elif (ranspeed%3) == 0:
        apple.y += 5
        orange.y += 5
        pineapple.y += 5
    elif (ranspeed%2) == 0:
        apple.y += 4
        orange.y += 4
        pineapple.y += 4
    elif (ranspeed%7) == 0:
        apple.y += 7
        orange.y += 7
        pineapple.y += 7
    elif time_O >= 30:
        apple.y += 8
        orange.y += 8
        pineapple.y += 8
    else:
        apple.y += 3
        orange.y += 3
        pineapple.y += 3
    if apple.y > HEIGHT:
        place_apple()
        place_orange()
        place_pineapple()
        gamescreen = 2
        #quit()
    
    if orange.y > HEIGHT :
        place_apple()
        place_orange()
        place_pineapple()
        gamescreen = 2
        #quit()
    
    if pineapple.y > HEIGHT:
        place_apple()
        place_orange()
        place_pineapple()
        gamescreen = 2
        #quit()
    update_time()
place_apple()
place_orange()
place_pineapple()
start_time = time.time()
pgzrun.go()