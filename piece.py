import pygame
import os

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

b_bishop = pygame.image.load(os.path.join(image_path, "b_bishop.png"))
b_king = pygame.image.load(os.path.join(image_path, "b_king.png"))
b_knight = pygame.image.load(os.path.join(image_path, "b_knight.png"))
b_pawn = pygame.image.load(os.path.join(image_path, "b_pawn.png"))
b_queen = pygame.image.load(os.path.join(image_path, "b_queen.png"))
b_rook = pygame.image.load(os.path.join(image_path, "b_rook.png"))

w_bishop = pygame.image.load(os.path.join(image_path, "w_bishop.png"))
w_king = pygame.image.load(os.path.join(image_path, "w_king.png"))
w_knight = pygame.image.load(os.path.join(image_path, "w_knight.png"))
w_pawn = pygame.image.load(os.path.join(image_path, "w_pawn.png"))
w_queen = pygame.image.load(os.path.join(image_path, "w_queen.png"))
w_rook = pygame.image.load(os.path.join(image_path, "w_rook.png"))

def valid_position(positions, x, y, black):
    #   if black piece, return true when piece is white or empty
    if x and y in range(8):
        location = positions[x][y]
        #   when location is empty
        if location == 0:
            return True
        elif black:
            if location.black:
                return False
            else:
                return True
        else:
            if location.black:
                return True
            else:
                return False
    else:
        return False


class Piece:
    def __init__(self, x, y, black, image):
        self.x = x
        self.y = y
        self.moves = []
        self.black = black
        self.image = image

    def get_move(self, positions):
        pass

class Pawn(Piece):
    def __init__(self, x, y, black):
        if black:
            self.image = b_pawn
        else:
            self.image = w_pawn
        super().__init__(x, y, black, self.image)
        
    def get_move(self, positions):
        moves = []
        possible = []
        if black:
            #   when pawn is located on default position
            possible_x = [self.x + 1, self.x - 1]
            possible_y = self.y - 1
            if self.y == 6:
                moves.append((self.x, self.y - 1))
                moves.append((self.x, self.y - 2))
            else:
                moves.append((self.x, self.y - 1))


class Bishop(Piece):
    def __init__(self, x, y, black):
        if black:
            self.image = b_bishop
        else:
            self.image = w_bishop
        super().__init__(x, y, black, self.image)
        
    def get_move(self, positions):
        pass


class Knight(Piece):
    def __init__(self, x, y, black):
        if black:
            self.image = b_knight
        else:
            self.image = w_knight
        super().__init__(x, y, black, self.image)
        
    def get_move(self, positions):
        pass

class Rook(Piece):
    def __init__(self, x, y, black):
        if black:
            self.image = b_rook
        else:
            self.image = w_rook
        super().__init__(x, y, black, self.image)
        
    def get_move(self, positions):
        pass

class Queen(Piece):
    def __init__(self, x, y, black):
        if black:
            self.image = b_queen
        else:
            self.image = w_queen
        super().__init__(x, y, black, self.image)
        
    def get_move(self, positions):
        pass

class King(Piece):
    def __init__(self, x, y, black):
        if black:
            self.image = b_king
        else:
            self.image = w_king
        super().__init__(x, y, black, self.image)
        
    def get_move(self, positions):
        pass