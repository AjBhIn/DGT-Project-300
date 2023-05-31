# Imports
import pygame as pg

# Have to started the font class before using it
pg.font.init()

# Constant variables
Q_num_colour = (255, 107, 107)
Q_colour = (0,0,0)
white_board_colour = (247, 255, 247)
Q_num_margin_x = 10
Question_margin_x = 8
jura_bold = "Jura-Bold.ttf"
question_size = 28

# Text container or where the text will be info
container_size = (400, 100)
text_container = pg.surface.Surface(container_size)
text_container.fill(white_board_colour)
text_container_pos = text_container.get_rect(center = (260,542))

# Text Generator
class Typer:

    def __init__(self, textitself, text_color, pos_text, font_family = jura_bold, font_size = question_size):
        # Font related info
        self.textitself = textitself
        self.text_color = text_color
        self.font_size = font_size
        self.font_family = font_family
        self.pos = pos_text
        self.antialias = True

        # Style of the text
        self.text_style = pg.font.Font(self.font_family, self.font_size)
        self.text_size = self.text_style.size(self.textitself)

        # Making the Text and it pos
        self.making_text = self.text_style.render(self.textitself, self.antialias, self.text_color)
        self.text_pos = self.making_text.get_rect(midleft = self.pos) # Taking control of the text box from it mid_left point
        
        #putting the text on the mini screen
        text_container.blit(self.making_text, self.text_pos)


Q1_num = Typer("Q1", Q_num_colour, (Q_num_margin_x, 50))
Q1_question = Typer("What is Complex Numbe", Q_colour, (48, 50))


