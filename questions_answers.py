# Imports
import pygame as pg
import white_board as wt

# Have to started the font class before using it
pg.font.init()

# Constant global variables such fonts, colour
JURA_BOLD = "Jura-Bold.ttf"
QUESTION_FONT_SIZE = 40
QUESTION_NUM_COLOUR = (255, 107, 107)
QUESTION_COLOUR = (0,0,0)

# Class to make the questions and the options for the question
class QuestionMaker:

    # Puts the container onto the white board
    def font_container_render(self):
         wt.display_board.surface.blit(self.font_container, self.font_container_placement)

    def __init__(self, quesstion_num, question, JURA_BOLD = JURA_BOLD, QUESTION_FONT_SIZE = QUESTION_FONT_SIZE, 
                 QUESTION_NUM_COLOUR = QUESTION_NUM_COLOUR, QUESTION_COLOUR = QUESTION_COLOUR):
        
        # Settingup the style for the question font
            # Question font family
        self.JURA_BOLD = JURA_BOLD
            # Question font size for question and question number
        self.font_size = QUESTION_FONT_SIZE
            # Style of the font
        self.question_font_style = pg.font.Font(self.JURA_BOLD, self.font_size)
        self.antialias = True


        # Question number and question char sizes
        self.question_num_char_size = self.question_font_style.size(quesstion_num)
        self.question_char_size = self.question_font_style.size(question)


        # Font Container
            # Font Container dimensions
        self.font_container_W = int(40 + self.question_num_char_size[0] + self.question_char_size[0])
        self.font_container_H = 110
            # Font container placement
        self.font_container_x = int(wt.display_board.surface.get_width()/4)
        self.font_container_y = int(wt.display_board.surface.get_height()/2)
            # Blueprints of the font container
        self.font_container = pg.Surface((self.font_container_W , self.font_container_H))
        self.font_container_placement = self.font_container.get_rect(center = (self.font_container_x, self.font_container_y))
        self.font_container.fill((247, 255, 247))


        # Question number font
            # Question number placement
        self.question_num_x = 10
        self.question_num_y = int(self.font_container.get_height() / 2)
            # Question number colour
        self.question_num_colour = QUESTION_NUM_COLOUR
            # Question number blueprints
        self.question_num = self.question_font_style.render(quesstion_num, self.antialias, self.question_num_colour)
        self.question_num_placement = self.question_num.get_rect(midleft = (self.question_num_x, self.question_num_y))


        # Question font
            # Question placement
        self.question_x = self.question_num_char_size[0] + 30
        self.question_y = int(self.font_container.get_height() / 2)
            # Question colour
        self.question_colour = QUESTION_COLOUR
            # Question blueprints
        self.question = self.question_font_style.render(question, self.antialias, self.question_colour)
        self.question_placement = self.question.get_rect(midleft = (self.question_x, self.question_y))


        # Putting the question and question numner in the font container
        self.font_container.blit(self.question_num, self.question_num_placement)
        self.font_container.blit(self.question, self.question_placement)


Q1 = QuestionMaker("Q1", "2 + 2 =")







