# Imports
import pygame as pg

# starting pygame
pg.init()

# Constant varibales/ colours and sizes of the box
box_size = (510, 70)
pinks_box_colour = (235, 62, 62)
blue_box_colour = (20, 153, 228)
yellow_box_colour = (255, 215, 15)
green_box_colour = (39, 239, 83)
boxes_colour = [pinks_box_colour, blue_box_colour, yellow_box_colour, green_box_colour]

# Puts the answers in boxes
class AnswerCreator:

    def __init__(self, box_size = box_size, colours = boxes_colour):

        # setting the sizes of the box
        self.box_A = pg.surface.Surface(box_size)
        self.box_B = pg.surface.Surface(box_size)
        self.box_C = pg.surface.Surface(box_size)
        self.box_D = pg.surface.Surface(box_size)

        # colours of the box
        self.box_A.fill(colours[0])
        self.box_B.fill(colours[1])
        self.box_C.fill(colours[2])
        self.box_D.fill(colours[3])



