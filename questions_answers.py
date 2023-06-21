# Imports
import pygame as pg

# Have to started the font class before using it
pg.font.init()

# Constant variables
white_board_colour = (247, 255, 247)

# Text container or where the text will be info
container_size = (400, 100)
text_container = pg.surface.Surface(container_size)
text_container.fill(white_board_colour)
text_container_pos = text_container.get_rect(center = (260,155))



