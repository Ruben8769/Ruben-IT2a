import pygame
import random

pygame.init()
clock = pygame.time.Clock()
fps = 1

# Colors
cell_border_cl = (20,20,20, .5)
cells_cl = (240,240,240)
worm_cl = (78, 210, 149)
apple_cl = (206, 24, 24)

# Cell size, amount
CELL_SIZE = 30
CELL_NUMBER = 16
WIDTH = CELL_SIZE * CELL_NUMBER
HEIGHT = CELL_SIZE * CELL_NUMBER

screen = pygame.display.set_mode((WIDTH, HEIGHT))

worm = [7 * CELL_SIZE, 7 * CELL_SIZE, CELL_SIZE, CELL_SIZE]
dir = "right"

def draw_snake():
    pygame.draw.rect(screen, (worm_cl), worm)
    if dir == "right":
        worm[0] += 1 * CELL_SIZE
    elif dir == "left":
        worm[0] -= 1 * CELL_SIZE
    elif dir == "up":
        worm[1] -= 1 * CELL_SIZE
    elif dir == "down":
        worm[1] += 1 * CELL_SIZE

apple = [random.randint(0,CELL_NUMBER-1) * CELL_SIZE, random.randint(0,CELL_NUMBER-1) * CELL_SIZE, CELL_SIZE, CELL_SIZE]
apple1 = [random.randint(0,CELL_NUMBER-1) * CELL_SIZE, random.randint(0,CELL_NUMBER-1) * CELL_SIZE, CELL_SIZE, CELL_SIZE]
apple2 = [random.randint(0,CELL_NUMBER-1) * CELL_SIZE, random.randint(0,CELL_NUMBER-1) * CELL_SIZE, CELL_SIZE, CELL_SIZE]
apple3 = [random.randint(0,CELL_NUMBER-1) * CELL_SIZE, random.randint(0,CELL_NUMBER-1) * CELL_SIZE, CELL_SIZE, CELL_SIZE]

def draw_apple():
    pygame.draw.rect(screen, (apple_cl), apple)

def draw_apple1():
    pygame.draw.rect(screen, (apple_cl), apple1)
    
def draw_apple2():
    pygame.draw.rect(screen, (apple_cl), apple2)
    
def draw_apple3():
    pygame.draw.rect(screen, (apple_cl), apple3)

def collide():
    if worm[0] == apple[0] and worm[1] == apple[1]:
        apple[0] = random.randint(0,CELL_NUMBER-1) * CELL_SIZE
        apple[1] = random.randint(0,CELL_NUMBER-1) * CELL_SIZE
        
def collide1():
    if worm[0] == apple1[0] and worm[1] == apple1[1]:
        apple1[0] = random.randint(0,CELL_NUMBER-1) * CELL_SIZE
        apple1[1] = random.randint(0,CELL_NUMBER-1) * CELL_SIZE
        
def collide2():
    if worm[0] == apple2[0] and worm[1] == apple2[1]:
        apple2[0] = random.randint(0,CELL_NUMBER-1) * CELL_SIZE
        apple2[1] = random.randint(0,CELL_NUMBER-1) * CELL_SIZE
        
def collide3():
    if worm[0] == apple3[0] and worm[1] == apple3[1]:
        apple3[0] = random.randint(0,CELL_NUMBER-1) * CELL_SIZE
        apple3[1] = random.randint(0,CELL_NUMBER-1) * CELL_SIZE

def draw_cells():
    for cell_position in range(CELL_NUMBER):
        pygame.draw.line(screen, cell_border_cl, (cell_position * CELL_SIZE, 0), (cell_position * CELL_SIZE, HEIGHT))
    for cell_position in range(CELL_NUMBER):
        pygame.draw.line(screen, cell_border_cl, (0, cell_position * CELL_SIZE), (WIDTH, cell_position * CELL_SIZE))

def update_screen():
    screen.fill(cells_cl)
    draw_cells()
    draw_snake()
    draw_apple()
    draw_apple1()
    draw_apple2()
    draw_apple3()
    collide()
    collide1()
    collide2()
    collide3()
    pygame.display.update()

# Main loop
main = True
while main:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                main = False
            if event.key == pygame.K_d:
                dir = "right"
            if event.key == pygame.K_a:
                dir = "left"
            if event.key == pygame.K_w:
                dir = "up"
            if event.key == pygame.K_s:
                dir = "down"
            if event.key == pygame.K_e:
                fps -= 1
            if event.key == pygame.K_q:
                fps += 1
    update_screen()