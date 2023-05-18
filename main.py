# Importing the pygame and sys.exit to be able to use pygame
import pygame as pg
import sys

# initialising the pygame or starting pygame
pg.init()

# General setup
WIDTH, HEIGHT = 1042, 697
window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Quiz Race")

# Icon
icon = pg.image.load("DGT WORK (3).png")
pg.display.set_icon(icon)

# Fps control
FPS = 60  # frame rate
clock = pg.time.Clock()  # clock that will count

# Colour
game_active_col = (78, 205, 196)

# Custom cursor
image_of_cursor = pg.image.load("cursor (1).png")
image_of_cursor_rotate = pg.transform.rotozoom(
    image_of_cursor, 30, 1)  # rotating the image
cursor = pg.cursors.Cursor((11, 12), image_of_cursor_rotate)

# Running or looping the game
while True:
    for events in pg.event.get():
        if events.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # Putting color on the screen
    window.fill(game_active_col)

    # putting a cursor on the screen
    pg.mouse.set_cursor(cursor)

    # updating the game at a framerate of 60
    pg.display.update()
    clock.tick(FPS)
