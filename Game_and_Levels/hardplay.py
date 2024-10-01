import pygame
from Game_assets.button import load_buttons
import math
class HardPlay:
    def __init__(self, display, gamestatemanager):
        self.display = display
        self.gamestatemanager = gamestatemanager
        self.background_image = pygame.image.load('Game Images/Updated Background.png')
        self.phase_shift = 0
        pygame.font.init()

        self.text_font = pygame.font.Font("Fonts/SuperSalad-qZgvV.ttf", 70)
        self.button_font = pygame.font.Font("Fonts/SuperSalad-qZgvV.ttf", 40)

    def run(self):
        self.display.blit(self.background_image, (0, 0))

        title = self.text_font.render("NUMERICAL INTUITION", True, (225, 225, 225))
        self.display.blit(title, (190, 50))

        self.blackplay_button, self.blacklevel_button, self.back_button = load_buttons("blackplay", 'blacklevel', 'back')

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.blackplay_button.is_clicked(pos):
                    self.gamestatemanager.set_state('hardgame')
                elif self.back_button.is_clicked(pos):
                    self.gamestatemanager.set_state('start')
                elif self.blacklevel_button.is_clicked(pos):
                    self.gamestatemanager.set_state('level')

        self.blackplay_button.draw(self.display)
        self.blacklevel_button.draw(self.display)
        self.back_button.draw(self.display)

        pygame.display.update()

        def draw_text_sine(text, font, text_col, x, y):
            amplitude = 10
            frequency = 0.01
            vertical_pos = amplitude * math.sin(frequency * x + self.phase_shift)
            img = font.render(text, True, text_col)
            self.display.blit(img, (x, y + vertical_pos))

            self.phase_shift += 0.1

        draw_text_sine("PLAY", self.button_font, (100, 100, 100), 180, 445)
        draw_text_sine("LEVEL", self.button_font, (100, 100, 100), 590, 445)

        pygame.display.update()
