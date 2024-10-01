import pygame
import random
from Game_assets.button import load_buttons
from Game_database.database import HighScoreDB
from Game_database.normalgame_highscore_db import NormalGameHighScoreDB
from Game_database.hardgame_highscore_db import HardGameHighScoreDB
from Game_database.profiledatabase import NameDatabase
class Profile:
    def __init__(self, display, gamestatemanager):
        self.display = display
        self.gamestatemanager = gamestatemanager
        self.name_database = NameDatabase()
        self.background_image = pygame.image.load('Game Images/Updated Background.png')
        self.text_font = pygame.font.Font("Fonts/SuperSalad-qZgvV.ttf", 50)
        self.small_text_font = pygame.font.Font("Fonts/SuperSalad-qZgvV.ttf", 20)
        self.input_text_font = pygame.font.Font("Fonts/SuperSalad-qZgvV.ttf", 30)

        self.profile_image = pygame.image.load('Game Images/profile frame.png')
        self.name1_image = pygame.image.load('Game Images/Name Frame.png')
        self.name2_image = pygame.image.load('Game Images/Name Frame.png')
        self.name3_image = pygame.image.load('Game Images/Name Frame.png')
        self.name4_image = pygame.image.load('Game Images/Name Frame.png')
        self.name5_image = pygame.image.load('Game Images/Name Frame.png')

        self.profile_image = pygame.transform.scale(self.profile_image, (300, 300))
        self.name1_image = pygame.transform.scale(self.name1_image, (300, 250))
        self.name2_image = pygame.transform.scale(self.name2_image, (300, 250))
        self.name3_image = pygame.transform.scale(self.name3_image, (300, 250))
        self.name4_image = pygame.transform.scale(self.name4_image, (300, 250))
        self.name5_image = pygame.transform.scale(self.name5_image, (300, 250))

        self.new_image = pygame.image.load('Game Profiles/Profile 1.png')

        self.input_box_rect = pygame.Rect(160, 395, 220, 50)
        self.input_text = self.generate_random_name()

        self.highscore_db = HighScoreDB()
        self.normalgame_highscore_db = NormalGameHighScoreDB()
        self.hardgame_highscore_db = HardGameHighScoreDB()

    def generate_random_name(self):
        names = ['Purrington', 'Meowster', 'Whiskerpaw', 'Slinker', 'Pounceworthy']
        return random.choice(names)

    def scale_image(self, image, width, height):
        return pygame.transform.scale(image, (width, height))

    def run(self):
        self.display.blit(self.background_image, (0, 0))
        self.back_button = load_buttons('back')[0]
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.back_button.is_clicked(pos):
                    self.gamestatemanager.set_state('start')
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                elif len(self.input_text) < 10:
                    self.input_text += event.unicode

                if event.type == pygame.K_RETURN:
                    if self.input_text:
                        self.name_database.add_name(self.input_text)

        title = self.text_font.render("PLAYER'S PROFILE", True, (225, 225, 225))
        self.display.blit(title, (460, 50))
        title = self.text_font.render("HIGHSCORES:", True, (225, 225, 225))
        self.display.blit(title, (460, 170))

        scaled_new_image = self.scale_image(self.new_image, 280, 270)
        self.display.blit(scaled_new_image, (130, 60))

        self.display.blit(self.profile_image, (120, 50))
        self.display.blit(self.name1_image, (123, 290))
        self.display.blit(self.name2_image, (123, 410))
        self.display.blit(self.name3_image, (423, 170))
        self.display.blit(self.name4_image, (423, 290))
        self.display.blit(self.name5_image, (423, 410))

        self.back_button.draw(self.display)

        title = self.small_text_font.render("BEGINNER:", True, (0, 0, 0))
        self.display.blit(title, (450, 250))
        title = self.small_text_font.render("MODERATE:", True, (0, 0, 0))
        self.display.blit(title, (450, 370))
        title = self.small_text_font.render("INTENSE:", True, (0, 0, 0))
        self.display.blit(title, (450, 490))
        title = self.small_text_font.render("NAME:", True, (0, 0, 0))
        self.display.blit(title, (150, 370))
        title = self.small_text_font.render("TOTAL SCORE:", True, (0, 0, 0))
        self.display.blit(title, (150, 490))

        pygame.draw.rect(self.display, (255, 255, 255), self.input_box_rect, 2)
        input_surface = self.input_text_font.render(self.input_text, True, (0, 0, 0))
        self.display.blit(input_surface, (self.input_box_rect.x + 5, self.input_box_rect.y + 5))

        highscore1 = self.highscore_db.get_highscore()
        normal_highscore = self.normalgame_highscore_db.get_highscore()
        hard_highscore = self.hardgame_highscore_db.get_highscore()

        highscore = self.highscore_db.get_highscore()
        highscore_text = self.input_text_font.render(f" {highscore}", True, (0, 0, 0))
        self.display.blit(highscore_text, (530, 270))

        highscore = self.normalgame_highscore_db.get_highscore()
        highscore_text = self.input_text_font.render(f" {highscore}", True, (0, 0, 0))
        self.display.blit(highscore_text, (530, 390))

        highscore = self.hardgame_highscore_db.get_highscore()
        highscore_text = self.input_text_font.render(f" {highscore}", True, (0, 0, 0))
        self.display.blit(highscore_text, (530, 510))

        total_highscore = highscore1 + normal_highscore + hard_highscore

        total_highscore_text = self.input_text_font.render(f" {total_highscore}", True, (0, 0, 0))
        self.display.blit(total_highscore_text, (250, 520))

        pygame.display.flip()