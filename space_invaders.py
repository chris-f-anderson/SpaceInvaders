# Ctrl + Shift + P, then select interpreter
# Choose an interpreter that works
import pygame

pygame.init()
clock = pygame.time.Clock()
game_display = pygame.display.set_mode((400, 600))
score_font = pygame.font.SysFont('Arial', 22, True)
title_font = pygame.font.SysFont('Arial', 26, True)
pygame.display.set_caption('SPACE INVADERS!')


x_coordinate = 50
y_coordinate = 100

def handle_events():
    global x_coordinate, y_coordinate
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_coordinate = x_coordinate - 10
            elif event.key == pygame.K_RIGHT:
                y_coordinate = y_coordinate + 10

      # Main game loop
    is_playing = True
    while is_playing:

        handle_events()

        game_display.blit(game_display, (0, 0))
        
        game_display.fill((0, 0, 0))
        pygame.draw.rect(game_display, (0 , 255, 0), pygame.Rect(x_coordinate, y_coordinate, 20, 20))
        # score_text = score_font.render(str(snake.score), False, (255, 255, 255))
        # game_display.blit(score_text, (0,0))

        pygame.display.update()

        clock.tick(30)
pygame.quit()
