import pygame
from vars_const import SCREEN_WIDTH, SCREEN_HEIGHT,touching_floor

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))   
pygame.display.set_caption("A Crazy Run Through The Desert")

bg_layers = [
    pygame.image.load(r"assets/parallax/parallax_desert/a1.png").convert_alpha(),
    pygame.image.load(r"assets/parallax/parallax_desert/a2.png").convert_alpha(),
    pygame.image.load(r"assets/parallax/parallax_desert/a3.png").convert_alpha(),
    pygame.image.load(r"assets/parallax/parallax_desert/a4.png").convert_alpha(),
    pygame.image.load(r"assets/parallax/parallax_desert/a5.png").convert_alpha()
]
bg_layers = [pygame.transform.scale(layer, (SCREEN_WIDTH, SCREEN_HEIGHT)) for layer in bg_layers]
def draw_parallax():
    for layer in bg_layers:
        screen.blit(layer, (0, 0))
    
clock = pygame.time.Clock()
#COWBOY INFO - - - - - - - - - - - -  - - - - - - - - - - - - - -
cowboy_x = 50
cowboy_y = SCREEN_HEIGHT - 30
cowboy_width = 50
cowboy_height = 50
cowboy_speed_y = 0
ground = True
cowboy_Rect = pygame.Rect(cowboy_x,cowboy_y,cowboy_width,cowboy_height)





running = True
while (running):
    draw_parallax()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and ground:
        cowboy_speed_y = -20
        ground = False
    cowboy_Rect.y += cowboy_speed_y
    cowboy_speed_y += 1
    pygame.draw.rect(screen,(230,49,0),cowboy_Rect)
        
    if cowboy_Rect.bottom >= SCREEN_HEIGHT - 30:
        cowboy_Rect.bottom = SCREEN_HEIGHT - 30
        cowboy_speed_y = 0
        ground = True
        
    clock.tick(100)
    pygame.display.update()
pygame.quit()