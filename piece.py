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

def valid_position(positions, x, y):
    #   if black piece, return true when piece is white or empty
    if x in range(8) and y in range(8):
        location = positions[x][y]
        #   when location is empty
        if location == 0:
            return "empty"
        elif location.black:
            return "black"
        else:
            return "white"
    else:
        #   not a proper location
        return "null"


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
        if self.black:
            if valid_position(positions, self.x, self.y - 1) == "empty":
                moves.append((self.x, self.y - 1))
                if self.y == 6:
                    if valid_position(positions, self.x, self.y - 2) == "empty":
                        moves.append((self.x, self.y - 2))
            if valid_position(positions, self.x - 1, self.y - 1) == "white":
                moves.append((self.x - 1, self.y - 1))
            if valid_position(positions, self.x + 1, self.y - 1) == "white":    
                moves.append((self.x + 1, self.y - 1))
        else:
            if valid_position(positions, self.x, self.y + 1) == "empty":
                moves.append((self.x, self.y + 1))
                if self.y == 1:
                    if valid_position(positions, self.x, self.y + 2) == "empty":
                        moves.append((self.x, self.y + 2))
            if valid_position(positions, self.x + 1, self.y + 1) == "black":
                moves.append((self.x - 1, self.y + 1))
            if valid_position(positions, self.x + 1, self.y + 1) == "black":    
                moves.append((self.x + 1, self.y + 1))
        return moves



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
        hit = False
        curr_y = self.y
        increment = 0
        moves = []
        while not hit:
            increment += 1
            valid = valid_position(positions, self.x,  curr_y + increment)
            location = (self.x, curr_y + increment)
            if valid == "empty":
                moves.append(location)
            elif valid == "white":
                if self.black:
                    moves.append(location)
                hit = True
            elif valid == "black":
                if not self.black:
                    moves.append(location)
                hit = True
            else:
                hit = True
        increment = 0
        hit = False
        while not hit:
            increment -= 1
            valid = valid_position(positions, self.x, curr_y + increment)
            location = (self.x, curr_y + increment)
            if valid == "empty":
                moves.append(location)
            elif valid == "white":
                if self.black:
                    moves.append(location)
                hit = True
            elif valid == "black":
                if not self.black:
                    moves.append(location)
                hit = True
            else:
                hit = True
        return moves

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