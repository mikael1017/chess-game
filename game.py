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
current_path = os.path.dirname (__file__)
image_path = os.path.join(current_path, "images")
game_font = pygame.font.Font(None, 40)
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
black_turn = True
mark_image = pygame.image.load(os.path.join(image_path, "mark.png"))

def pos_to_pixel(pos):
    return (space * pos) + border 

def display_msg(message):
    msg = game_font.render(message, True, (255, 0, 0))
    msg_rect = msg.get_rect(center = (int(screen_width / 2), int(screen_height / 2)))
    screen.blit(msg, msg_rect)
    pygame.display.update()
    pygame.time.delay(1500)

def draw_board(board):
    for i in range(board.col):
        for j in range(board.row):
            position = board.positions[i][j]
            if (position != 0):
                screen.blit(board.positions[i][j].image, (pos_to_pixel(i), pos_to_pixel(j)))
    pygame.display.update()

#   if piece doesn't have any possible move, it displays "No available move" on the screen
#   otherwise, it display possible move of selected piece for 1.5 seconds
def draw_moves(moves):
    if len(moves) == 0:
        display_msg("No possible move")
        return
    move_location = []
    for move in moves:
        move_location.append(pos_to_pixel(move[0]))
        move_location.append(pos_to_pixel(move[1]))
        screen.blit(mark_image, (move_location[0], move_location[1]))
        print(move_location)
        move_location = []
    pygame.display.update()
    pygame.time.delay(1500)

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
            #   if chess piece is clicked on other player's turn, it will print out other's turn
            for i in range(board.col):
                for j in range(board.row):
                    piece = board.positions[i][j]
                    if (piece != 0):
                        piece_rect = piece.image.get_rect()
                        piece_rect.left = pos_to_pixel(i)
                        piece_rect.top = pos_to_pixel(j)
                        if piece_rect.collidepoint(pos):
                            if (piece.black != black_turn):
                                display_msg("Other player's turn")
                            else:
                                piece_to_move = piece
                                
                            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3: # when user clicks a piece by right mouse button
            pos = pygame.mouse.get_pos()
            for i in range(board.col):
                for j in range(board.row):
                    piece = board.positions[i][j]
                    if (piece != 0):
                        piece_rect = piece.image.get_rect()
                        piece_rect.left = pos_to_pixel(i)
                        piece_rect.top = pos_to_pixel(j)
                        if piece_rect.collidepoint(pos):
                            if (piece.black != black_turn):
                                display_msg("Other player's turn")
                                break
                            draw_moves(piece.get_move(board.positions))

    # 3. Character location
    
    # 4. Collision handling
    
    # 5. Display it in window
    screen.blit(board.board_image, (50, 50)) 
    draw_board(board)


pygame.quit()

