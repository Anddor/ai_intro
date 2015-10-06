from PIL import Image, ImageDraw, ImageFont
import os


class Board_img_gen(object):

    """docstring for Board_img_gen"""

    def __init__(self, world_width, world_height, square_size=50):
        super(Board_img_gen, self).__init__()
        self.square_size = square_size
        self.img = self.make_img(world_width, world_height, square_size)
        self.draw = ImageDraw.Draw(self.img)

    # make a blank image for the text, initialized to transparent text color

    def make_img(self, world_width, world_height, square_size):
        img_height = world_height * square_size
        img_width = world_width * square_size
        img = Image.new('RGBA', (img_width, img_height), (255, 255, 255, 0))
        return img

    def draw_world(self, world):
        x = 0
        y = 0
        for row in world:
            for square in row:
                # print(square, x, y)
                pos_x = x * self.square_size
                pos_y = y * self.square_size
                self.draw_square(square, pos_x, pos_y)
                x += 1
            y += 1
            x = 0

    def draw_square(self, square, x, y):
        # Dictanary over colors
        colors = {
            "w": (76, 77, 255, 0),
            "m": (166, 166, 166, 0),
            "f": (31, 127, 0, 0),
            "g": (127, 255, 127, 0),
            "r": (191, 128, 64, 0),
            "#": (100, 100, 100, 0),
            ".": (255, 255, 255, 0),
            "A": (249, 15, 1, 0),
            "B": (72, 255, 0, 0)
        }
        # Draws a reqtangle representing a square in the
        # game on the right location at the image
        recangle = [(x, y), (x + self.square_size, y + self.square_size)]
        self.draw.rectangle(recangle, colors[square], (0, 0, 0, 0))

    def draw_path(self, path):
        # Draws a dot for each square in the path
        color = (0, 0, 0, 0)
        # Size represents the size of the dot
        size = self.square_size // 5
        for square in path:
            x, y = square.state
            # calculates the center position on the image for each square
            pos_x = (x * self.square_size + self.square_size//2)
            pos_y = (y * self.square_size + self.square_size//2)
            # Corinates for the bondingboks
            bounding_box = [
                (pos_x-size/2, pos_y-size/2), (pos_x + size/2, pos_y + size/2)]
            self.draw.ellipse(bounding_box, color)

    def draw_open_closed(self, squares, char):
        color = (0, 0, 0, 0)
        font = ImageFont.truetype("saxmono.ttf", 25)
        size = 25/2
        for square in squares:
            y, x = square
            pos_x = (x * self.square_size + self.square_size//2)
            pos_y = (y * self.square_size + self.square_size//2)
            pos = (pos_x-(size//2), pos_y-size)
            self.draw.text(pos, char, color, font=font)

    def show_img(self):
        self.img.show()

    def save(self, board_file_name, alg):
        file_path = os.getcwd()
        self.img.save(file_path + "/Boards_with_solution/" + board_file_name + alg + ".BMP", "BMP") 
