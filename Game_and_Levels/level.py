import pygame
from Game_assets.button import load_buttons
import math

class Levels:
    def __init__(self, display, gamestatemanager):
        self.display = display
        self.gamestatemanager = gamestatemanager
        self.background_image = pygame.image.load('Game Images/Updated Background.png')
        self.phase_shift = 0

        self.text_font = pygame.font.Font("Fonts/SuperSalad-qZgvV.ttf", 70)
        self.button_font = pygame.font.Font("Fonts/SuperSalad-qZgvV.ttf", 30)
        self.message_font = pygame.font.Font("Fonts/SuperSalad-qZgvV.ttf", 20)

    def run(self):
        self.display.blit(self.background_image, (0, 0))

        title = self.text_font.render("LEVELS", True, (225, 225, 225))
        self.display.blit(title, (350, 50))
        title = self.message_font.render("For 5 to 9 Years Old", True, (225, 225, 225))
        self.display.blit(title, (70, 300))
        title = self.message_font.render("For 12 to 15 Years Old", True, (225, 225, 225))
        self.display.blit(title, (350, 300))
        title = self.message_font.render("For 18 Years old and Above", True, (225, 225, 225))
        self.display.blit(title, (610, 300))
        title = self.message_font.render("Recommended", True, (225, 225, 225))
        self.display.blit(title, (95, 270))
        title = self.message_font.render("Recommended", True, (225, 225, 225))
        self.display.blit(title, (380, 270))
        title = self.message_font.render("Recommended", True, (225, 225, 225))
        self.display.blit(title, (665, 270))

        self.easy_button, self.normal_button, self.hard_button = load_buttons('easy', 'normal', 'hard')

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.easy_button.is_clicked(pos):
                    self.gamestatemanager.set_state('play')
                elif self.normal_button.is_clicked(pos):
                    self.gamestatemanager.set_state('normalplay')
                elif self.hard_button.is_clicked(pos):
                    self.gamestatemanager.set_state('hardplay')

        self.easy_button.draw(self.display)
        self.normal_button.draw(self.display)
        self.hard_button.draw(self.display)

        def draw_text_sine(text, font, text_col, x, y):
            amplitude = 10
            frequency = 0.01
            vertical_pos = amplitude * math.sin(frequency * x + self.phase_shift)
            img = font.render(text, True, text_col)
            self.display.blit(img, (x, y + vertical_pos))

            self.phase_shift += 0.1

        draw_text_sine("BEGINNER", self.button_font, (100, 100, 100), 110, 465)
        draw_text_sine("MODERATE", self.button_font, (100, 100, 100), 380, 465)
        draw_text_sine("INTENSE", self.button_font, (100, 100, 100), 660, 465)
