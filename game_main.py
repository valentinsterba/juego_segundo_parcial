import pygame
from vars_const import WIDTH, HEIGHT

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))   
pygame.display.set_caption("RUN THROUGH THE DESERT")

bg_images = []

for i in range(1,10):
    bg_image = pygame.image.load(f"assets\parallax\parallax_desert\layer{i}.png").convert_alpha()
    bg_images.append(bg_image)
    
for i in bg_images:
    screen.blit(i,(0,0))

running = True
while (running):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            pass
        
        pygame.display.update()

pygame.quit()