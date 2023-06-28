# Imports
import pygame as pg
import white_board as wt

# Have to started the font class before using it
pg.font.init()

# Constant global variables such fonts, colour
JURA_BOLD = "Jura-Bold.ttf"
QUESTION_FONT_SIZE = 28
QUESTION_NUM_COLOUR = (255, 107, 107)
QUESTION_COLOUR = (0,0,0)

# Class to make the questions and the options for the question
class QuestionMaker:

    # Putting the question surface on the board
    def question_on_screen(self):
        wt.display_board.surface.blit(self.question_surface, self.question_surface_pos)

    def __init__(self, question_num, question, question_num_colour = QUESTION_NUM_COLOUR, question_colour = QUESTION_COLOUR, question_font_type= JURA_BOLD, question_font_size = QUESTION_FONT_SIZE):
        # variables such height and width
        self.width_question_surface = 440
        self.height_question_surface = 110
        self.question_surface_colour = (247, 255, 247)
        self.question_font_type = question_font_type
        self.question_font_size = question_font_size
        self.question_num = question_num
        self.antialise_state = True
        self.question_num_colour = question_num_colour
        self.question = question
        self.question_colour = question_colour
        self.max_ques_num_line_size = 435
        self.max_question_line = 408

        # Creating surface for the question
        self.question_surface_x_pos = int(wt.display_board.surface.get_width()/1/4)
        self.question_surface_y_pos = int(wt.display_board.surface.get_height()/2)
        self.question_surface = pg.Surface((self.width_question_surface, self.height_question_surface))
        self.question_surface.fill('blue')
        self.question_surface_pos = self.question_surface.get_rect(center = (self.question_surface_x_pos, self.question_surface_y_pos))

        # Text style
        self.text_style = pg.font.Font(self.question_font_type, self.question_font_size)

        # Making the Question number font
        self.question_num_text_y_pos = 0
        self.question_num_text_x_pos = 0
        self.question_num_text = self.text_style.render(self.question_num, self.antialise_state, self.question_num_colour)

        # Making the Question fonts
        self.question_text_x_pos = int(self.question_num_text.get_width() + 10)
        self.question_text_y_pos = 0
        self.question_size = self.text_style.size(self.question)
        self.overall_question_size = self.question_size[0] + self.question_num_text.get_width() + 10 # Gets the question number and question size
        self.question_split_spaced = []
        self.question_in_line = []
        self.line_width = 0
        self.line_one_question = []
        self.line_two_question = []

        # Putting the fonts on the screen
        # self.question_surface.blit(self.question_num_text,  self.question_num_text_pos)
        # self.question_surface.blit(self.question_text, self.question_pos)


Q1 = QuestionMaker("Q1", "What is the formula")







