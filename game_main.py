import pygame
from vars_const import SCREEN_WIDTH, SCREEN_HEIGHT,touching_floor, BLACK

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

def draw_text(text, font, color, surface, x, y):
    '''Dibuja la superficie en la que el score se va a ubicar
       Se le centra y da estilo con Font y color'''
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect) 

def update_score(start_time):
    ''' Calcular el tiempo transcurrido
        Y controlar el limite de velocidad de aumento del score dividiendo // 100'''
    elapsed_time = pygame.time.get_ticks() - start_time  
    score = elapsed_time // 100  
    return score
clock = pygame.time.Clock()

invisible_floor = SCREEN_HEIGHT - 30
font = pygame.font.Font(None, 50)
#COWBOY INFO - - - - - - - - - - - -  - - - - - - - - - - - - - -
cowboy_x = 50
cowboy_y = invisible_floor
cowboy_width = 50
cowboy_height = 50
cowboy_speed_y = 0
ground = True
cowboy_Rect = pygame.Rect(cowboy_x,cowboy_y,cowboy_width,cowboy_height)

# OBSTACLE INFO
obstacle_width = 50
obstacle_height = 100
obstacle_x = SCREEN_WIDTH
obstacle_y = invisible_floor - obstacle_height
obstacle_speed = -10

obstacle_Rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)





start_time = pygame.time.get_ticks()
running = True
while (running):
    draw_parallax()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    
    score = update_score(start_time)
    draw_text(f"Score: {score}", font, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
    if keys[pygame.K_SPACE] and ground:
        cowboy_speed_y = -20
        ground = False
    cowboy_Rect.y += cowboy_speed_y
    cowboy_speed_y += 1
    pygame.draw.rect(screen,(230,49,0),cowboy_Rect)

    pygame.draw.rect(screen, (0, 0, 255), obstacle_Rect)
    obstacle_Rect.x += obstacle_speed

    if obstacle_Rect.x < 0 - obstacle_width:
        obstacle_Rect.x = obstacle_x
        
    if cowboy_Rect.bottom >= invisible_floor:
        cowboy_Rect.bottom = invisible_floor
        cowboy_speed_y = 0
        ground = True
    
    if cowboy_Rect.colliderect(obstacle_Rect):
        print("Colisión")
        running = False
    
    clock.tick(100)
    pygame.display.update()
pygame.quit()