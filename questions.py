# Imports
import pygame as pg

# Have to started the font class before using it
pg.font.init()

# Questions list
type_questions = [['Q1', "What is Complex Numbe"]]

# Constant variables
white_board_colour = (247, 255, 247)

# Text container or where the text will be info
container_size = (400, 100)
text_container = pg.surface.Surface(container_size)
text_container.fill(white_board_colour)
text_container_pos = text_container.get_rect(center = (260,155))

# Text Generator
class Typer:

    def question_maker(self, question_num, question_itself):
        # text sizer finder
        Q_num_size = self.text_style.size(question_num)
        Q_size = self.text_style.size(question_itself)

        # generatering the question and question number
        making_Q_num = self.text_style.render(question_num, self.antialias, self.Q_num_colour)
        making_Question = self.text_style.render(question_itself, self.antialias, self.Q_colour)

        # Taking control of the text box from it mid_left point // setting the position of the text box
        Q_num_pos = making_Q_num.get_rect(midleft = (self.Q_num_margin_x, self.text_y_pos))
        Q_pos = making_Question.get_rect(midleft = ((self.Q_margin_x + Q_num_size[0] + self.Q_num_margin_x), self.text_y_pos))

        #putting the text on the mini screen
        text_container.blit(making_Q_num, Q_num_pos)
        text_container.blit(making_Question, Q_pos)


    def __init__(self, question_list):
        self.font_family = "Jura-Bold.ttf"
        self.font_size = 28
        self.antialias = True
        self.Q_num_colour = (255, 107, 107)
        self.Q_colour = (0,0,0)
        self.Q_num_margin_x = 10
        self.Q_margin_x = 8
        self.text_y_pos = 50 # this is in reference to text container

        # Style of the text
        self.text_style = pg.font.Font(self.font_family, self.font_size)

        # retvering the questions from the list
        for each_question in question_list:
            self.question_num = each_question[0]
            self.question = each_question[1]
            self.question_maker(self.question_num, self.question)

# passing the questions into the class // instance of the class
questions = Typer(type_questions)


