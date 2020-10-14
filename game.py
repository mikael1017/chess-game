import pygame
import os
from board import Bishop
from board import King
from board import Rook
from board import Pawn
from board import Queen
from board import Knight
from board import Board
from piece import Piece
from collections import namedtuple
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

board = Board()
space = 86
border = 110
black_turn = True
mark_image = pygame.image.load(os.path.join(image_path, "mark.png"))
clicked_image_x = -1
clicked_image_y = -1
piece_to_move = 0
turn = 0
background = pygame.image.load(os.path.join(image_path, "background.png"))

def pos_to_pixel(pos):
    return (space * pos) + border 

def display_msg(message):
    msg = game_font.render(message, True, (255, 0, 0))
    msg_rect = msg.get_rect(center = (int(screen_width / 2), int(screen_height / 2)))
    screen.blit(msg, msg_rect)
    pygame.display.update()
    pygame.time.delay(3000)

def draw_board(board):
    for i in range(board.col):
        for j in range(board.row):
            position = board.positions[i][j]
            if (position != 0):
                screen.blit(board.positions[i][j].image, (pos_to_pixel(i), pos_to_pixel(j)))
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
        # print(move_location)
        move_location = []
    pygame.display.update()
    pygame.time.delay(1000)
#   event loop


def game_loop():
    board = Board()
    space = 86
    border = 110
    black_turn = True
    mark_image = pygame.image.load(os.path.join(image_path, "mark.png"))
    clicked_image_x = -1
    clicked_image_y = -1
    piece_to_move = 0
    turn = 0
    background = pygame.image.load(os.path.join(image_path, "background.png"))
    running = True 
    selected_piece = "None"
    king_caught = False


    while running:
        dt = clock.tick(60) #frame per second
        #   Event handling (keyboard, mouse, etc)
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
                        if (isinstance(piece_to_move, Piece) and isinstance(piece, Piece) and piece_to_move.black != piece.black):
                            piece_rect = piece.image.get_rect()
                            piece_rect.left = pos_to_pixel(i)
                            piece_rect.top = pos_to_pixel(j)
                            if piece_rect.collidepoint(pos):
                                if (i, j) in board.positions[clicked_image_x][clicked_image_y].get_move(board.positions):
                                    board.positions[i][j] = board.positions[clicked_image_x][clicked_image_y]
                                    board.positions[clicked_image_x][clicked_image_y] = 0
                                    board.positions[i][j].x = i
                                    board.positions[i][j].y = j
                                    piece_to_move = 0
                                    pygame.display.update()
                                    if isinstance(piece, King):
                                        king_caught = True
                                        running = False
                                        break
                                    black_turn = not black_turn
                                else:
                                    display_msg("Can't place a piece there")
                        elif (piece != 0):
                            piece_rect = piece.image.get_rect()
                            piece_rect.left = pos_to_pixel(i)
                            piece_rect.top = pos_to_pixel(j)
                            if piece_rect.collidepoint(pos):
                                if (piece.black != black_turn):
                                    display_msg("Other player's turn")
                                    break
                                clicked_image_x = i
                                clicked_image_y = j
                                pygame.draw.rect(screen, (225, 0, 0), piece_rect, width = 4)
                                pygame.display.update()
                                pygame.time.delay(500)
                                piece_to_move = piece
                                selected_piece = piece_to_move.__class__.__name__
                        #   when empty position is clicked it moves to the new location 
                        elif (isinstance(piece_to_move, Piece) and piece == 0):
                            piece_rect = pygame.Rect(piece_rect.left, piece_rect.top, 75, 75)
                            piece_rect.left = pos_to_pixel(i)
                            piece_rect.top = pos_to_pixel(j)
                            if piece_rect.collidepoint(pos):
                                if (i, j) in board.positions[clicked_image_x][clicked_image_y].get_move(board.positions):
                                    board.positions[i][j] = board.positions[clicked_image_x][clicked_image_y]
                                    board.positions[clicked_image_x][clicked_image_y] = 0
                                    board.positions[i][j].x = i
                                    board.positions[i][j].y = j
                                    piece_to_move = 0
                                    black_turn = not black_turn
                                else:
                                    display_msg("Can't place a piece there")
                    else:
                        continue
                    break
                else:
                    continue
                break
                        #   If moving chess piece is opposite color of the located chess piece
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
                                print(piece.get_move)
                                draw_moves(piece.get_move(board.positions))

        screen.blit(background, (0, 0))
        screen.blit(board.board_image, (50, 50))
        draw_board(board)
        score = game_font.render("Turn : {}".format(turn), True, (255, 255, 255))
        chosen = game_font.render("Selected piece : {}".format(selected_piece), True, (255, 255, 255))
        turn = "Black" if black_turn else "White"
        screen.blit(score, (0, 5))
        screen.blit(chosen, (450, 5))
        pygame.display.update()
        if king_caught:
            display_msg("Game Over! {} won!".format(turn))

game_loop()
pygame.quit()

