import pygame
import time
import pathlib
path = str(pathlib.Path(__file__).parent.resolve())

#variables
dots = 9
c_pos = []

#CONSTANTS 
WIDTH, HEIGHT = 650,650
X_SPACE = WIDTH/4
Y_SPACE = HEIGHT/4

WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
RED = (255,0,0)

#position of circles
x = X_SPACE
y = Y_SPACE
num = 0
for i in range(dots):
    c_pos.append((int(x), int(y)))
    x += X_SPACE
    num += 1
    if num == 3:
        y +=Y_SPACE
        x = X_SPACE
        num = 0

# use [:] to pick just some of elements from list - for instance: data = data[0:1624]
with open(path+ "\\combinations.txt", "r") as f:
    data = f.read().splitlines()

#data = data[380000:389112]  



#init
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("comicsans", 50)
text = font.render("Press s to start", 1, WHITE)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Patterns")


#func definition
def draw(var):
    starting_dot = int(var[0])
    screen.fill(BLACK)
    for x, y in c_pos:
        pygame.draw.circle(screen, WHITE, (x, y), 5)

    pygame.draw.circle(screen, RED, (c_pos[starting_dot][0], c_pos[starting_dot][1]), 5)

    for i in range(len(var)-1):
        a = int(var[i])
        b = int(var[i+1])
        pygame.draw.line(screen, YELLOW, c_pos[a], c_pos[b], 2)
        
        pygame.display.update()
        time.sleep(.15)

def main():
    run = True
    start = False
    index = 0
    

    screen.blit(text, text.get_rect(center = screen.get_rect().center))
    #screen.blit(text, (WIDTH//2-text.get_width()//2, HEIGHT//2-text.get_height()//2))
    pygame.display.update()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    start = True
        if start:
            try:
                draw(data[index])
            except:
                screen.fill(BLACK)
                pygame.display.update()
                time.sleep(10)
                run = False

            index +=1
            #print(index)

main()
pygame.quit()

