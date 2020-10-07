import pygame
import os
from piece import Bishop
from piece import King
from piece import Rook
from piece import Pawn
from piece import Queen
from piece import Knight

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

class Board:
    def __init__(self):
        self.board_image = pygame.image.load(os.path.join(image_path, "board.png"))
        self.board_size = self.board_image.get_rect().size
        self.height = self.board_size[1]
        self.width = self.board_size[0]
        self.border = 50
        self.cell = 80
        self.positions = [[0 for x in range(8)] for y in range(8)]
        
        self.positions[7][0] = Rook(7, 0, "black")
        self.positions[7][1] = Knight(7, 1, "black")
        self.positions[7][2] = Bishop(7, 2, "black")
        self.positions[7][3] = Queen(7, 3, "black")
        self.positions[7][4] = King(7, 4, "black")
        self.positions[7][5] = Bishop(7, 5, "black")
        self.positions[7][6] = Knight(7, 6, "black")
        self.positions[7][7] = Rook(7, 7, "black")
        
        for i in range(8):
            self.positions[6][i] = Pawn(6, i, "black")
        
        self.positions[0][0] = Rook(0, 0, "white")
        self.positions[0][1] = Knight(0, 1, "white")
        self.positions[0][2] = Bishop(0, 2, "white")
        self.positions[0][3] = Queen(0, 3, "white")
        self.positions[0][4] = King(0, 4, "white")
        self.positions[0][5] = Bishop(0, 5, "white")
        self.positions[0][6] = Knight(0, 6, "white")
        self.positions[0][0] = Rook(0, 0, "white")
        
        for i in range(8):
            self.positions[1][i] = Pawn(1, i, "white")


# image size
# 785 x 785
# border
# 55 pixels
# each space
# 80 x 80
