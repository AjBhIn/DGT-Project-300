# Imports
import pygame as pg
import white_board as wt

# starting pygame
pg.init()

# answers list
answer_list = [["4", "2", "None", "Do Not Know"]]

# Constant varibales/ colours and sizes of the box
box_size = (510, 70)
box_position_display_board = (526, 5)
pinks_box_colour = (235, 62, 62)
blue_box_colour = (20, 153, 228)
yellow_box_colour = (255, 215, 15)
green_box_colour = (39, 239, 83)
boxes_colour = [pinks_box_colour, blue_box_colour, yellow_box_colour, green_box_colour]
# font style
jura_medium = "Jura-Medium.ttf"
text_size = 28
text_colour = (255, 255, 255)

# Puts the answers in boxes
class AnswerCreator:

    def text_creator(self):
        # putting the box A on the display board and it componments
        wt.display_board.surface.blit(self.box_A, self.box_position)


    def __init__(self, answers, box_size = box_size, colours = boxes_colour, font_style_for_answers = jura_medium, answer_size = text_size, text_colour = text_colour, box_positon_in_display_board = box_position_display_board):

        # setting the sizes of the box
        self.box_A = pg.surface.Surface(box_size)
        self.box_B = pg.surface.Surface(box_size)
        self.box_C = pg.surface.Surface(box_size)
        self.box_D = pg.surface.Surface(box_size)

        # position of the text and box
        self.box_position = box_positon_in_display_board
        self.name_answer_pos = (28, 35)
        self.answer_pos = (210, 35)
        
        # colours of the box
        self.box_A.fill(colours[0])
        self.box_B.fill(colours[1])
        self.box_C.fill(colours[2])
        self.box_D.fill(colours[3])

        # Answers/ text
        self.text_style = pg.font.Font(font_style_for_answers, answer_size)
        self.antialias = True

        #Creating the text
        self.box_A_text = self.text_style.render(answers[0][0], self.antialias, text_colour)
        self.box_A_text_pos = self.box_A_text.get_rect(center = self.answer_pos)

        self.box_B_text = self.text_style.render(answers[0][1], self.antialias, text_colour)
        self.box_B_text_pos = self.box_B_text.get_rect(midlcentereft = self.answer_pos)

        self.box_C_text = self.text_style.render(answers[0][2], self.antialias, text_colour)
        self.box_C_text_pos = self.box_C_text.get_rect(center = self.answer_pos)

        self.box_D_text = self.text_style.render(answers[0][3], self.antialias, text_colour)
        self.box_D_text_pos = self.box_D_text.get_rect(center = self.answer_pos)

        # Putting the Text on the Screen
        self.box_A.blit(self.box_A_text, self.box_A_text_pos)
        self.box_B.blit(self.box_A_text, self.box_A_text_pos)
        self.box_C.blit(self.box_A_text, self.box_A_text_pos)
        self.box_D.blit(self.box_A_text, self.box_A_text_pos)

anwers = AnswerCreator(answer_list)



