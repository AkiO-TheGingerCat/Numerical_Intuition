import pygame
from Game_assets.button import load_buttons
import math

class Start:
    def __init__(self, display, gamestatemanager):
        self.display = display
        self.gamestatemanager = gamestatemanager
        self.background_image = pygame.image.load('Game Images/Updated Background.png')
        self.phase_shift = 0
        pygame.font.init()

        self.text_font = pygame.font.Font("Fonts/SuperSalad-qZgvV.ttf", 70)
        self.small_text_font = pygame.font.Font("Fonts/SuperSalad-qZgvV.ttf", 30)
        self.button_font = pygame.font.Font("Fonts/SuperSalad-qZgvV.ttf", 40)

    def run(self):
        self.display.blit(self.background_image, (0, 0))

        title = self.text_font.render("NUMERICAL INTUITION", True, (225, 225, 225))
        self.display.blit(title, (190, 50))
        title = self.small_text_font.render("PROFILE", True, (225, 225, 225))
        self.display.blit(title, (380, 510))

        self.start_button, self.exit_button, self.profile_button, self.setting_button = load_buttons("start", 'exit', 'profile', 'settings')

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.start_button.is_clicked(pos):
                    self.gamestatemanager.set_state('play')
                elif self.profile_button.is_clicked(pos):
                    self.gamestatemanager.set_state('profile')
                elif self.setting_button.is_clicked(pos):
                    self.gamestatemanager.set_state('settings')
                elif self.exit_button.is_clicked(pos):
                    pygame.quit()
                    quit()

        self.start_button.draw(self.display)
        self.exit_button.draw(self.display)
        self.profile_button.draw(self.display)
        self.setting_button.draw(self.display)

        pygame.display.update()

        def draw_text_sine(text, font, text_col, x, y):
            amplitude = 10
            frequency = 0.01
            vertical_pos = amplitude * math.sin(frequency * x + self.phase_shift)
            img = font.render(text, True, text_col)
            self.display.blit(img, (x, y + vertical_pos))

            self.phase_shift += 0.1

        draw_text_sine("START", self.button_font, (100, 100, 100), 180, 445)
        draw_text_sine("EXIT", self.button_font, (100, 100, 100), 590, 445)

        pygame.display.update()
