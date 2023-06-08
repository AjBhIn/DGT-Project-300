# Imports
import pygame as pg
import sys
import race_track as rt
import white_board as wt
import questions as qs
import answers as an


# initialising the pygame or starting pygame
pg.init()

# General setup
WIDTH, HEIGHT = 1042, 697
window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Quiz Race")

# Icon
ICON = pg.image.load("icon (2).png")
pg.display.set_icon(ICON)

# Fps control
FPS = 60  # frame rate
clock = pg.time.Clock()  # clock that will count

# Colours
GAME_ACTIVE_BCOLOUR = (78, 205, 196)

# Custom cursor
image_of_cursor = pg.image.load("cursor (1).png") # image of the cursor
image_of_cursor_rotate = pg.transform.rotozoom(
    image_of_cursor, 30, 1)  # rotating the image
cursor = pg.cursors.Cursor((11, 12), image_of_cursor_rotate) # putting the image in cursor widget

# Running or looping the game
while True:
    for events in pg.event.get():
        if events.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # Putting color on the screen
    window.fill(GAME_ACTIVE_BCOLOUR)
    
    # Putting the tracks on the screen
    for each_lane in rt.tracks:
        for each_step in each_lane:
            window.blit(each_step[0], each_step[1])
    window.blit(rt.starting_lane.line_surface, rt.starting_lane.pos)
    window.blit(rt.finishing_lane.line_surface, rt.finishing_lane.pos)
    
    # Putting the white board on the screen
    window.blit(wt.main_board.surface, (0, 347))
    wt.main_board.surface.blit(wt.display_board.surface, (0, 40))
    wt.display_board.surface.blit(rt.divider_lane.line_surface, rt.divider_lane.pos)

    # Putting the container of the question on the White Board
    wt.display_board.surface.blit(qs.text_container, qs.text_container_pos)

    # Putting the answers boxes on the display board
    an.anwers.text_creator()

    # putting a cursor on the screen
    pg.mouse.set_cursor(cursor)

    # updating the game at a framerate of 60
    pg.display.update()
    clock.tick(FPS)
