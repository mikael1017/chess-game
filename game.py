import pygame
from board import Board
#############################################
#   Must have
pygame.init() # reset 
#   initialize the window
screen_width = 900 # x-axis
screen_height = 900 # y-axis
screen = pygame.display.set_mode((screen_width, screen_height))

#   Title 
pygame.display.set_caption("Chess game made by Jaewoo")

#   FPS
clock = pygame.time.Clock()

#############################################

# 1. Background, Game image, Character, Position of image, Font
#   Background
board = Board()


#   event loop
running = True 
while running:
    dt = clock.tick(60) #frame per second

    # 2. Event handling (keyboard, mouse, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # when user click the close button
            running = False

    # 3. Character location
    
    # 4. Collision handling
    
    # 5. Display it in window
    screen.blit(board.board_image, (50, 50)) 
    pygame.display.update()


pygame.quit()