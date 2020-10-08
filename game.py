import pygame
import os
from board import Bishop
from board import King
from board import Rook
from board import Pawn
from board import Queen
from board import Knight
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
space = 86
border = 110

def pos_to_pixel(pos):
    return (space * pos) + border 

def draw_board(board):
    for i in range(board.col):
        for j in range(board.row):
            position = board.positions[i][j]
            if (position != 0):
                screen.blit(board.positions[i][j].image, (pos_to_pixel(i), pos_to_pixel(j)))


#   event loop
running = True 
while running:
    dt = clock.tick(60) #frame per second

    # 2. Event handling (keyboard, mouse, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # when user click the close button
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # when user clicks a piece by left mouse button
            pos = pygame.mouse.get_pos()

            #   when piece is clicked by mouse
            for i in range(board.col):
                for j in range(board.row):
                    piece = board.positions[i][j]
                    if (piece != 0):
                        piece_rect = piece.image.get_rect()
                        piece_rect.left = pos_to_pixel(i)
                        piece_rect.top = pos_to_pixel(j)
                        if piece_rect.collidepoint(pos):
                            print(piece.get_move(board.positions))
                            print(piece.__class__.__name__)

    # 3. Character location
    
    # 4. Collision handling
    
    # 5. Display it in window
    screen.blit(board.board_image, (50, 50)) 
    draw_board(board)

    pygame.display.update()


pygame.quit()

