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
        self.col = 8
        self.row = 8
        self.positions = [[0 for x in range(8)] for y in range(8)]
        
        self.positions[0][7] = Rook(0, 7, True)
        self.positions[1][7] = Knight(1, 7 , True)
        self.positions[2][7] = Bishop(2, 7, True)
        self.positions[3][7] = Queen(3, 7, True)
        self.positions[4][7] = King(4, 7, True)
        self.positions[5][7] = Bishop(5, 7, True)
        self.positions[6][7] = Knight(6, 7, True)
        self.positions[7][7] = Rook(7, 7, True)
        
        # for i in range(8):
        #     self.positions[i][6] = Pawn(i, 6, True)
        
        self.positions[0][0] = Rook(0, 0, False)
        self.positions[1][0] = Knight(1, 0, False)
        self.positions[2][0] = Bishop(2, 0, False)
        self.positions[3][0] = Queen(3, 0, False)
        self.positions[4][0] = King(4, 0, False)
        self.positions[5][0] = Bishop(5, 0, False)
        self.positions[6][0] = Knight(6, 0, False)
        self.positions[7][0] = Rook(7, 0, False)
        
        for i in range(8):
            self.positions[i][1] = Pawn(i, 1, False)


# image size
# 785 x 785
# border
# 55 pixels
# each space
# 80 x 80
